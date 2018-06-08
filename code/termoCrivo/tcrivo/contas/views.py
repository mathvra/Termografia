from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

# Create your views here.
def cadastro_view (request):
    if request.method == 'POST':
        formulario = UserCreationForm(request.POST)
        if formulario.is_valid():
            usuario = formulario.save()
            login(request, usuario)
            return redirect('contaCores:lista')
    else:
        formulario = UserCreationForm()
    return render(request, 'contas/cadastro.html', {'formulario':formulario})

def login_view (request):
    if request.method == 'POST':
        formulario = AuthenticationForm(data = request.POST)
        if formulario.is_valid():
            usuario = formulario.get_user()
            login(request, usuario)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))

            return redirect('contaCores:lista')

    else:
        formulario = AuthenticationForm()
    return render(request, 'contas/login.html', {'formulario':formulario})

def logout_view (request):
    if request.method== 'POST':
        logout(request)
        return redirect('contaCores:lista')