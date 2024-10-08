from django.contrib import admin
from .models import Titular

class TitularAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cpf', 'email', 'telefone', 'criado_em', 'usuario')
    search_fields = ('nome', 'cpf', 'email')

    def save_model(self, request, obj, form, change):
        if not change:
            obj.usuario = request.user
        super().save_model(request, obj, form, change)
        
admin.site.register(Titular, TitularAdmin)
