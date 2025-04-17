from django.test import TestCase
from core.models import FeriadoModel
from datetime import datetime

class SemFeriadoTest(TestCase):
    def setUp(self):
        self.resp = self.client.get('/')

    def test_200_response(self):
        self.assertEqual(self.resp.status_code, 200)
    
    def test_texto(self):
        self.assertContains(self.resp, 'Não é feriado')
    
    def test_template(self):
        self.assertTemplateUsed(self.resp, 'feriado.html')
        self.assertTemplateNotUsed(self.resp, 'natal2.html')


class Feriado_TDD_Test(TestCase):
    def setUp(self):
        hoje = datetime.today()
        FeriadoModel.objects.create(nome='Dia do TDD',dia=hoje.day, mes=hoje.month)
        self.resp = self.client.get('/')

    def test_200_response(self):
        self.assertEqual(self.resp.status_code, 200)
    
    def test_texto(self):
        self.assertContains(self.resp, 'Dia do TDD')
    
    def test_template(self):
        self.assertTemplateUsed(self.resp, 'feriado.html')

class FeriadoModelTest(TestCase):
    def setUp(self):
        self.cadastro = FeriadoModel.objects.create(nome="Natal",dia=25,mes=12)
    
    def test_create(self):
        self.assertTrue(FeriadoModel.objects.exists())
    
    def test_name(self):
        feriado_no_banco = FeriadoModel.objects.first()
        self.assertEqual(feriado_no_banco.nome, 'Natal')