from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def cadastro_view (request):
    if request.method == 'POST':
        formulario = UserCreationForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('contaCores:lista')
    else:
        formulario = UserCreationForm()
    return render(request, 'contas/cadastro.html', {'formulario':formulario})