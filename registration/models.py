from django.db import models

class User(models.Model):

    username = models.CharField(max_length=20)
    password = models.CharField(max_length=200)

    def __str__(self):
        return self.username




