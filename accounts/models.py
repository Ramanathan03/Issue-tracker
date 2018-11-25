from django.db import models

# Create your models here.
class bio(models.Model):
        image = models.ImageField(upload_to="img",blank=True, null=True)
        