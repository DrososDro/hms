from django.shortcuts import redirect, render
from .forms import AddHouseForm
from django.contrib import messages


# Create your views here.
def show_houses(request):
    current_user = request.user
    houses = current_user.house_set.all()
    context = {
        "houses": houses,
    }

    return render(request, "houses/show_houses.html", context)


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
    return render(request, "houses/delete_form.html", context)


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
            return redirect("show-houses")

    context = {
        "form": form,
        "title2": "Add House",
        "button": "Submit",
    }
    return render(request, "houses/payment.html", context)


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
        "title2": "Add House",
        "button": "Submit",
    }
    return render(request, "houses/payment.html", context)
