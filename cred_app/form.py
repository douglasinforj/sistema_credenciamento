from django import forms
from .models import Participacao, Convidado


class ParticipacaoForm(forms.ModelForm):
    class Meta:
        model = Participacao
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ParticipacaoForm, self).__init__(*args, **kwargs)
        
        # Verifica se o titular foi selecionado
        if 'titular' in self.data:
            try:
                titular_id = int(self.data.get('titular'))
                self.fields['convidados'].queryset = Convidado.objects.filter(titular_id=titular_id)
            except (ValueError, TypeError):
                pass  # Se o titular não for válido, mantenha a queryset vazia
        elif self.instance.pk:
            # Caso já esteja editando uma participação existente
            self.fields['convidados'].queryset = self.instance.titular.convidados.all()
        else:
            self.fields['convidados'].queryset = Convidado.objects.none()
