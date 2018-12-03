from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class bio(models.Model):
        user = models.OneToOneField(User)
        image = models.ImageField(upload_to ="img",blank=True, null=True)
        location = models.CharField(blank=True, null=True, max_length=50)
        
        def __unicode__(self):
            return self.location
        