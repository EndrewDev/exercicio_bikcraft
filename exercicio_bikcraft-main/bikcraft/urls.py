from django.urls import path
from . import views

urlpatterns = [
    # home
    path('', views.HomeView.as_view(), name='pagina-inicial'),

    # sobre
    path('sobre/', views.SobreView.as_view(), name='pagina-sobre'),

    # produtos
    path('produtos/', views.ListProdutosView.as_view(), name='pagina-produtos'),
    path('produtos/cadastrar/', views.CadastraProdutoView.as_view(), name='cadastrar-produtos'),
    path('produtos/atualizar/<int:pk>/', views.UpdateProdutoView.as_view(), name='pagina-atualizado'),
    path('produto/deleta/<int:pk>/', views.DeleteProdutoView.as_view(), name='deleta-produto'),

    # lojas
    path('lojas/cadatrar/', views.CadastraLojaView.as_view(), name='cadastra-loja'),
    path('lojas/', views.ListLojasView.as_view(), name='pagina-loja'),
    path('lojas/atualizar/<int:pk>/', views.UpdateLojaView.as_view(), name='atualiza-lojas'),
    path('lojas/deletar/<int:pk>/', views.DeleteLojaView.as_view(), name='deleta-lojas'),

    # vendedores
    path('pessoas/cadastrar/', views.CadastraVendedorView.as_view(), name='cadastra-pessoas'),
    path('vendedores/', views.ListVendedoresView.as_view(), name='pagina-vendedores'),
    path('pessoas/atualizar/<int:pk>/', views.UpdateVendedorView.as_view(), name='pessoas-atualiza'),
    path('pessoas/deletar/<int:pk>/', views.DeleteVendedorView.as_view(), name='deleta-pessoas'),
    
    # contados
    path('enviado/', views.EnviadoView.as_view(), name='pagina-enviado'),
    path('contados/', views.ContadosView.as_view(), name='pagina-contados'),
]
