from django.shortcuts import render, redirect
from .models import Event, Attendee
from .forms import EventForm, AttendeeForm
from django.db.models import Q


def home_page(request):
    query = request.GET.get('event_query')

    if query:
        events = Event.objects.filter(Q(title__icontains=query) | Q(location__icontains=query))
    else:
        events = Event.objects.all()

    return render(request, 'index.html', {'events': events})


def add_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mainapp:home_page')

    else:
        form = EventForm()
        return render(request, 'add_event.html', {'form': form})


def add_attendee(request, event_id):
    event = Event.objects.get(pk=event_id)

    if request.method == 'POST':
        form = AttendeeForm(request.POST, initial={'event': event_id})
        if form.is_valid():
            form.save()
            return redirect('mainapp:home_page')

    else:
        form = AttendeeForm(initial={'event': event_id})
        return render(request, 'add_attendee.html', {'form': form, 'event': event})


def event_details(request, event_id):
    event = Event.objects.get(pk=event_id)
    attendees = Attendee.objects.filter(event_id=event_id)

    return render(request, 'event_details.html', {'event': event, 'attendees': attendees})


def remove_attendee(request, attendee_id):
    attandee_to_remove = Attendee.objects.get(pk=attendee_id)
    event_id = attandee_to_remove.event.id
    attandee_to_remove.delete()

    return redirect('mainapp:event_details', event_id)


def remove_event(request, event_id):
    event_to_remove = Event.objects.get(pk=event_id)
    event_to_remove.delete()

    return redirect('mainapp:home_page')

