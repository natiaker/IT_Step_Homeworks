from django.shortcuts import render, redirect, get_object_or_404
from .models import Event
from .forms import RegisterForm, EventForm
from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.db.models import Q


# @login_required(login_url='/login')
def homepage(request):
    query = request.GET.get('event_query')

    if query:
        events = Event.objects.filter(Q(title__icontains=query) | Q(location__icontains=query))
    else:
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
    event = Event.objects.get(pk=event_id)

    return render(request, 'event_details.html', {'event': event})


@login_required(login_url='/login')
def user_profile(request):
    events = Event.objects.filter(participants=request.user.id)
    return render(request, 'user_profile.html', {'events': events})


@login_required(login_url='/login')
def participate(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    event.participants.add(request.user)

    return redirect('main_app:homepage')


def remove_participation(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    if request.user in event.participants.all():
        event.participants.remove(request.user)

    return redirect('main_app:user_profile')


