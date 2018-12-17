from django.test import TestCase
from .apps import SearchConfig
from .views import do_search
# Create your tests here.

class TestSearchApp(TestCase):
    def test_app(self):   
        self.assertEqual("search",SearchConfig.name)
    
    def test_search_view(self):
        search_page = self.client.get("/search/?q")
        self.assertEqual(search_page.status_code,200)
        self.assertTemplateUsed(search_page,"search.html") 
        """
        to check the url is occured and to check the it using right template
        """

