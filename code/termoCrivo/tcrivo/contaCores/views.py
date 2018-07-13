from django.shortcuts import render,redirect
from .models import ContaCores
from django.contrib.auth.decorators import login_required
from . import forms
# Create your views here.
def contaCores(request):
    contaCores = ContaCores.objects.all().order_by('data')
    return render(request, 'contaCores/contaCores.html', {'contaCores':contaCores})

def contaCores_detalhes(request, slug):
    contaCor = ContaCores.objects.get(slug=slug)
    return render(request, 'contaCores/contaCores_detalhes.html',{'contaCor':contaCor})

@login_required(login_url='/contas/login/')
def contaCores_criar(request):
    if request.method == 'POST':
        formulario = forms.CriarContaCores(request.POST, request.FILES)
        if formulario.is_valid():
            instacia = formulario.save(commit=False)
            instacia.autor = request.user
            instacia.save()
            return redirect('contaCores:lista')
    else:
        formulario = forms.CriarContaCores()
    return render(request, 'contaCores/contaCores_criar.html/', {'formulario': formulario})