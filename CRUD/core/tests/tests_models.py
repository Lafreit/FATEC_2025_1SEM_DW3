from django.test import TestCase
from core.models import Cliente

class ClienteModelTest(TestCase):
    def setUp(self):
        self.cliente = Cliente.objects.create(
            nome="João Silva",
            cpf="123.456.789-09",
            cnpj="12.345.678/0001-95",
            endereco="Rua das Flores, 123",
            cep="12345-678",
            telefone="(11) 99999-9999",
            email="joao@fatec.sp.gov.br"
        )

    def test_cliente_criado_com_sucesso(self):
        self.assertTrue(Cliente.objects.exists())

    def test_str_retorna_nome(self):
        cliente = Cliente.objects.first()
        self.assertEqual(str(cliente), "João Silva")

    def test_campos_obrigatorios(self):
        cliente = Cliente.objects.first()
        self.assertEqual(cliente.nome, "João Silva")
        self.assertEqual(cliente.cpf, "123.456.789-09")
        self.assertEqual(cliente.cnpj, "12.345.678/0001-95")
        self.assertEqual(cliente.endereco, "Rua das Flores, 123")
        self.assertEqual(cliente.cep, "12345-678")
        self.assertEqual(cliente.telefone, "(11) 99999-9999")
        self.assertEqual(cliente.email, "joao@fatec.sp.gov.br")

    def test_campos_cpf_e_cnpj_podem_ser_nulos(self):
        cliente = Cliente.objects.create(
            nome="Maria Souza",
            cpf=None,
            cnpj=None,
            endereco="Av. Central, 1000",
            cep="87654-321",
            telefone="(11) 98888-8888",
            email="maria@fatec.sp.gov.br"
        )
        self.assertIsNone(cliente.cpf)
        self.assertIsNone(cliente.cnpj)
