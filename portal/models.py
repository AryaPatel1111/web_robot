# portal/models.py

from django.db import models
from django.contrib.auth.models import User

class TimeSlot(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    # any other fields

class GameSession(models.Model):
    timeslot = models.OneToOneField(TimeSlot, on_delete=models.CASCADE)
    access_code = models.CharField(max_length=10)  # or however you plan to generate it
    # any other fields
