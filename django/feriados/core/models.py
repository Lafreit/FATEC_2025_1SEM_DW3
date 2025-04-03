from django.db import models

class FeriadoModel(models.Model):
    nome = models.CharField('Feriado',max_length=50)
    dia = models.IntegerField('Dia')
    mes = models.IntegerField('Mes')
    
    def __str__(self):
        return self.nome
