from django.urls import path
from . import views

urlpatterns = [
    # home
    path('', views.HomeView.as_view(), name='pagina-inicial'),

    # sobre
    path('sobre/', views.SobreView.as_view(), name='pagina-sobre'),

    # produtos
    path('cadastra_produtos/', views.cadastra_produtos, name='pagina-cadastraprodutos'),
    path('produtos/', views.produtos, name='pagina-produtos'),
    path('produtos/atualizar/<int:pk>/', views.atualizado_produtos, name='pagina-atualizado'),
    path('produto/deleta/<int:id>/', views.deleta_produto, name='deleta-produto'),

    # lojas
    path('cadastra_lojas/', views.cadastra_loja, name='cadastra-loja'),
    path('lojas/', views.lojas, name='pagina-loja'),
    path('atualiza_lojas/<int:id>/', views.atualizado_lojas, name='atualiza-lojas'),
    path('deleta_lojas/<int:id>/', views.deleta_lojas, name='deleta-lojas'),

    # vendedores
    path('cadastra_pessoas/', views.cadastra_pessoas, name='cadastra-pessoas'),
    path('vendedores/', views.vendedores, name='pagina-vendedores'),
    path('atualiza_pessoas/<int:id>/', views.atualiza_pessoas, name='pessoas-atualiza'),
    path('deleta_pessoas/<int:id>/', views.deleta_pessoas, name='deleta-pessoas'),
    
    # contados
    path('enviado/', views.enviado, name='pagina-enviado'),
    path('contados/', views.contados, name='pagina-contados'),
]
