from django import forms

class FeriadoForm(forms.Form):
    nome = forms.CharField(label="Nome do Feriado", max_length=50)
    dia = forms.IntegerField(label="Dia", min_value=1, max_value=31)
    mes = forms.IntegerField(label="Mês", min_value=1, max_value=12)
    
    def clean_nome(self):
        nome = self.cleaned_data['nome']
        return nome.upper()