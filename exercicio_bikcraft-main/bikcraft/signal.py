from django.db.models.signals import pre_save, post_save, pre_delete, post_delete
from django.db.models import Sum
from django.dispatch import receiver
from .models import Pessoas, Bike, Lojas

def atualiza_inventario_bike():
    numero_de_bike = Bike.objects.all().count()
    valor_total = Bike.objects.aggregate(valor_total=Sum('preco'))['valor_total']

@receiver(pre_save, sender=Pessoas)
def vendedor_pre_save(sender, instance, **kwargs):
    print('### SEU VENDEDOR JÁ ESTÁ NO DB ###')

@receiver(post_save, sender=Pessoas)
def vendedor_post_save(sender, instance, **kwargs):
    print('### SEU VENDEDOR JÁ ESTÁ NO DB ###')

@receiver(pre_save, sender=Bike)
def bike_pre_save(sender, instance, **kwargs):
    print('### SUA BIKE JÁ ESTÁ NO DB ###')
    atualiza_inventario_bike()

@receiver(post_save, sender=Bike)
def bike_post_save(sender, instance, ** kwargs):
    print('### SUA BIKE JÁ ESTÁ NO DB ###')
    atualiza_inventario_bike()

@receiver(pre_save, sender=Lojas)
def lojas_pre_save(sender, instance, **kwargs):
    print('### SUA LOJA JÁ ESTÁ NO DB ###')

@receiver(post_save, sender=Lojas)
def lojas_post_save(sender, instance, **kwargs):
    print('### SUA LOJA JÁ ESTÁ NO DB ###')

@receiver(pre_delete, sender=Pessoas)
def pessoa_pre_delete(sender, instance, **kwargs):
    print('### SEU VENDEDOR JÁ ESTÁ DELETADO NO DB ###')

@receiver(post_delete, sender=Pessoas)
def pessoa_post_delete(sender, instance, **kwargs):
    print('### SEU VENDEDOR JÁ ESTÁ DELETADO NO DB ###')

@receiver(pre_delete, sender=Bike)
def bike_pre_delete(sender, instance, **kwargs):
    print('### SUA BIKE JÁ ESTÁ DELETADO NO DB ###')
    atualiza_inventario_bike()

@receiver(post_delete, sender=Bike)
def bike_post_delete(sender, instance, **kwargs):
    print('### SUA BIKE JÁ ESTÁ DELETADO DO DB ###')

@receiver(pre_delete, sender=Lojas)
def loja_pre_delete(sender, instance, **kwargs):
    print('### SUA LOJA JÁ ESTÁ DELETADO NO DB ###')

@receiver(post_delete, sender=Lojas)
def loja_post_delete(sender, isntance, **kwargs):
    print('### SUA LOJA JÁ ESTÁ DELETADO NO DB ###')
