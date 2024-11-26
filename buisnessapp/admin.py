from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Events, Work_Order

admin.site.register(Events)

admin.site.register(Work_Order)