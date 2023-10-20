from django.forms import ModelForm
from django import forms
from decimal import Decimal
from reserva.models import Stand

class StandForm(ModelForm):
    localizacao = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Localização do stand",
        })
    )
    valor = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "money",
            "placeholder": "Valor do stand",
        })
    )

    def clean_valor(self):
        valor = self.cleaned_data["valor"]
        return Decimal(valor.replace(",", "."))

    class Meta:
        model = Stand
        fields = (
            "localizacao",
            "valor",
        )


        