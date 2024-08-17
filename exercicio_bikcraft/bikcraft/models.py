from django.db import models

class Bike(models.Model):
    modelo = models.CharField(max_length=255, verbose_name='Modelo')
    preco = models.FloatField(verbose_name='Preço')
    descricao = models.TextField(verbose_name='Descrição')
    foto = models.ImageField(upload_to='media/bikcraft/', blank=True, null=True, verbose_name='Foto')

    def __str__(self):
        return self.modelo
    
class Contados(models.Model):
    nome = models.CharField(max_length=255, verbose_name='Nome')
    email = models.CharField(max_length=255, verbose_name='E-mail')
    mensagem = models.TextField(verbose_name='Mensagem')

    def __str__(self):
        return self.email
    
class Lojas(models.Model):
    nome = models.CharField(max_length=30, verbose_name='Nome da Loja')
    produtos = models.ManyToManyField(Bike, verbose_name='Produtos')
    cnpj = models.CharField(max_length=25, verbose_name='CNPJ')
    detalhe = models.TextField(blank=True, null=True, verbose_name='Descrição')

    def __str__(self):
        return self.nome
    
class Pessoas(models.Model):
    nome = models.CharField(max_length=100, verbose_name='Nome')
    cpf  = models.CharField(max_length=11, verbose_name='CPF')
    opcao_lojas = models.ForeignKey(Lojas, on_delete=models.CASCADE, verbose_name='Lojas')

    def __str__(self):
        return self.nome
    
class DetalheBikes(models.Model):
    bike = models.OneToOneField(Bike, on_delete=models.CASCADE, verbose_name='Bike')
    marca = models.CharField(max_length=50, verbose_name='Marca')
    cor = models.CharField(max_length=50, verbose_name='Cor')
    detalhe = models.CharField(max_length=255, verbose_name='Detalhe')

    def __str__(self):
        return self.bike