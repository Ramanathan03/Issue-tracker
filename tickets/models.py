from django.db import models

# Create your models here.

priority = ('High','Low')


class add_tickets(models.Model):
    title = models.CharField()
    priority= models.CharField(label="Priority",choices='', required=False)