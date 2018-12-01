from django.db import models

# Create your models here.
class bio(models.Model):
        image = models.ImageField(upload_to ="img",blank=True, null=True)
        location = models.CharField(blank=True, null=True, max_length=50)
        
        def __unicode__(self):
            return self.location
        