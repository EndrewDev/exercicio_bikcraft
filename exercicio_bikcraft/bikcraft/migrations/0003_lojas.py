# Generated by Django 5.0.6 on 2024-06-13 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bikcraft', '0002_alter_bike_descricao_alter_bike_foto_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lojas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30, verbose_name='Nome')),
                ('cnpj', models.CharField(max_length=25, verbose_name='CNPJ')),
                ('detalhe', models.TextField(blank=True, null=True, verbose_name='Descrição')),
                ('produtos', models.ManyToManyField(to='bikcraft.bike', verbose_name='Produtos')),
            ],
        ),
    ]
