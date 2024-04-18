from django.shortcuts import render, redirect
from apps.usuarios.forms import LoginForms, CadastroForms
from django.contrib.auth.models import User
from django.contrib import messages, auth


# Create your views here.

def login(request):
    form = LoginForms()

    if request.method == 'POST':
        form = LoginForms(request.POST)

        if form.is_valid():
            nome = form['nome_login'].value()
            senha = form['senha'].value()

        #authenticate valida se os parâmetros existem no banco de dados
            
        usuario = auth.authenticate(
            request,
            username=nome,
            password=senha
        )

        #usuário precisa voltar como Valid ou None

        if usuario is not None:
            auth.login(request, usuario)
            messages.success(request, "Login realizado com sucesso.")
            return redirect('index')
        else:
            messages.error(request, 'Erro ao efetuar login.')
            return redirect('login')

    return render(request, 'usuarios/login.html', {"form" : form})

def cadastro(request):
    
    form = CadastroForms()

    if request.method == 'POST':
        form = CadastroForms(request.POST)

        if form.is_valid():
    
            nome = form['nome_cadastro'].value()
            email = form['email'].value()
            senha = form['senha_cadastro'].value()

            # Verificar se o usuário existe
            if User.objects.filter(username=nome).exists():
                messages.error(request, 'Usuário já cadastrado.')
                return redirect('cadastro')  # Redirecionar para a página inicial após o cadastro


            # Criar usuário
            user = User.objects.create_user(username=nome, email=email, password=senha)
            user.save()
            messages.success(request, 'Usuário cadastrado com sucesso!')
            return redirect('login')  # Redirecionar para a página inicial após o cadastro


    return render(request, 'usuarios/cadastro.html', {"form": form})

def logout(request):
    auth.logout(request)
    messages.success(request, "Logout realizado com sucesso.")
    return redirect('login')