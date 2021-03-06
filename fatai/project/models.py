from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# django admin username = admin
# django admin password = fatai12345
# Create your models here.

STATUS = (
    (0, "NIL"),
    (1, "Delivered")
)

class Track(models.Model):
    tracking_number = models.CharField(max_length=150, unique=True, primary_key=True)
    slug = models.SlugField(max_length=100)
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    receiver = models.CharField(max_length=300)
    signed_for_by = models.CharField(max_length=300)
    date = models.DateField()
    time = models.TimeField(auto_now_add=True)
    location = models.CharField(max_length=100, blank=False)
    destination = models.CharField(max_length=100, blank=False)
    status = models.IntegerField(choices=STATUS, default=1)

    class Meta:
        ordering = ['-time']

    def get_absolute_url(self):
        return reverse('project:detail', kwargs={'slug': self.slug})

    def __str__(self):
        return self.tracking_number
    