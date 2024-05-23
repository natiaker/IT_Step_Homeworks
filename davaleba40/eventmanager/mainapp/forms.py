
from django import forms
from .models import Event, Attendee


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


class AttendeeForm(forms.ModelForm):
    class Meta:
        model = Attendee
        fields = ['name', 'email', 'event']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'JohnDoe@example.com'}),
            'event': forms.Select(attrs={'class': 'form-control'})
        }
