from django.shortcuts import redirect, render
from .forms import AddVehicleForm, AddPaymentForm, AddPayTypeForm
from django.contrib import messages
from accounts.decorators import authenticated_user, required_permissions
from .models import PaymentType


url_list = [
    "delete-vehicle",
    "show-vehicles",
    "edit-vehicle",
    "add-vehicle-payment",
    "add-vehicle",
    "add-vehicle-payment-type",
    "show-vehicle-payments",
    "show-vehicle-payment-types",
    "edit-vehicle-payment-type",
    "delete-vehicle-payment-type",
    "show-payments-vehicle",
]


# Create your views here.
@authenticated_user
@required_permissions(["vehicles"])
def show_vehicles(request):
    current_user = request.user
    vehicles = current_user.vehicles_set.all()
    context = {"houses": vehicles, "vehicles_url_list": url_list}

    return render(request, "vehicles/show_vehicles.html", context)


@authenticated_user
@required_permissions(["vehicles"])
def delete_vehicle(request, pk):
    current_user = request.user
    vehicles = current_user.vehicles_set.get(id=pk)
    if request.method == "POST":
        vehicles.delete()
        messages.success(request, "Vehicle successfully Deleted")
        return redirect("show-vehicles")
    context = {"title": vehicles.licence_plate, "vehicles_url_list": url_list}
    return render(request, "delete_form.html", context)


@authenticated_user
@required_permissions(["vehicles"])
def edit_vehicle(request, pk):
    current_user = request.user
    house = current_user.vehicles_set.get(id=pk)
    form = AddVehicleForm(instance=house)
    if request.method == "POST":
        form = AddVehicleForm(request.POST, instance=house)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.owner = current_user
            instance.save()
            messages.success(request, "Vehicle successfully Edited")
            return redirect("show-vehicles")

    context = {
        "form": form,
        "title2": "Edit Vehicle",
        "button": "Submit",
        "vehicles_url_list": url_list,
    }
    return render(request, "vehicles/pay.html", context)


def add_payment(request):
    form = AddPaymentForm()

    if request.method == "POST":
        form = AddPaymentForm(request.POST, request.FILES)

        if form.is_valid():
            instance = form.save(commit=False)
            instance.owner = request.user
            instance.save()
            return redirect("show-vehicle-payments")

    context = {
        "form": form,
        "button": "Submit",
        "title2": "Add Vehicle payment",
        "vehicles_url_list": url_list,
    }

    return render(request, "vehicles/pay.html", context)


@authenticated_user
@required_permissions(["vehicles"])
def add_vehicle(request):
    current_user = request.user
    form = AddVehicleForm()
    if request.method == "POST":
        form = AddVehicleForm(request.POST)
        if form.is_valid():
            print("valid")
            instance = form.save(commit=False)
            instance.owner = current_user
            instance.save()
            messages.success(request, "Vehicle successfully Added")
            return redirect("add-vehicle-payment")

    context = {
        "form": form,
        "title2": "Add Vehicle",
        "button": "Submit",
        "vehicles_url_list": url_list,
    }
    return render(request, "vehicles/pay.html", context)


@authenticated_user
@required_permissions(["vehicles"])
def add_payment_type(request):
    form = AddPayTypeForm()
    if request.method == "POST":
        form = AddPayTypeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "You successfully add payment type")
            return redirect("show-vehicle-payment-types")

    context = {
        "form": form,
        "button": "Submit",
        "title2": "Add Vehicle payment type",
        "vehicles_url_list": url_list,
    }
    return render(request, "vehicles/pay.html", context)


@authenticated_user
@required_permissions(["vehicles"])
def show_payments(request):
    current_user = request.user
    payments = current_user.vehicle_owner.all()
    context = {
        "payments": payments,
        "vehicles_url_list": url_list,
    }  # , "vehicles_url_list": url_list
    return render(request, "vehicles/show_payments.html", context)


@authenticated_user
@required_permissions(["vehicles"])
def show_payment_types(request):
    payment = PaymentType.objects.all()
    context = {"payments": payment, "vehicles_url_list": url_list}
    return render(request, "vehicles/show_payment_types.html", context)


@authenticated_user
@required_permissions(["vehicles"])
def edit_payment_type(request, pk):
    payment = PaymentType.objects.get(id=pk)
    form = AddPayTypeForm(instance=payment)
    if request.method == "POST":
        form = AddPayTypeForm(request.POST, instance=payment)
        if form.is_valid():
            form.save()
            messages.success(request, "You successfully Edit payment type")
            return redirect("show-vehicle-payment-types")

    context = {
        "form": form,
        "button": "Submit",
        "title2": "Edit vehicle payment type",
        "vehicles_url_list": url_list,
    }
    return render(request, "vehicles/pay.html", context)


@authenticated_user
@required_permissions(["vehicles"])
def delete_payment_type(request, pk):
    payment = PaymentType.objects.get(id=pk)
    if request.method == "POST":
        payment.delete()
        messages.success(request, "successfully Delete the payment type")
        return redirect("show-vehicle-payment-types")

    context = {"title": payment.name, "vehicles_url_list": url_list}
    return render(request, "delete_form.html", context)


@authenticated_user
@required_permissions(["vehicles"])
def show_payments_from_vehicles(request, pk):
    current_user = request.user
    payments = current_user.vehicle_owner.filter(vehicle=pk)
    context = {
        "payments": payments,
        "vehicles_url_list": url_list,
    }  # , "vehicles_url_list": url_list
    return render(request, "vehicles/show_payments.html", context)


@authenticated_user
@required_permissions(["vehicles"])
def show_payments_from_render(request, pk):
    current_user = request.user
    if pk == "None":
        payments = current_user.vehicle_owner.filter(render=None)
    else:
        payments = current_user.vehicle_owner.filter(render=pk)
    context = {
        "payments": payments,
        "vehicles_url_list": url_list,
    }  # , "vehicles_url_list": url_list
    return render(request, "vehicles/show_payments.html", context)


@authenticated_user
@required_permissions(["vehicles"])
def show_payments_from_payment_type(request, pk):
    current_user = request.user
    payments = current_user.vehicle_owner.filter(payment_type=pk)
    context = {
        "payments": payments,
        "vehicles_url_list": url_list,
    }  # , "vehicles_url_list": url_list
    return render(request, "vehicles/show_payments.html", context)
