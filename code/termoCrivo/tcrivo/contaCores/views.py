from django.shortcuts import render,redirect
from .models import ContaCores
from django.contrib.auth.decorators import login_required
from . import forms
from .termo import Tratamento
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

def contaCores_trat(request, foto):
    if request.method == 'POST':
        #Chamando func:
        trat = Tratamento(foto)
        trat.vermelho()
        trat.laranja()
        trat.amarelo()
        trat.verde()
        trat.ciano()
        trat.azul()
        trat.violeta()
        trat.magenta()
        trat.branco()
        if trat.is_valid():
            instacia = trat.save(commit=False)
            instacia.autor = request.user
            instacia.save()
            return redirect('contaCores:lista')
    else:
        trat = Tratamento(foto)
    return render(request, 'contaCores/contaCores_trat.html/', {'trat': trat})