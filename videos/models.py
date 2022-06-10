from django.db import models
from embed_video.fields import EmbedVideoField
# Create your models here.
class Alumni_Video(models.Model):
    title = models.TextField()
    description = models.TextField()
    added = models.DateTimeField(auto_now_add=True)
    url = EmbedVideoField()

    def __str__(self):
        return(self.title)

class Apptitude_Video(models.Model):
    title = models.TextField()
    description = models.TextField(blank=True)
    added = models.DateTimeField(auto_now_add=True)
    url = EmbedVideoField()
    companyName = models.CharField(max_length=20)
    def __str__(self):
        return(self.title)

class Interview_Corner(models.Model):
    title = models.TextField()
    description = models.TextField(blank=True)
    companyName = models.CharField(max_length=20)
    added = models.DateTimeField(auto_now_add=True)
    url = EmbedVideoField()

    def __str__(self):
        return(self.title)
