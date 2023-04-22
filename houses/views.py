from django.shortcuts import redirect, render
from .forms import AddHouseForm, AddPaymentForm, AddPayTypeForm
from django.contrib import messages
from accounts.decorators import authenticated_user, required_permissions
from .models import PaymentType


url_list = [
    "show-houses",
    "delete-house",
    "add-house",
    "edit-house",
    "add-house-payment",
    "add-payment-type",
    "show-payments",
    "show-payments-house",
    "show-payments-render",
    "show-payments-payment-type",
    "show-payment-types",
    "edit-payment-types",
    "delete-payment-type",
]


# Create your views here.
@authenticated_user
@required_permissions(["houses"])
def show_houses(request):
    current_user = request.user
    houses = current_user.house_set.all()
    context = {"houses": houses, "house_url_list": url_list}

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
    context = {"title": houses.name, "house_url_list": url_list}
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
        "house_url_list": url_list,
    }
    return render(request, "pay.html", context)


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
        "house_url_list": url_list,
    }
    return render(request, "pay.html", context)


@authenticated_user
@required_permissions(["houses"])
def add_payment(request):
    form = AddPaymentForm()

    if request.method == "POST":
        form = AddPaymentForm(request.POST, request.FILES)

        if form.is_valid():
            instance = form.save(commit=False)
            instance.owner = request.user
            instance.save()
            return redirect("show-payments")

    context = {
        "form": form,
        "button": "Submit",
        "title2": "Add payment",
        "house_url_list": url_list,
    }

    return render(request, "pay.html", context)


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
        "house_url_list": url_list,
    }
    return render(request, "pay.html", context)


@authenticated_user
@required_permissions(["houses"])
def show_payment_types(request):
    payment = PaymentType.objects.all()
    context = {"payments": payment, "house_url_list": url_list}
    return render(request, "show_payment_types.html", context)


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
        "house_url_list": url_list,
    }
    return render(request, "pay.html", context)


@authenticated_user
@required_permissions(["houses"])
def delete_payment_type(request, pk):
    payment = PaymentType.objects.get(id=pk)
    if request.method == "POST":
        payment.delete()
        messages.success(request, "successfully Delete the payment type")
        return redirect("show-payment-types")

    context = {"title": payment.name, "house_url_list": url_list}
    return render(request, "delete_form.html", context)


@authenticated_user
@required_permissions(["houses"])
def show_payments(request):
    current_user = request.user
    payments = current_user.owner.all()
    context = {
        "payments": payments,
        "house_url_list": url_list,
    }  # , "house_url_list": url_list
    return render(request, "houses/show_payments.html", context)


@authenticated_user
@required_permissions(["houses"])
def show_payments_from_houses(request, pk):
    current_user = request.user
    payments = current_user.owner.filter(house=pk)
    context = {
        "payments": payments,
        "house_url_list": url_list,
    }  # , "house_url_list": url_list
    return render(request, "houses/show_payments.html", context)


@authenticated_user
@required_permissions(["houses"])
def show_payments_from_render(request, pk):
    current_user = request.user
    if pk == "None":
        payments = current_user.owner.filter(render=None)
    else:
        payments = current_user.owner.filter(render=pk)
    context = {
        "payments": payments,
        "house_url_list": url_list,
    }  # , "house_url_list": url_list
    return render(request, "houses/show_payments.html", context)


@authenticated_user
@required_permissions(["houses"])
def show_payments_from_payment_type(request, pk):
    current_user = request.user
    payments = current_user.owner.filter(payment_type=pk)
    context = {
        "payments": payments,
        "house_url_list": url_list,
    }  # , "house_url_list": url_list
    return render(request, "houses/show_payments.html", context)
