from django.db import models

# Create your models here.
class Opportunity(models.Model):
    companyName = models.CharField(max_length=50)
    companydescription = models.TextField()
    perks = models.TextField(blank=True)
    googleformlink = models.CharField(max_length=255,blank=True)
    companywebsite = models.CharField(max_length=255,blank=True)
    companyemail = models.CharField(max_length=255,blank=True)

    def __str__(self):
        return self.companyName