from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import mixins


from .models import Produto, Venda, Mercadoria, CaixaDiario
from .serializers import ProdutoSerializers, VendaSerializers, MercadoriaSerializers, CaixaDiarioSerializers


class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializers

    @action(detail=True, methods=['get'])
    def mercadorias(self, request, pk=None):
        mercadorias = Mercadoria.objects.filter(produto_id=pk)
        serializer = MercadoriaSerializers(mercadorias, many=True)
        return Response(serializer.data)


class VendaViewSet(viewsets.ModelViewSet):
    queryset = Venda.objects.all()
    serializer_class = VendaSerializers

    @action(detail=True, methods=['get'])
    def mercadorias(self, request, pk=None):
        mercadorias = Mercadoria.objects.filter(produto_id=pk)
        serializer = MercadoriaSerializers(mercadorias, many=True)
        return Response(serializer.data)
    

class CaixaDiarioViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = CaixaDiario.objects.all()
    serializer_class = CaixaDiarioSerializers

class MercadoriaViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet
   ):
    queryset = Mercadoria.objects.all()
    serializer_class = MercadoriaSerializers