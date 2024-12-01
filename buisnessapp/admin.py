from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Events, Work_Order, Review

admin.site.register(Events)
class EventsAdmin(admin.ModelAdmin):
    list_display = ('event_name', 'description', 'date_of_the_event')  # Shows these fields in the admin list view
    search_fields = ('event_name',)  # Allows search by event name

admin.site.register(Work_Order)

admin.site.register(Review)
