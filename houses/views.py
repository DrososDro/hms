from django.shortcuts import redirect, render
from .forms import AddHouseForm, AddPaymentForm, AddPayTypeForm
from django.contrib import messages
from accounts.decorators import authenticated_user, required_permissions
from .models import PaymentType


# Create your views here.
@authenticated_user
@required_permissions(["houses"])
def show_houses(request):
    current_user = request.user
    houses = current_user.house_set.all()
    context = {
        "houses": houses,
    }

    return render(request, "houses/show_houses.html", context)


@authenticated_user
@required_permissions(["houses"])
def delete_house(request, pk):
    current_user = request.user
    houses = current_user.house_set.get(id=pk)
    if request.method == "POST":
        houses.delete()
        messages.success(request, "House successfully Deleted")
        return redirect("show-houses")
    context = {
        "title": houses.name,
    }
    return render(request, "delete_form.html", context)


@authenticated_user
@required_permissions(["houses"])
def add_house(request):
    current_user = request.user
    form = AddHouseForm()
    if request.method == "POST":
        form = AddHouseForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.owner = current_user
            instance.save()
            messages.success(request, "House successfully Added")
            return redirect("add-house-payment")

    context = {
        "form": form,
        "title2": "Add House",
        "button": "Submit",
    }
    return render(request, "houses/pay.html", context)


@authenticated_user
@required_permissions(["houses"])
def edit_house(request, pk):
    current_user = request.user
    house = current_user.house_set.get(id=pk)
    form = AddHouseForm(instance=house)
    if request.method == "POST":
        form = AddHouseForm(request.POST, instance=house)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.owner = current_user
            instance.save()
            messages.success(request, "House successfully Edited")
            return redirect("show-houses")

    context = {
        "form": form,
        "title2": "Edit House",
        "button": "Submit",
    }
    return render(request, "houses/pay.html", context)


@authenticated_user
@required_permissions(["houses"])
def add_payment(request):
    form = AddPaymentForm()

    if request.method == "POST":
        form = AddPaymentForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect("show-houses")

    context = {"form": form, "button": "Submit", "title2": "Add payment"}

    return render(request, "houses/pay.html", context)


@authenticated_user
@required_permissions(["houses"])
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


@authenticated_user
@required_permissions(["houses"])
def show_payment_types(request):
    payment = PaymentType.objects.all()
    context = {"payments": payment}
    return render(request, "houses/show_payment_types.html", context)


@authenticated_user
@required_permissions(["houses"])
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


@authenticated_user
@required_permissions(["houses"])
def delete_payment_type(request, pk):
    payment = PaymentType.objects.get(id=pk)
    if request.method == "POST":
        payment.delete()
        messages.success(request, "successfully Delete the payment type")
        return redirect("show-payment-types")

    context = {"title": payment.name}
    return render(request, "delete_form.html", context)


@authenticated_user
@required_permissions(["houses"])
def show_payments(request):
    current_user = request.user
    payments = current_user.payment_set.all()
    context = {"payments": payments}  # , "house_url_list": url_list
    return render(request, "houses/show_payments.html", context)
