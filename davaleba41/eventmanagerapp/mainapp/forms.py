from django import forms
from .models import Event
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class RegisterForm(UserCreationForm):

    email = forms.EmailField(required=False)

    class Meta:

        model = User

        fields = ['username', 'email', 'password1', 'password2']


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description', 'date', 'location', 'categories']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Please Input The Title'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Please Input the Description'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Please input the Location'}),
        }


