from django.urls import path
from . import views

urlpatterns = [
    path('', views.acessar, name='acessar'),
    path('cadastrar/',views.cadastrar_usuario, name='cadastra-usuario'),
    path('sair/', views.sair, name='sair')
]