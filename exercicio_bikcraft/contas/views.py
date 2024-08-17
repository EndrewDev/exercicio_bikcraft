from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.

# cadastra
def cadastrar_usuario(request):
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('pagina-inicial')
    else:
        form = UserCreationForm()
    return render(request, 'cadastra_usuario.html', {'form': form})

# acessa
def acessar(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('pagina-inicial')
    else:
        form = AuthenticationForm()
    return render(request, 'acessa.html', {'form': form})

# sair
def sair(request):
    logout(request)
    return redirect('pagina-inicial')