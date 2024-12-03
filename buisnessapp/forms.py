from django.forms import ModelForm
from .models import Events, Work_Order

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#--- For Authentication ---#

from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput

from django import forms


class CreateUserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class LoginForm(AuthenticationForm):

    username = forms.CharField(widget= TextInput())
    password = forms.CharField(widget=PasswordInput())


class EventsForm(ModelForm):

    class Meta:
        model = Events
        fields = '__all__'

# --- that's a form for allowing users to make work_orders --- #

class WorkForm(ModelForm):
    class Meta:
        model = Work_Order
        fields = '__all__'