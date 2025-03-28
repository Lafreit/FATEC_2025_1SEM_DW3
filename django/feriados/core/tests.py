from django.test import TestCase

class NatalTest(TestCase):
    def setUp(self):
        self.resp = self.client.get('/')

    def test_200_response(self):
        self.assertEqual(self.resp.status_code, 200)
    
    def test_texto(self):
        self.assertContains(self.resp, 'Natal')
    
    def test_template_natal(self):
        self.assertTemplateUsed(self.resp, 'natal.html')
        self.assertTemplateUsed(self.resp, 'natal2.html')