from django.db import models

class Users(models.Model):
    username = models.CharField(max_length=255)
    date = models.CharField(max_length=255)
    time = models.CharField(max_length=255)