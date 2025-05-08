from django.contrib import admin
from core.models import FeriadoModel
from datetime import date


class FeriadoModelAdmin(admin.ModelAdmin):
    list_display = ('nome', 'dia','mes','modificado_em','registrado_este_ano')
    date_hierarchy = 'modificado_em'
    search_fields = ('nome','dia','mes',)
    list_filter = ('modificado_em',)
    
    def registrado_este_ano(self, obj):
        hoje = date.today()
        return obj.modificado_em.month == hoje.month
    
    registrado_este_ano.short_description = "Registrado este mês"
    registrado_este_ano.boolean = True
        

admin.site.register(FeriadoModel, FeriadoModelAdmin)
