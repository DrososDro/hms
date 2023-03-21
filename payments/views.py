from django.shortcuts import render, redirect
from .forms import AddPayTypeForm
from django.contrib import messages
from .models import PaymentType

# Create your views here.


def add_payment_type(request):
    form = AddPayTypeForm()
    if request.method == "POST":
        form = AddPayTypeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "You successfully add payment type")
            return redirect("show-payment-types")

    context = {
        "form": form,
        "button": "Submit",
        "title2": "Add payment type",
    }
    return render(request, "houses/pay.html", context)


def show_payment_types(request):
    payment = PaymentType.objects.all()
    context = {"payments": payment}
    return render(request, "houses/show_payment_types.html", context)


def edit_payment_type(request, pk):
    payment = PaymentType.objects.get(id=pk)
    form = AddPayTypeForm(instance=payment)
    if request.method == "POST":
        form = AddPayTypeForm(request.POST, instance=payment)
        if form.is_valid():
            form.save()
            messages.success(request, "You successfully add payment type")
            return redirect("show-payment-types")

    context = {
        "form": form,
        "button": "Submit",
        "title2": "Add payment type",
    }
    return render(request, "houses/pay.html", context)


def delete_payment_type(request, pk):
    payment = PaymentType.objects.get(id=pk)
    if request.method == "POST":
        payment.delete()
        messages.success(request, "successfully Delete the payment type")
        return redirect("show-payment-types")

    context = {"title": payment.name}
    return render(request, "delete_form.html", context)
