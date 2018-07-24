from django import forms
from .models import ContaCores
from PIL import Image
from django.core.files import File
from .termo import Tratamento


class CriarContaCores(forms.ModelForm):

    class Meta:
        model = ContaCores
        fields = ['nome', 'slug', 'texto', 'data', 'foto']
    
    def analisar(self):
        foto = super(CriarContaCores, self).save()
        img = Image.open(foto.file)
        trat = Tratamento(img)
        trat.vermelho()
        trat.laranja()
        trat.amarelo()
        trat.verde()
        trat.ciano()
        trat.azul()
        trat.violeta()
        trat.magenta()
        trat.branco()


# class fotoForm(forms.ModelForm):
#     class Meta:
#         foto = forms.ImageField()
    

