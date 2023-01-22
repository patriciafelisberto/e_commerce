from django.contrib import admin
from .models import Produto, Venda, Mercadoria, CaixaDiario


class MercadoriaAdmin(admin.TabularInline):
    model = Mercadoria
    extra = 1


class ProdutoAdmin(admin.ModelAdmin):
    pass


class CaixaDiarioAdmin(admin.ModelAdmin):
    date_hierarchy = 'data'
    list_filter = ['data', 'valor_diario']
    list_display = ['data', 'valor_diario']


class VendaAdmin(admin.ModelAdmin):
    date_hierarchy = 'data'
    list_filter = ['data', 'valor_compra', 'metodo_pagamento']

    inlines = [MercadoriaAdmin]
    list_display = ['data', 'valor_compra', 'metodo_pagamento']


admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Venda, VendaAdmin)
admin.site.register(CaixaDiario, CaixaDiarioAdmin)