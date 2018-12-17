from django.test import TestCase
from .apps import CheckoutConfig
# Create your tests here.

class TestCheckoutApp(TestCase):
    def test_app(self):   
        self.assertEqual("checkout",CheckoutConfig.name)