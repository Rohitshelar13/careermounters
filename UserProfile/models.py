from platform import platform
from django.db import models
# Create your models here.
class userInfo(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.CharField(max_length=30)
    prnNo = models.CharField(max_length=25)
    departmentName = models.CharField(max_length=30)
    year = models.CharField(max_length=20)
    cgpa = models.CharField(max_length=10)
    phno = models.CharField(max_length=15)
    bdate = models.DateField()
    def __str__(self):
        return(self.email + " - " + self.departmentName)