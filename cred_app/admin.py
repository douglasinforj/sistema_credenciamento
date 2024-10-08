from django.contrib import admin
from .models import Titular, Convidado

from django.utils.html import format_html

class TitularAdmin(admin.ModelAdmin):
    list_display = ('foto_com_icone','nome', 'cpf', 'email', 'telefone', 'criado_em', 'usuario')
    search_fields = ('nome', 'cpf', 'email')

    def save_model(self, request, obj, form, change):
        if not change:
            obj.usuario = request.user
        super().save_model(request, obj, form, change)

    #Apresentar a foto como miniatura no admin
    def foto_com_icone(self, obj):
        if obj.foto:
            return format_html(
                '<img src="{}" style="width: 50px; height: 50px; border-radius: 50%;" /> <span class="dashicons dashicons-format-image" style="font-size: 20px;"></span>',
                obj.foto.url  # busca a url da foto
            )
        return "Sem foto"  # se não conter a foto

    foto_com_icone.short_description = 'Foto'  # descrição da foto no admin


admin.site.register(Titular, TitularAdmin)



#--------------Convidados------------------------

class ConvidadoAdmin(admin.ModelAdmin):
    list_display = ('foto_com_icone','nome', 'cpf', 'email', 'telefone', 'criado_em', 'titular', 'usuario')
    search_fields = ('nome', 'cpf', 'email', 'titular')

    def save_model(self, request, obj, form, change):
        if not change:
            obj.usuario = request.user
        super().save_model(request, obj, form, change)

    #Apresentar a foto como miniatura no admin
    def foto_com_icone(self, obj):
        if obj.foto:
            return format_html(
                '<img src="{}" style="width: 50px; height: 50px; border-radius: 50%;" /> <span class="dashicons dashicons-format-image" style="font-size: 20px;"></span>',
                obj.foto.url  # busca a url da foto
            )
        return "Sem foto"  # se não conter a foto

    foto_com_icone.short_description = 'Foto'  # descrição da foto no admin

admin.site.register(Convidado, ConvidadoAdmin)