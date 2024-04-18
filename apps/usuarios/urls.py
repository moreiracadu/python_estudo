from django.urls import path
from apps.usuarios.views import login, cadastro, logout

#URL chamam as views. Importar funções
#path -> caminho (endpoint), função, nome da função para referência

urlpatterns = [
    path('login', login, name='login'),
    path('cadastro', cadastro, name='cadastro'),
    path('logout', logout, name='logout')
]