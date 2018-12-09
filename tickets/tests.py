from django.test import TestCase
from django.shortcuts import render, HttpResponse,redirect,get_object_or_404
from .models import add_tickets_form
from .views import add_tickets
from .forms import ticketsForm
from .apps import TicketsConfig
# Create your tests here.
class TestViews(TestCase):
        
    def test_index(self):
        page = self.client.get("/")
        self.assertEqual(page.status_code,200)
        self.assertTemplateUsed(page,"index.html")
    
    def test_cannot_create_an_ticket_with_only_title(self):
        form = ticketsForm({'title':'Testing'})
        self.assertFalse(form.is_valid())
        
    def test_app(self):
        self.assertEqual("tickets",TicketsConfig.name)