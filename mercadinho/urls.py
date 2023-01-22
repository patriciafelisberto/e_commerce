from django.urls import path

from rest_framework.routers import SimpleRouter

from .views import VendaViewSet, ProdutoViewSet, CaixaDiarioViewSet


router = SimpleRouter()
router.register('produtos', ProdutoViewSet)
router.register('vendas', VendaViewSet)
router.register('caixadiario', CaixaDiarioViewSet)