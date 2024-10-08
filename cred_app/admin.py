from django.contrib import admin
from .models import Titular, Convidado, Evento

from django.utils.html import format_html

class TitularAdmin(admin.ModelAdmin):
    list_display = ('foto_com_icone','nome', 'cpf', 'email', 'telefone', 'criado_em', 'usuario')
    search_fields = ('nome', 'cpf', 'email')
    readonly_fields = ('exibir_foto',)  # Campo somente leitura para ver a foto

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


    #Exibir a foto no formuário de detalhes no admin:

    def exibir_foto(self, obj):
        if obj.foto:
            return format_html('<img src="{}" style="width: 150px; height: 150px;" />', obj.foto.url)
        return "Sem foto"

    exibir_foto.short_description = 'Foto atual'




admin.site.register(Titular, TitularAdmin)



#--------------Convidados------------------------

class ConvidadoAdmin(admin.ModelAdmin):
    list_display = ('foto_com_icone','nome', 'cpf', 'email', 'telefone', 'criado_em', 'titular', 'usuario')
    search_fields = ('nome', 'cpf', 'email', 'titular')
    readonly_fields = ('exibir_foto',)  

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

    #Exibir a foto no formuário de detalhes no admin:

    def exibir_foto(self, obj):
        if obj.foto:
            return format_html('<img src="{}" style="width: 150px; height: 150px;" />', obj.foto.url)
        return "Sem foto"

    exibir_foto.short_description = 'Foto atual'

admin.site.register(Convidado, ConvidadoAdmin)


#----------------------------Eventos----------------------------------


class EventoAdmin(admin.ModelAdmin):
    list_display = ('foto_icone','nome', 'data', 'data_termino', 'local',  'criado_em')
    search_fields = ('nome', 'local')
    readonly_fields = ('exibir_foto',)

    def foto_icone(self, obj):
        if obj.foto:
            return format_html('<img src="{}" style="width: 50px; height: 50px;" />', obj.foto.url)
        return "Sem foto"

    foto_icone.short_description = 'Foto'

    def exibir_foto(self, obj):
        if obj.foto:
            return format_html('<img src="{}" style="width: 300px; height: 300px;" />', obj.foto.url)
        return "Sem foto"

    exibir_foto.short_description = 'Foto do Evento'

admin.site.register(Evento, EventoAdmin)
