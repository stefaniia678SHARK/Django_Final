from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from .models import Events
def index(request):
	event = Events.objects.all()
	return render(request, 'index.html', {'event': Events})