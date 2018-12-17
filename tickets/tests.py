from django.test import TestCase
from django.shortcuts import render, HttpResponse,redirect,get_object_or_404
from .models import add_tickets_form
from .views import add_tickets
from .forms import ticketsForm
from .apps import TicketsConfig
# Create your tests here.
class TestViews(TestCase):
        
    def test_index(self):
        """
        Test_index to check the home page is occured and to see that index view picking/using right template
        """
        page = self.client.get("/")
        self.assertEqual(page.status_code,200)
        self.assertTemplateUsed(page,"index.html")
    
    def test_cannot_create_an_ticket_with_only_title(self):
        """
        Reason for these test is to check the add issue form cannot be created only with title
        I mean the user have to fill the every single field.
        """
        form = ticketsForm({'title':'Testing'})
        self.assertFalse(form.is_valid())
        
    def test_app(self):  # most obivious test 
        self.assertEqual("tickets",TicketsConfig.name)