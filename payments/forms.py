from django import forms
from .models import PaymentType, Payment


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
        exclude = ["id"]
        widgets = {
            "house": forms.RadioSelect(attrs={"type": "radio"}),
            "date_of_payment": forms.DateInput(attrs={"type": "date"}),
        }

    def __init__(self, *args, **kwargs):
        super(AddPaymentForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            if name == "house":
                field.widget.attrs.update({"class": "form-check-input"})
                print(field.widget.attrs)
                pass
            else:
                field.widget.attrs.update({"class": "form-control"})
