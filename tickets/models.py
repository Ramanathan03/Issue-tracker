from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib import messages, auth
from datetime import datetime, timedelta
# Create your models here.

BUG = 'Bug'
FEATURE = 'FEATURE'
priority = (('HIGH','High'),('LOW','Low'))
types = (
  (BUG,'Bug'),
    (FEATURE,'feature')
    )
    
NEW = 'New'
UNDER_REVIEW = 'Under_review'
DECLINED = 'Declined'
NEEDS_MORE_INFO = 'Needs_more_info'
PLANNED = 'Planned'
IN_PROGRESS = 'In_Progress'
COMPLETED = 'Completed'
STATUS_CHOICES = (
        (NEW, 'new'),
        (UNDER_REVIEW, 'under-review'),
        (DECLINED, 'declined'),
        (NEEDS_MORE_INFO, 'needs-more-info'),
        (PLANNED, 'planned'),
        (IN_PROGRESS, 'in-progress'),
        (COMPLETED, 'completed'), )
def one_day_hence():
    return timezone.now() + timezone.timedelta(days=30 , minutes=60 , hours=24)
class add_tickets_form(models.Model):
    title = models.CharField(max_length=250,blank=False)
    description = models.TextField()
    priority= models.CharField(max_length=15,choices=priority, default='Low')
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default=NEW)
    type = models.CharField(max_length=20,choices=types,default='Bug')
    views = models.IntegerField(default=0)
    date_create = models.DateTimeField(blank=True, null=True, default=timezone.now)
    last_seen = models.DateTimeField(blank=False, default=one_day_hence )
    author =models.ForeignKey(User, default='', on_delete=models.CASCADE)

    def __str__(self):
        return  "{0}-{1}-{2}".format(self.title,self.description,self.author)
        
class Comment_form(models.Model):
    user =models.ForeignKey(User, default='',  on_delete=models.CASCADE)
    ticket = models.ForeignKey(add_tickets_form, default='', on_delete=models.CASCADE,  related_name='comments')
    comment = models.TextField()
    comment_created = models.DateTimeField(blank=True, null=True, default=timezone.now)
    
    def __str__(self):
        return "{0} created by {1}".format(self.comment,self.user)


    




    