from django.db import models
from .constants.metodosPagamento import METODOS_PAGAMENTO


class Produto(models.Model):
    nome = models.CharField(max_length=255)
    estoque = models.IntegerField()


    def __str__(self):
        return self.nome


class Venda(models.Model):
    data = models.DateField()
    valor_compra = models.DecimalField(max_digits=10, decimal_places=2, blank=True, default=0)
    metodo_pagamento = models.CharField(max_length=20, choices=METODOS_PAGAMENTO)


    def __str__(self):
        return f' Compra Nº{self.id}'

    class Meta:
        ordering = ['id']
        verbose_name = u'Venda'
        verbose_name_plural = u'Vendas'
    

class Mercadoria(models.Model):
    material = models.ForeignKey(Produto, on_delete=models.SET_NULL, related_name='material_mercadoria', null=True)
    quantidade = models.DecimalField(max_digits=5,decimal_places=0)
    preco = models.DecimalField(max_digits=10,decimal_places=2)
    venda = models.ForeignKey(Venda, on_delete=models.CASCADE, related_name='compra_mercadoria')
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, editable=False)
    

    def __str__(self):
        if self.material:
            return self.material.nome + ",R$" + str(self.preco) +"," + str(self.quantidade) + ",R$" + str(self.subtotal)
        else:
            return "Produto removido"

    class Meta:
        verbose_name = u'Produto'
        verbose_name_plural = u'PRODUTOS'

  
    def save(self, *args, **kwargs):
        self.subtotal = self.preco * self.quantidade
        if self.quantidade > self.material.estoque:
            raise ValueError(f'O Produto {self.material} não possui estoque suficiente!!!')
        else:
            self.material.estoque -= self.quantidade
            self.material.save()
            self.venda.valor_compra += self.subtotal
            self.venda.save()
            super(Mercadoria, self).save(*args, **kwargs)
    
    
class CaixaDiario(models.Model):
    data = models.DateField()
    valor_diario = models.DecimalField(max_digits=10, decimal_places=2, editable=False)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.data.strftime('%d/%m/%Y') + ",R$" + str(self.valor_diario)

    def save(self, *args, **kwargs):
        vendas_do_dia = Venda.objects.filter(data=self.data)
        valor_total = sum(venda.valor_compra for venda in vendas_do_dia)
        self.valor_diario = valor_total
        super(CaixaDiario, self).save(*args, **kwargs)