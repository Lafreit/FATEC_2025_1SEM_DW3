from django import forms
from .models import Cliente
import re

def validar_cpf(cpf):
    cpf = re.sub(r'[^0-9]', '', cpf)
    if len(cpf) != 11 or cpf == cpf[0] * 11:
        raise forms.ValidationError("CPF inválido.")
    for i in range(9, 11):
        soma = sum(int(cpf[num]) * ((i + 1) - num) for num in range(0, i))
        digito = ((soma * 10) % 11) % 10
        if digito != int(cpf[i]):
            raise forms.ValidationError("CPF inválido.")

def validar_cnpj(cnpj):
    cnpj = re.sub(r'[^0-9]', '', cnpj)
    if len(cnpj) != 14 or cnpj == cnpj[0] * 14:
        raise forms.ValidationError("CNPJ inválido.")
    pesos1 = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    pesos2 = [6] + pesos1
    for i in range(12, 14):
        soma = sum(int(cnpj[num]) * pesos2[num] for num in range(0, i))
        digito = 11 - (soma % 11)
        digito = 0 if digito >= 10 else digito
        if digito != int(cnpj[i]):
            raise forms.ValidationError("CNPJ inválido.")

def validar_cep(cep):
    if not re.match(r'^\d{{5}}-\d{{3}}$', cep):
        raise forms.ValidationError("CEP deve estar no formato 00000-000.")

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'

    def clean_email(self):
        email = self.cleaned_data['email']
        if not email.endswith('@fatec.sp.gov.br'):
            raise forms.ValidationError("Use um e-mail institucional (@fatec.sp.gov.br).")
        return email

    def clean_cpf(self):
        cpf = self.cleaned_data.get('cpf')
        if cpf:
            validar_cpf(cpf)
        return cpf

    def clean_cnpj(self):
        cnpj = self.cleaned_data.get('cnpj')
        if cnpj:
            validar_cnpj(cnpj)
        return cnpj

    def clean_cep(self):
        cep = self.cleaned_data.get('cep')
        validar_cep(cep)
        return cep
