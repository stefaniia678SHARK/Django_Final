from django.shortcuts import render, redirect
from django.http import HttpResponse
from calendar import HTMLCalendar
from datetime import date
# Create your views here.

from django.shortcuts import render
from .models import Events, Work_Order, Profile
from .forms import EventsForm, WorkForm, CreateUserForm, LoginForm, UpdateUserForm

from django.contrib.auth.models import auth, User

#---- For authentication, log in and log out we need to import ----#
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required

from datetime import datetime, timedelta
from django.contrib import messages

# - Home page, Header

def index(request):

	event = Events.objects.all()
	return render(request, 'index.html', {'event': Events})

def header (request):
	return render(request, 'header.html')

# ----- Register/create a user ------#

def register(request):

	form = CreateUserForm()

	if request.method == 'POST':
		form = CreateUserForm(request.POST)

		if form.is_valid():

			current_user = form.save(commit=False)

			user = form.save()

			profile = Profile.objects.create(user=user)

			messages.success(request, "User registration was successful!")

			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password1')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)  # Log in the user
				return redirect('my-login')  # Redirect to dashboard

	#if form.is_valid():
		#	form.save()
		#	return redirect('dashboard')

	return render(request, 'main/register.html', {'form': form})

# ----- Login a user ------#

def my_login(request):

	form = LoginForm()

	if request.method == 'POST':
		form = LoginForm(request, data =request.POST)

		if form.is_valid():

			username = request.POST.get('username')
			password = request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:

				auth.login(request, user)

				return redirect("dashboard")

	return render(request, "main/my-login.html", {'form': form})

# ---- Dashboard -----#

@login_required(login_url='my-login')  #--Protecting our views (log in -> dashboard)  --#
def dashboard(request):

	profile = Profile.objects.get(user=request.user)

	view_event = Events.objects.all()

	return render(request, 'dashboard.html', {'view_event': view_event, 'profile': profile})

# ---- Profile management ----#

@login_required(login_url='my-login')
def profile_management(request):

	if request.method == 'POST':

		user_form = UpdateUserForm(request.POST, instance=request.user)

		if user_form.is_valid():

			user_form.save()

			return redirect ('dashboard')

	user_form = UpdateUserForm(instance=request.user)

	return render(request, 'profile/profile-management.html', {'user_form': user_form})

# ----- Delete an account -----#

@login_required(login_url='my-login')
def deleteaccount(request):

	if request.method == 'POST':

		try:

			deleteUser = User.objects.get(username=request.user.username)  # Fetch the logged-in user
			deleteUser.delete()  # Delete the user

			return redirect('index')

		except User.DoesNotExist:
			messages.error(request, "User does not exist.")

			return redirect('dashboard')

	return render(request, 'profile/delete-account.html')

# ----- Logout a user ------#

def user_logout(request):

	auth.logout(request)

	return redirect("index")

#----- EVENTS ------#

@login_required(login_url='my-login')
def events(request):
	event = Events.objects.all()

	form = EventsForm()

# Creating an event
	if request.method == 'POST':
		form = EventsForm(request.POST)

		if form.is_valid():

			event = form.save(commit=False)
			event.user = request.user #linking a user to an event
			event.save()

			return redirect('dashboard')

	return render(request, 'main/events.html', {'event': event, 'form': form})

#  -  View created events

def view_events(request):

	current_user = request.user.id

	event = Events.objects.all().filter(user=current_user)

	context = {'view_event': event}

	return render(request, 'dashboard.html', context = context)


#  -  Update an event

def update_event(request, pk):

	event = Events.objects.get(id=pk)
#updating an instance, specific object that we want to update
	form = EventsForm(instance=event)

	if request.method == 'POST':

		form = EventsForm(request.POST, instance=event)

		if form.is_valid():
			form.save()

			return redirect('dashboard')

	return render(request, 'profile/update_event.html', {'event': event, 'form': form})

#  -  Delete an event


def delete_event(request, pk):

	event = Events.objects.get(id=pk)

	if request.method == 'POST':

		event.delete()

		return redirect('dashboard')

	context = {'object': event}

	return render(request, 'profile/delete_event.html', context=context)


# - WORK ORDERS

def work_orders(request):
	orders = Work_Order.objects.all()

	form = WorkForm(request.POST or None)

	return render(request, 'main/work_orders.html', {'orders': orders, 'form': form})



def create_work(request):
	return redirect('work_orders')

