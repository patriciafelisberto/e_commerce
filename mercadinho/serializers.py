from rest_framework import serializers

from .models import Produto, Venda, Mercadoria, CaixaDiario


class ProdutoSerializers(serializers.ModelSerializer):

    mercadoria = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    
    class Meta: 

        model = Produto
        fields = '__all__'


class VendaSerializers(serializers.ModelSerializer):

 
    mercadoria = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta: 

        model = Venda
        fields = '__all__'


class MercadoriaSerializers(serializers.ModelSerializer):

    class Meta: 

        model = Mercadoria
        fields = '__all__'

class CaixaDiarioSerializers(serializers.ModelSerializer):

    class Meta: 

        model = CaixaDiario
        fields = '__all__'