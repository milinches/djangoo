from django.db import models
from django.contrib.auth.models import User

# Create your models here.

STATUS = (
    (0, "Sold"),
    (1, "Remaining")
)

class Track(models.Model):
    tracking_number = models.CharField(max_length=150, unique=True, primary_key=True)
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    receiver = models.CharField(max_length=300)
    signed_for_by = models.CharField(max_length=300)
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)