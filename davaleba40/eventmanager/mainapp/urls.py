from django.urls import path
from . import views


app_name = 'mainapp'

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('add_event/', views.add_event, name='add_event'),
    path('add_attendee/<int:event_id>', views.add_attendee, name='add_attendee'),
    path('event_details/<int:event_id>/', views.event_details, name='event_details'),
    path('remove_attendee/<int:attendee_id>', views.remove_attendee, name='remove_attendee'),
    path('remove_event/<int:event_id>/', views.remove_event, name='remove_event'),
]

