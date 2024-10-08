from django.contrib import admin
from .models import Titular, Convidado, Evento, Participacao

from .form import ParticipacaoForm

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
    list_display = ('foto_com_icone','nome', 'cpf', 'email', 'telefone', 'criado_em', 'titular', 'checkin_realizado', 'entrada_confirmada', 'usuario')
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



#-----------------------Participacao-------------------------------

#Foi criado um form para atender este codigo:

class ParticipacaoAdmin(admin.ModelAdmin):
    list_display = ('titular', 'evento', 'pagamento_confirmado', 'checkin_realizado', 'entrada_confirmada')
    search_fields = ('titular__nome', 'evento__nome')
    list_filter = ('pagamento_confirmado', 'checkin_realizado', 'entrada_confirmada')
    form = ParticipacaoForm  # Use o formulário personalizado

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        # Filtra os convidados com base no titular selecionado
        if db_field.name == "convidados":
            if request.POST:
                if 'titular' in request.POST:
                    titular_id = request.POST['titular']
                    kwargs["queryset"] = Convidado.objects.filter(titular_id=titular_id)
            elif request.GET:
                if 'titular' in request.GET:
                    titular_id = request.GET['titular']
                    kwargs["queryset"] = Convidado.objects.filter(titular_id=titular_id)

        return super().formfield_for_manytomany(db_field, request, **kwargs)

# Registro do ModelAdmin
admin.site.register(Participacao, ParticipacaoAdmin)