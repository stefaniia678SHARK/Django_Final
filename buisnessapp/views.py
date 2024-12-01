from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.

from django.shortcuts import render
from .models import Events, Work_Order
from .forms import EventsForm, WorkForm

# - Home page, Header
def index(request):
	event = Events.objects.all()
	return render(request, 'index.html', {'event': Events})
def header (request):
	return render(request, 'header.html')


# - EVENTS

def events(request):
	event = Events.objects.all()

	form = EventsForm()

# Creating an event
	if request.method == 'POST':
		form = EventsForm(request.POST)

		if form.is_valid():
			form.save()
			return redirect('events')

	return render(request, 'events.html', {'event': event, 'form': form})

#  -  View created events

def view_events(request):
	view_event = Events.objects.all()

	context = {'view_event': view_event}

	return render(request, 'view_event.html', context = context)


#  -  Update an event

def update_event(request, pk):

	event = Events.objects.get(id=pk)
#updating an instance, specific object that we want to update
	form = EventsForm(instance=event)

	if request.method == 'POST':

		form = EventsForm(request.POST, instance=event)

		if form.is_valid():
			form.save()

			return redirect('view_event')

	return render(request, 'update_event.html', {'event': event, 'form': form})

#  -  Delete an event


def delete_event(request, pk):

	event = Events.objects.get(id=pk)

	if request.method == 'POST':

		event.delete()

		return redirect('view_event')

	context = {'object': event}

	return render(request, 'delete_event.html', context=context)









# - WORK ORDERS

def work_orders(request):
	orders = Work_Order.objects.all()

	form = WorkForm(request.POST or None)

	return render(request, 'work_orders.html', {'orders': orders, 'form': form})



def create_work(request):
	return redirect('work_orders')
