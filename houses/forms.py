from django import forms
from .models import House


class AddHouseForm(forms.ModelForm):
    class Meta:
        model = House
        fields = "__all__"
        exclude = ["id", "payments", "owner"]

    def __init__(self, *args, **kwargs):
        super(AddHouseForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({"class": "form-control"})
