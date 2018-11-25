from django.conf.urls import url, include
from tickets.views import add_tickets

urlpatterns = [
    url(r'^add_tickets/$',add_tickets, name='add_tickets'),
    ]