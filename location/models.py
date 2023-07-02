from django.db import models

# Create your models here.

class Location(models.Model):
    name = models.CharField(max_length = 180)
    latitude = models.CharField(max_length = 180)
    longitude = models.CharField(max_length = 180)

    def __str__(self):
        return self.task
