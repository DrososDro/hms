from django.forms import widgets
from django.shortcuts import render, redirect
from django.contrib import messages
from datetime import timedelta, datetime
from .models import WorkTime, WorkCalc
from .forms import AddHourForm, AddWorkTimes
from .utils import minute_interval
from accounts.decorators import authenticated_user, required_permissions

url_list = [
    "show-hours",
    "add-hours",
    "delete-hours",
    "show-sum",
    "set-work-hours",
]


# Create your views here.
@authenticated_user
@required_permissions(["work"])
def show_hours(request):
    current_user = request.user
    hours = current_user.workcalc_set.all()
    context = {
        "hours": hours,
        "hour_url_list": url_list,
    }
    return render(request, "work_hours/show_hours.html", context)


@authenticated_user
@required_permissions(["work"])
def delete_hours(request, pk):
    current_user = request.user
    hour = current_user.workcalc_set.get(id=pk)
    if request.method == "POST":
        hour.delete()
        messages.success(request, "You Successfuly delete the object")
        return redirect("show-hours")

    context = {
        "title": hour.date,
        "hour_url_list": url_list,
    }
    return render(request, "delete_form.html", context)


@authenticated_user
@required_permissions(["work"])
def add_hours(request):
    current_user = request.user
    last = current_user.workcalc_set.all().last()
    try:
        WorkTime.objects.get(owner=current_user)
    except Exception:
        return redirect("set-work-hours")
    form = AddHourForm(
        initial={"date": last.date + timedelta(days=1) if last else None}
    )
    if request.method == "POST":
        form = AddHourForm(request.POST)
        if current_user.workcalc_set.filter(date=request.POST["date"]).exists():
            messages.error(request, "Date already exists for this user")
        elif form.is_valid():
            form_data = form.cleaned_data
            if form_data["day"] != "0":
                instance = form.save(commit=False)
                instance.owner = current_user
                instance.start_of_work = None
                instance.end_of_work = None
                instance.save()
                messages.success(request, "Successfully Added")
                return redirect("add-hours")
            else:
                if (
                    form_data["start_of_work"] is None
                    or form_data["end_of_work"] is None
                ):
                    messages.error(
                        request, "Start or End Field is blanck Please fill it."
                    )
                else:
                    instance = form.save(commit=False)
                    instance.owner = current_user
                    instance.save()
                    messages.success(request, "Successfully Added")
                    return redirect("add-hours")
    context = {
        "form": form,
        "button": "Submit",
        "title2": "Add Hours",
        "hour_url_list": url_list,
    }

    return render(request, "work_hours/add_hours.html", context)


@authenticated_user
@required_permissions(["work"])
def set_work_times(request):
    current_user = request.user
    try:
        time = WorkTime.objects.get(owner=current_user)

        if time:
            form = AddWorkTimes(instance=time)

    except Exception:
        form = AddWorkTimes()
    context = {
        "hour_url_list": url_list,
        "form": form,
        "button": "Submit",
        "title2": "Set Working Hours",
    }
    if request.method == "POST":
        try:
            form = AddWorkTimes(request.POST, instance=time)
        except Exception:
            form = AddWorkTimes(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.owner = current_user
            print(instance)
            instance.save()
            messages.success(request, "Work Hours Successfully changed")
            return redirect("add-hours")

    return render(request, "work_hours/add_hours.html", context)


@authenticated_user
@required_permissions(["work"])
def calculate_hours(request):
    current_user = request.user

    try:
        time = WorkTime.objects.get(owner=current_user)
    except WorkTime.DoesNotExist:
        return redirect("set-work-hours")

    # here i tyl to see if there is any object and if there isnt redirect
    try:
        WorkCalc.objects.filter(owner=current_user)
    except WorkCalc.DoesNotExist:
        return redirect("add-hours")

    hours_text = ""
    hours_text1 = ""
    used = False
    mini = current_user.workcalc_set.first().date
    first = mini
    maxi = current_user.workcalc_set.last().date
    last = maxi

    if request.method == "POST":
        id_from = datetime.strptime(
            request.POST.get("from"),
            "%Y-%m-%d",
        ).date()
        id_to = datetime.strptime(request.POST.get("to"), "%Y-%m-%d").date()
        hours_list = current_user.workcalc_set.filter(
            date__gte=id_from,
            date__lte=id_to,
        )
        before = timedelta(minutes=0)
        after = timedelta(minutes=0)
        work_days = 0
        weekend = 0
        times_off = 0
        sick_leave = 0
        public_holidays = 0

        for item in hours_list:
            if item.day == "0":
                before += minute_interval(item.start_of_work, time.work_hour_start)
                after += minute_interval(time.work_hour_end, item.end_of_work)
                work_days += 1
            else:
                if item.day == "1":
                    weekend += 1
                elif item.day == "2":
                    times_off += 1
                elif item.day == "3":
                    sick_leave += 1
                elif item.day == "4":
                    public_holidays += 1

        used = True
        hours_text = f"Total days: {len(hours_list)},  Extra time: {after}, Work days: {work_days}"
        hours_text1 = f" Weekend: {weekend}, Time off: {times_off}, Sick leave: {sick_leave}, Public holidays: {public_holidays}"
        first = hours_list.first().date
        last = hours_list.last().date

    context = {
        "used": used,
        "hour_url_list": url_list,
        "mini": mini,
        "maxi": maxi,
        "hour_text": hours_text,
        "hour_text1": hours_text1,
        "first": first,
        "last": last,
        "title1": "Calculate Hours",
        "button": "Calculate",
    }
    return render(request, "work_hours/sum.html", context)
