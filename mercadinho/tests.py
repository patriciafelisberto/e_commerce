from django.test import TestCase
from mercadinho.models import Produto, Venda, Mercadoria, CaixaDiario
from datetime import datetime


class ProdutoTestCase(TestCase):
    def setUp(self):
        self.produto = Produto.objects.create(nome="Produto Teste", estoque=10)
        self.venda = Venda.objects.create(data="2022-01-01", valor_compra=50, metodo_pagamento="cartao")
        self.venda.compra_mercadoria.create(material=self.produto, quantidade=5, preco=10)

    def test_excluir_produto_sem_excluir_historico(self):
        # Verifica se o Produto existe antes de ser excluído
        self.assertTrue(Produto.objects.filter(id=self.produto.id).exists())
        # Verifica se o histórico de Vendas existe antes de excluir o Produto
        self.assertTrue(Venda.objects.filter(id=self.venda.id).exists())

        # Exclui o Produto
        self.produto.delete()

        # Verifica se o Produto foi excluído
        self.assertFalse(Produto.objects.filter(id=self.produto.id).exists())
        # Verifica se o histórico de Vendas ainda existe
        self.assertTrue(Venda.objects.filter(id=self.venda.id).exists())


class MyTestCase(TestCase):
    def setUp(self):
        self.produto = Produto.objects.create(nome="Produto Teste", estoque=10)
        self.venda = Venda.objects.create(data=datetime.now().date(), valor_compra=0)
        self.mercadoria = Mercadoria.objects.create(material=self.produto, quantidade=5, preco=10, venda=self.venda)
        self.caixa = CaixaDiario.objects.create(data=datetime.now().date())

    def test_valor_compra_venda(self):
        self.venda.compra_mercadoria.add(self.mercadoria)
        self.assertEqual(self.venda.valor_compra, 50)

    def test_subtotal_mercadoria(self):
        self.assertEqual(self.mercadoria.subtotal, 50)

    def test_estoque_produto(self):
        self.assertEqual(self.produto.estoque, 5)

    def test_valor_diario_caixa(self):
        self.assertEqual(self.caixa.valor_diario, 50)

    def test_erro_estoque_insuficiente(self):
        mercadoria_estoque_insuficiente = Mercadoria(material=self.produto, quantidade=20, preco=10, venda=self.venda)
        with self.assertRaises(ValueError):
            mercadoria_estoque_insuficiente.save()