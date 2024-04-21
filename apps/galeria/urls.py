from django.urls import path
from apps.galeria.views import \
    index, imagem, buscar, nova_imagem, editar_imagem, deletar_imagem

#URL chamam as views. Importar funções
#path -> caminho (endpoint), função, nome da função para referência

urlpatterns = [
    path('', index, name = 'index'),
    path('imagem/<int:foto_id>', imagem, name = 'imagem'),
    path('buscar', buscar, name = 'buscar'),
    path('nova-imagem', nova_imagem, name = 'nova_imagem'),
    path('editar-imagem/<int:foto_id>', editar_imagem, name = 'editar_imagem'),
    path('deletar-imagem/<int:foto_id>', deletar_imagem, name = 'deletar_imagem')
]