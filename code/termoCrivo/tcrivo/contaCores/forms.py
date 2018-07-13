from django import forms
from . import models


class CriarContaCores(forms.ModelForm):
    class Meta:
        model = models.ContaCores
        fields = ['nome', 'slug', 'texto', 'data', 'foto']

