from django.shortcuts import render, redirect
from .models import Event
from .forms import RegisterForm, EventForm
from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required


# @login_required(login_url='/login')
def homepage(request):
    events = Event.objects.all()
    return render(request, 'index.html', {'events': events})


def sign_up(request):

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('main_app:homepage')
        else:
            return render(request, 'registration/sign_up.html', {'form': form})

    else:
        form = RegisterForm()
        return render(request, 'registration/sign_up.html', {'form': form})


def logout_user(request):
    logout(request)
    return redirect('main_app:homepage')


def add_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)

        if form.is_valid():
            event = form.save()
            return redirect('main_app:homepage')
    else:
        form = EventForm()
        return render(request, 'add_event.html', {'form': form})


def remove_event(request, event_id):
    event_to_remove = Event.objects.get(id=event_id)
    event_to_remove.delete()

    return redirect('main_app:homepage')


def event_details(request, event_id):
    event = Event.objects.get(id=event_id)

    return render(request, 'event_details.html', {'event': event})


def participate(request, event_id):
    pass

