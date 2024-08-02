# band/models.py
from django.db import models

class BandMember(models.Model):
    name = models.CharField(max_length=100)
    instrument = models.CharField(max_length=100)
    bio = models.TextField()
    image = models.ImageField(upload_to='band_members/')

    def __str__(self):
        return self.name
