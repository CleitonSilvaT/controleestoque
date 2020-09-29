from django.contrib import admin
from .models import Estoque
from .models import EstoqueItens

# Register your models here.

# admin.site.register(Estoque)
# admin.site.register(EstoqueItens)

class EstoqueItensInLine(admin.TabularInline):
    model = EstoqueItens
    extra = 0

@admin.register(Estoque)
class EstoqueAdmin(admin.ModelAdmin):
    inlines = (EstoqueItensInLine,)
    list_display = ('__str__', 'nf')
    search_fields = ('nf',)
    list_filter = ('funcionario',)
    date_hierarchy = 'created'