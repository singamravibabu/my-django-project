from django.test import TestCase

# Create your tests here.
class SimpleTestCase(TestCase):
    def test_homepage_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
