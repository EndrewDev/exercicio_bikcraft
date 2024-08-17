from django.shortcuts import render, redirect, get_object_or_404
from .forms import BikeModelForm, ContadosModelForm, LojasModelForm, PessoasModelForm, DetalheModeForm
from .models import Bike, Contados, Lojas, Pessoas, DetalheBikes
from django.contrib.auth.decorators import login_required

# home:
def home(request):
    return render(request, 'bike.html')

# sobre:
def sobre(request):
    return render(request, 'sobre.html')

# cadastra produtos:
@login_required
def cadastra_produtos(request):

    user = request.user
    if user.is_authenticated:

        if request.method == 'POST':
            bike_form = BikeModelForm(request.POST, request.FILES)
            if bike_form.is_valid():
                bike_form.save()
                return redirect('pagina-produtos')
        else:
            bike_form = BikeModelForm()
            return render(request, 'cadastra_produtos.html', {'form': bike_form})
    else:
        return redirect('pagina-cadastraprodutos')
        

# recebe as informação para html:
def produtos(request):
    bike = Bike.objects.all()
    search = request.GET.get('search')
    if search:
        bike = bike.filter(modelo__icontains=search)
    return render(request, 'produtos.html', {'produtos': bike})

# atualiza produto:
def atualizado_produtos(request, pk):
    bike = get_object_or_404(Bike, pk=pk)
    print(request.POST)
    if request.method == 'POST':
        form = BikeModelForm(request.POST, instance=bike)
        if form.is_valid():
            form.save()
            return redirect('pagina-produtos')
    else:
        form = BikeModelForm(instance=bike)
    return render(request, 'cadastra_produtos_atualizar.html', {'form': form, 'bike': bike})

# deleta produto:
def deleta_produto(request, id):
    deleta_produtos = get_object_or_404(Bike, pk=id)
    print(deleta_produtos)
    deleta_produtos.delete()
    return redirect('pagina-produtos')

# contado:
def contados(request):
    if request.method == "POST":
        contados_form = ContadosModelForm(request.POST, request.FILES)
        if contados_form.is_valid():
            contados_form.save()
            return redirect('pagina-enviado')
    else:
        contados_form = ContadosModelForm()
    return render(request, 'contados.html', {'contados': contados_form})

# enviado com sucesso do contado:
def enviado(request):
    contados = Contados.objects.all()
    return render(request, 'enviado.html', {'contados': contados})

# cadastra loja:
@login_required
def cadastra_loja(request):
    if request.method == 'POST':
        lojas_form = LojasModelForm(request.POST, request.FILES)
        if lojas_form.is_valid():
            lojas_form.save()
            return redirect('pagina-loja')
    else:
        lojas_form = LojasModelForm()
    return render(request, 'cadastra_lojas.html', {'lojas_form': lojas_form})

# recebe as informação para html:
def lojas(request):
    lojas = Lojas.objects.all()
    search = request.GET.get('search')
    if search:
        lojas = lojas.filter(modelo__icontains=search)
    return render(request, 'lojas.html', {'lojas': lojas})

# atualiza loja:
def atualizado_lojas(request, id):
    bike = get_object_or_404(Bike, id=id)

    if request.method == 'POST':
        modelo = request.POST.get('modelo')
        preco = request.POST.get('preco')
        descricao = request.POST.get('descricao')
        foto = request.POST.get('foto')

        if len(modelo) > 0:
            bike.modelo = modelo
        if len(preco) > 0:
            bike.preco = preco
        if len(descricao) > 0:
            bike.descricao = descricao
        if len(foto) > 0:
            bike.foto = foto
        bike.save()
        return redirect('pagina-loja')
    return render(request, 'cadastra_lojas.html', {'bike': bike})

# deleta loja:
def deleta_lojas(request, id):
    deleta_lojas = get_object_or_404(Lojas, id=id)
    deleta_lojas.delete()
    return redirect('pagina-loja')

#cadstra vendedor:
@login_required
def cadastra_pessoas(request):
    if request.method == 'POST':
        pessoas = PessoasModelForm(request.POST, request.FILES)
        if pessoas.is_valid():
            pessoas.save()
            return redirect('pagina-vendedores')
    else:
        pessoas = PessoasModelForm()
    return render(request, 'pessoas.html', {'pessoas': pessoas})
    
# recebe as informação para html:
def vendedores(request):
    informacao_pessoas = Pessoas.objects.all()
    return render(request, 'vendedores.html', {'vendedores': informacao_pessoas})

#atualiza vendedor:
def atualiza_pessoas(request, id):
    pessoas_atualiza = get_object_or_404(Pessoas, id=id)

    if request.method == 'POST':
        nome = request.POST.get('nome')
        cpf = request.POST.get('cpf')
        opcao_lojas = request.POST.get('opcao_lojas')

        if len(nome) > 0:
            pessoas_atualiza.nome = nome
        if len(cpf) > 0:
            pessoas_atualiza.cpf = cpf
        if len(opcao_lojas) > 0:
            pessoas_atualiza.opcao_lojas = opcao_lojas
        pessoas_atualiza.save()
        return redirect('pagina-vendedores')
    return render(request, 'pessoas.html', {'vendeodres': pessoas_atualiza})

# deleta vendedor:
def deleta_pessoas(request, id):
    pessoas = get_object_or_404(Pessoas, id=id)
    pessoas.delete()
    return redirect('pagina-vendedores')

# cadastra detalhe:
@login_required
def detalhes_bikes(request):
    if request.method == 'POST':
        detalhe_bike = DetalheModeForm(request.POST, request.FILES)
        if detalhe_bike.is_valid():
            detalhe_bike.save()
            return redirect('pagina-produtos')
    else:
        detalhe_bike = DetalheModeForm()
    return render(request, 'detalhe_bike.html', {'detalhe': detalhe_bike})

# recebe as informação para html:
def detalhe(request):
    detalhe = DetalheBikes.objects.all()
    return render(request, 'pagina-detalhemais.html', {'detalhes': detalhe})

# atualiza detalhe:
def atualiza_detalhe(request, id):
    detalhe_atualiza = get_object_or_404(DetalheBikes, id=id)
    if request.method == 'POST':
        bike = request.POST.get('bike')
        marca = request.POST.get('marca')
        cor = request.POST.get('cor')
        detalhe = request.POST.get('detalhe')

        if len(bike) > 0:
            detalhe_atualiza.bike = bike
        if len(marca) > 0:
            detalhe_atualiza.marca = marca
        if len(cor) > 0:
            detalhe_atualiza.cor = cor
        if len(detalhe) > 0:
            detalhe_atualiza.detalhe = detalhe
        detalhe_atualiza.save()
        return redirect('atualizado-sucesso-detalhe')
    return render(request, 'detalhe_bike.html')

# deleta detalhe:
def deleta_detalhe(request, id):
    detalhe_deleta = get_object_or_404(DetalheBikes, id=id)
    detalhe_deleta.delete()
    return redirect('deleta-sucesso-detalhes')