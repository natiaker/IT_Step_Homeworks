from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    img_link = models.URLField()
    description = models.TextField(max_length=500)

