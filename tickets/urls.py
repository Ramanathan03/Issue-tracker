from django.conf.urls import url, include
from tickets.views import add_tickets , show_tickets, confrim

urlpatterns = [
    url(r'^add_tickets/$',add_tickets, name='add_tickets'),
    url(r'^confrim/$',confrim, name='confrim'),
    url(r'^(?P<pk>\d+)/$',show_tickets, name='show_tickets'),
    
    
    
    ]