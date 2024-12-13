from django.forms import ModelForm
from .models import Events, Work_Order, Profile

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#--- For Authentication ---#

from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput

from django import forms


#-- Update a profile picture --#

#class UpdateProfileFrom (forms.ModelForm):

#    profile_picture = forms.ImageField(widget=forms.FileInput(attrs={'class':'form-control-file'}))

#    class Meta:
#        model = Profile
#        fields = ['profile_picture',]


class CreateUserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class LoginForm(AuthenticationForm):

    username = forms.CharField(widget= TextInput())
    password = forms.CharField(widget=PasswordInput())

# --- Update a user ---#

class UpdateUserForm(forms.ModelForm):

    password = None

    class Meta:

        model = User
        fields = ['username', 'email', ]
        exclude = ['password1', 'password2']

#---- Create an event ----#

class EventsForm(ModelForm):

    class Meta:
        model = Events
        fields = ['event_name', 'description', 'date_of_the_event',]
        exclude = ['user',]

# --- that's a form for allowing users to make work_orders --- #

class WorkForm(ModelForm):
    class Meta:
        model = Work_Order
        fields = ['work_name', 'description', 'due_date', 'in_progress',]
