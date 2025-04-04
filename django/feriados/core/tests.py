from django.test import TestCase
from core.models import FeriadoModel
from datetime import datetime

class NatalTest(TestCase):
    def setUp(self):
        self.resp = self.client.get('/')

    def test_200_response(self):
        self.assertEqual(self.resp.status_code, 200)
    
    def test_texto(self):
        self.assertContains(self.resp, 'Natal')
    
    def test_template_natal(self):
        self.assertTemplateUsed(self.resp, 'natal.html')
        self.assertTemplateNotUsed(self.resp, 'natal2.html')


class FeriadoModelTest(TestCase):
    def setUp(self):
        self.cadastro = FeriadoModel.objects.create(nome="Natal",dia=25,mes=12)
    
    def test_create(self):
        self.assertTrue(FeriadoModel.objects.exists())
    
    def test_name(self):
        feriado_no_banco = FeriadoModel.objects.first()
        self.assertEquals(feriado_no_banco.nome, 'Natal')