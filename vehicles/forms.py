from django import forms
from .models import Vehicles, PaymentType, Payment


class AddVehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicles
        fields = "__all__"
        exclude = ["id", "owner"]

    def __init__(self, *args, **kwargs):
        super(AddVehicleForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({"class": "form-control"})


class AddPayTypeForm(forms.ModelForm):
    class Meta:
        model = PaymentType
        fields = "__all__"
        exclude = ["id"]

    def __init__(self, *args, **kwargs):
        super(AddPayTypeForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({"class": "form-control"})


class AddPaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = "__all__"
        exclude = ["id", "owner"]
        widgets = {
            "house": forms.Select(attrs={"type": "select"}),
            "date_of_payment": forms.DateInput(attrs={"type": "date"}),
        }

    def __init__(self, *args, **kwargs):
        super(AddPaymentForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({"class": "form-control"})
