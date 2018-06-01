from django.shortcuts import render
from .models import ContaCores
# Create your views here.
def contaCores(request):
    contaCores = ContaCores.objects.all().order_by('data')
    return render(request, 'contaCores/contaCores.html', {'contaCores':contaCores})

def contaCores_detalhes(request, nome):
    contaCor = ContaCores.objects.get(nome=nome)
    return render(request, 'contaCores/contaCores_detalhes.html',{'contaCor':contaCor})