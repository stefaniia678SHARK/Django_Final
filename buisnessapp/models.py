
# Create your models here.

from django.db import models
from django.contrib.auth.models import User

#----- Profile ------#

class Profile(models.Model):

    profile_picture = models.ImageField(null=True, blank=True, default='default.webp')

    user = models.ForeignKey(User, max_length=10, on_delete=models.CASCADE, null=True)

#---- Create an event ------#

class Events (models.Model):

    event_name = models.CharField(max_length=100)
    description = models.CharField(max_length = 200)
    date_of_the_event = models.DateField()
    date_posted = models.DateTimeField(auto_now_add=True, null=True)
    icon = models.ImageField(upload_to='images/', null=True, blank=True)

    user = models.ForeignKey(User, max_length=10, on_delete=models.CASCADE, null=True)

#---- Create Work Order ----#

class Work_Order (models.Model):
   #work_order = models.ForeignKey('self', on_delete=models.CASCADE)pe
   work_name = models.CharField(max_length=100)
   description = models.CharField(max_length=200)
   date_posted = models.DateTimeField(auto_now_add=True)
   due_date = models.DateField()
   in_progress = models.BooleanField(default=False)

   user = models.ForeignKey(User, max_length=10, on_delete=models.CASCADE, null=True)

class Review(models.Model):

    reviewer_name= models.CharField(max_length=100)
    reviewer_title= models.CharField(max_length=200)

    work_orders = models.ForeignKey('Work_Order', on_delete=models.CASCADE)

#class To_Do_List (models.Model):
#   user = models.ForeignKey(User, on_delete=models.CASCADE)
