from django.forms import ModelForm
from .models import Events, Work_Order


class EventsForm(ModelForm):

    class Meta:
        model = Events
        fields = '__all__'

#that's a form for allowing users to make work_orders

class WorkForm(ModelForm):
    class Meta:
        model = Work_Order
        fields = '__all__'