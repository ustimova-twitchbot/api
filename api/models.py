from urllib import response
from django.db import models
from django.utils import timezone
import requests

class User(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Channel(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Comment(models.Model):
    text = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    channel = models.ForeignKey(Channel, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.text

    

