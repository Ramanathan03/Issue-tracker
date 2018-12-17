from django.test import TestCase
from django.contrib.auth.models import User
from .apps import AccountsConfig
from .forms import bio_and_image
from .views import profile
# Create your tests here.
class TestAccounts(TestCase):
    def test_app(self):   
        self.assertEqual("accounts",AccountsConfig.name)
        
    def test_image_profile_form_can_be_empty(self):
        image_location_form = bio_and_image({'location':''})
        self.assertTrue(image_location_form.is_valid())
    
    