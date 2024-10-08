from django.shortcuts import render, redirect, get_object_or_404
from .forms import BikeModelForm, ContadosModelForm, LojasModelForm, PessoasModelForm
from .models import Bike, Contados, Lojas, Pessoas
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import ListView, DeleteView, DetailView, CreateView, TemplateView, UpdateView

# home class:
class HomeView(TemplateView):
    def get(self, request):
        return render(request, 'bike.html')

# sobre class:
class SobreView(TemplateView):
    def get(self, request):
        return render(request, 'sobre.html')

# cadastra produtos:
# classes:
@method_decorator(login_required, name='dispatch')
class CadastraProdutoView(CreateView):
    model = Bike
    template_name = 'cadastra_produtos.html'
    form_class = BikeModelForm
    success_url = '/produtos/'

#função
# @login_required
# def cadastra_produtos(self, request):

#     user = request.user
#     if user.is_authenticated:

#         if request.method == 'POST':
#             bike_form = BikeModelForm(request.POST, request.FILES)
#             if bike_form.is_valid():
#                 bike_form.save()
#                 return redirect('pagina-produtos')
#         else:
#             bike_form = BikeModelForm()
#             return render(request, 'cadastra_produtos.html', {'form': bike_form})
#     else:
#         return redirect('pagina-cadastraprodutos')
    
# recebe as informação para html:
# Classes:
class ListProdutosView(ListView):
    model = Bike
    template_name = 'produtos.html'
    context_object_name = 'produtos'

#Função:
# def listprodutos(request):
#     bike = Bike.objects.all()
#     search = request.GET.get('search')
#     if search:
#         bike = bike.filter(modelo__icontains=search)
#     return render(request, 'produtos.html', {'produtos': bike})

# atualiza produto:
# classes:
@method_decorator(login_required, name='dispatch')
class UpdateProdutoView(UpdateView):
    model = Bike
    template_name = 'cadastra_produtos_atualizar.html'
    form_class = BikeModelForm
    success_url = '/produtos/'
    
#Função:
# @login_required
# def atualizado_produtos(self, request, pk):
    # bike = get_object_or_404(Bike, pk=pk)
    # print(request.POST)
    # if request.method == 'POST':
        # form = BikeModelForm(request.POST, instance=bike)
        # if form.is_valid():
            # form.save()
            # return redirect('pagina-produtos')
    # else:
        # form = BikeModelForm(instance=bike)
    # return render(request, 'cadastra_produtos_atualizar.html', {'form': form, 'bike': bike})

# deleta produto:
@method_decorator(login_required, name='dispatch')
class DeleteProdutoView(DeleteView):
    model = Bike
    template_name = 'produtos.html'
    success_url = '/produtos/'

# Função:
# @login_required
# def deleta_produto(request, id):
#     deleta_produtos = get_object_or_404(Bike, pk=id)
#     print(deleta_produtos)
#     deleta_produtos.delete()
#     return redirect('pagina-produtos')

# contado:
@method_decorator(login_required, name='dispatch')
class ContadosView(CreateView):
    model = Contados
    template_name = 'contados.html'
    form_class = ContadosModelForm
    success_url = '/enviado/'

# @login_required
# def contados(self, request):
#     if request.method == "POST":
#         contados_form = ContadosModelForm(request.POST, request.FILES)
#         if contados_form.is_valid():
#             contados_form.save()
#             return redirect('pagina-enviado')
#     else:
#         contados_form = ContadosModelForm()
#     return render(request, 'contados.html', {'contados': contados_form})

# enviado com sucesso do contado:
def enviado(request):
    contados = Contados.objects.all()
    return render(request, 'enviado.html', {'contados': contados})

# cadastra loja:
# classes
@method_decorator(login_required, name='dispatch')
class CadastraLojaView(CreateView):
    model = Lojas
    template_name = 'cadastra_lojas.html'
    form_class = LojasModelForm
    success_url = '/lojas/'

# Função
# @login_required
# def cadastra_loja(self, request):
#     if request.method == 'POST':
#         lojas_form = LojasModelForm(request.POST, request.FILES)
#         if lojas_form.is_valid():
#             lojas_form.save()
#             return redirect('pagina-loja')
#     else:
#         lojas_form = LojasModelForm()
#     return render(request, 'cadastra_lojas.html', {'lojas_form': lojas_form})

# recebe as informação para html:
# classes
class ListLojasView(ListView):
    model = Lojas
    template_name = 'lojas.html'
    context_object_name = 'lojas'

# função
# def lojas(request):
#     lojas = Lojas.objects.all()
#     search = request.GET.get('search')
#     if search:
#         lojas = lojas.filter(modelo__icontains=search)
#     return render(request, 'lojas.html', {'lojas': lojas})

# atualiza loja:
# Classes
@method_decorator(login_required, name='dispatch')
class UpdateLojaView(UpdateView):
    model = Lojas
    template_name = 'atualiza_loja.html'
    form_class = LojasModelForm
    success_url = '/lojas/'
    
# Função
# @login_required
# def atualizado_lojas(self, request, id):
#     bike = get_object_or_404(Bike, id=id)

#     if request.method == 'POST':
#         modelo = request.POST.get('modelo')
#         preco = request.POST.get('preco')
#         descricao = request.POST.get('descricao')
#         foto = request.POST.get('foto')

#     if len(modelo) > 0:
#         bike.modelo = modelo
#         if len(preco) > 0:
#             bike.preco = preco
#         if len(descricao) > 0:
#             bike.descricao = descricao
#         if len(foto) > 0:
#             bike.foto = foto
#         bike.save()
#         return redirect('pagina-loja')
#     return render(request, 'cadastra_lojas.html', {'bike': bike})

# deleta loja:
# Classes
@method_decorator(login_required, name='dispatch')
class DeleteLojaView(DeleteView):
    model = Lojas
    template_name = 'lojas.html'
    success_url = '/lojas/'

# Função
# @login_required
# def deleta_lojas(request, id):
#     deleta_lojas = get_object_or_404(Lojas, id=id)
#     deleta_lojas.delete()
#     return redirect('pagina-loja')

#cadstra vendedor:
# Classes
@method_decorator(login_required, name='dispatch')
class CadastraVendedorView(CreateView):
    model = Pessoas
    template_name = 'cadastra_vendedor.html'
    form_class = PessoasModelForm
    success_url = '/vendedores/'

# função
# @login_required
# def cadastra_pessoas(self, request):
#     if request.method == 'POST':
#         pessoas = PessoasModelForm(request.POST, request.FILES)
#         if pessoas.is_valid():
#             pessoas.save()
#             return redirect('pagina-vendedores')
#     else:
#         pessoas = PessoasModelForm()
#     return render(request, 'pessoas.html', {'pessoas': pessoas})
    
# recebe as informação para html:
# Classes
class ListVendedoresView(ListView):
    model = Pessoas
    template_name = 'vendedores.html'
    context_object_name = 'vendedores'

# Função
# def vendedores(request):
#     informacao_pessoas = Pessoas.objects.all()
#     return render(request, 'vendedores.html', {'vendedores': informacao_pessoas})

#atualiza vendedor:
# Classes
@method_decorator(login_required, name='dispatch')
class UpdateVendedorView(UpdateView):
    model = Pessoas
    template_name = 'atualiza_vendedores.html'
    form_class = PessoasModelForm
    success_url = '/vendedores/'

# Função
# @login_required
# def atualiza_pessoas(self, request, id):
#     pessoas_atualiza = get_object_or_404(Pessoas, id=id)

#     if request.method == 'POST':
#         nome = request.POST.get('nome')
#         cpf = request.POST.get('cpf')
#         opcao_lojas = request.POST.get('opcao_lojas')

#         if len(nome) > 0:
#             pessoas_atualiza.nome = nome
#         if len(cpf) > 0:
#             pessoas_atualiza.cpf = cpf
#         if len(opcao_lojas) > 0:
#             pessoas_atualiza.opcao_lojas = opcao_lojas
#         pessoas_atualiza.save()
#         return redirect('pagina-vendedores')
#     return render(request, 'pessoas.html', {'vendeodres': pessoas_atualiza})

# deleta vendedor:
#Classes
@method_decorator(login_required, name='dispatch')
class DeleteVendedorView(DeleteView):
    model = Pessoas
    template_name = 'vendedores.html'
    success_url = '/vendedores/'

# função
# @login_required
# def deleta_pessoas(self, request, id):
#     pessoas = get_object_or_404(Pessoas, id=id)
#     pessoas.delete()
#     return redirect('pagina-vendedores')