from django.shortcuts import get_object_or_404, render, redirect
from apps.galeria.models import Fotografia
from django.contrib import messages

#Funções de visualização que geralmente são invocadas pelas URLs do app

def index(request):

    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado')
        return redirect('login')

    fotografias = Fotografia.objects.order_by("-data_fotografia").filter(publicada=True)
    return render(request, 'galeria/index.html', {"cards" : fotografias})

def imagem(request, foto_id):
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    return render(request, 'galeria/imagem.html', {"fotografia":fotografia})

def buscar(request):

    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado')
        return redirect('login')

    fotografias = Fotografia.objects.order_by("-data_fotografia").filter(publicada=True)

    if 'buscar' in request.GET:
        nome_busca = request.GET['buscar']
        if nome_busca:
            fotografias = fotografias.filter(nome__icontains=nome_busca)


    return render(request, 'galeria/buscar.html', {"cards" : fotografias})

def nova_imagem(request):
    return render(request, 'galeria/nova-imagem.html')

def editar_imagem(request):
    pass

def deletar_imagem(request):
    pass
