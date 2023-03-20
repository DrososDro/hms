from django import forms
from .models import WorkCalc, WorkTime
from django.db import models


class AddHourForm(forms.ModelForm):
    class Meta:
        model = WorkCalc
        fields = "__all__"
        exclude = ["owner"]
        widgets = {
            "date": forms.DateInput(
                attrs={
                    "type": "date",
                    "value": None,
                }
            ),
            "start_of_work": forms.TimeInput(attrs={"type": "time"}),
            "end_of_work": forms.TimeInput(attrs={"type": "time"}),
        }

    def __init__(self, *args, **kwargs):
        super(AddHourForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({"class": "form-control"})


class AddWorkTimes(forms.ModelForm):
    class Meta:
        model = WorkTime
        fields = "__all__"
        exclude = ["owner"]

        widgets = {
            "work_hour_start": forms.TimeInput(attrs={"type": "time"}),
            "work_hour_end": forms.TimeInput(attrs={"type": "time"}),
        }

    def __init__(self, *args, **kwargs):
        super(AddWorkTimes, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({"class": "form-control"})
