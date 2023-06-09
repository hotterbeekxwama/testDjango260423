from django.conf import settings
from django.db import models
from django.utils import timezone

class Voetbalspelers(models.Model):   
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    naam_voetballer = models.CharField(max_length=200)
    actuele_voetbalclub = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
       self.published_date = timezone.now()
       self.save()