# Generated by Django 4.1.4 on 2023-01-22 15:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CaixaDiario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField()),
                ('valor_diario', models.DecimalField(decimal_places=2, editable=False, max_digits=10)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('estoque', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Venda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField()),
                ('valor_compra', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10)),
                ('metodo_pagamento', models.CharField(choices=[('cartao_debito', 'Cartão de Débito'), ('cartao_credito', 'Cartão de Crédito'), ('pix', 'Pix')], max_length=20)),
            ],
            options={
                'verbose_name': 'Venda',
                'verbose_name_plural': 'Vendas',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Mercadoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.DecimalField(decimal_places=0, max_digits=5)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=10)),
                ('subtotal', models.DecimalField(decimal_places=2, editable=False, max_digits=10)),
                ('material', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='material_mercadoria', to='mercadinho.produto')),
                ('venda', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='compra_mercadoria', to='mercadinho.venda')),
            ],
            options={
                'verbose_name': 'Produto',
                'verbose_name_plural': 'PRODUTOS',
            },
        ),
    ]