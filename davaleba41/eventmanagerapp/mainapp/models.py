from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):

    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'category'


class Event(models.Model):

    title = models.CharField(max_length=40)
    img_address = models.URLField(default="https://1000logos.net/wp-content/uploads/2020/02/The-Doors-Logo.jpg")
    description = models.TextField()
    date = models.DateField()
    location = models.CharField(max_length=50)
    categories = models.ManyToManyField(Category)
    participants = models.ManyToManyField(User, related_name='events_participants')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'event'


