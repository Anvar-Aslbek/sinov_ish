from django import forms
from .models import Baho


class BahoForm(forms.ModelForm):
    class Meta:
        model = Baho
        fields = "__all__"