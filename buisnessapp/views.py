from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from .models import Events
def index(request):
	event = Events.objects.all()
	return render(request, 'index.html', {'event': Events})
def header (request):
	return render(request, 'header.html')

def events(request):
	event = Events.objects.all()
	return render(request, 'events.html', {'event': Events})

def work_orders(request):
	work_order = work_orders.objects.all()
	return render(request, 'work_orders.html', {'work_order': work_orders})