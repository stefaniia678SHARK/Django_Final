from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import User

class Events (models.Model):
    event_name = models.CharField(max_length=100)
    description = models.CharField(max_length = 200)
    date_of_the_event = models.DateTimeField('date of event')

    #def __str__(self):
    #   return f"Calendar for {self.event_name}: {self.description}"

#class Work_Order_Status (models.Model):
#   work_order = models.ForeignKey('self', on_delete=models.CASCADE)

#class To_Do_List (models.Model):
#   user = models.ForeignKey(User, on_delete=models.CASCADE)
