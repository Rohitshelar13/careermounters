from django.db import models

# Create your models here.
class CS_IT_Course(models.Model):
    sno = models.AutoField(primary_key=True)
    courseName = models.TextField()
    source = models.CharField(max_length=50)
    duration = models.CharField(max_length=20)
    cat = (
        ('Free','Free'),
        ('Paid','Paid'),
    )
    category = models.CharField(max_length=10,choices=cat,default='Free')
    timeStamp = models.DateTimeField(auto_now_add = True, blank=True)
    courseLink = models.TextField()
    def __str__(self):
        return self.source + '-' + self.courseName

class Entc_Course(models.Model):
    sno = models.AutoField(primary_key=True)
    courseName = models.CharField(max_length=200)
    source = models.CharField(max_length=50)
    duration = models.CharField(max_length=20)
    cat = (
        ('Free','Free'),
        ('Paid','Paid'),
    )
    category = models.CharField(max_length=10,choices=cat,default='Free')
    timeStamp = models.DateTimeField(auto_now_add = True, blank=True)
    courseLink = models.TextField()
    def __str__(self):
        return self.source + '-' + self.courseName

class Electrical_Course(models.Model):
    sno = models.AutoField(primary_key=True)
    courseName = models.CharField(max_length=200)
    source = models.CharField(max_length=50)
    duration = models.CharField(max_length=20)
    cat = (
        ('Free','Free'),
        ('Paid','Paid'),
    )
    category = models.CharField(max_length=10,choices=cat,default='Free')
    timeStamp = models.DateTimeField(auto_now_add = True, blank=True)
    courseLink = models.TextField()
    def __str__(self):
        return self.source + '-' + self.courseName

class Mechanical_Course(models.Model):
    sno = models.AutoField(primary_key=True)
    courseName = models.CharField(max_length=200)
    source = models.CharField(max_length=50)
    duration = models.CharField(max_length=20)
    cat = (
        ('Free','Free'),
        ('Paid','Paid'),
    )
    category = models.CharField(max_length=10,choices=cat,default='Free')
    timeStamp = models.DateTimeField(auto_now_add = True, blank=True)
    courseLink = models.TextField()
    def __str__(self):
        return self.source + '-' + self.courseName

class Civil_Course(models.Model):
    sno = models.AutoField(primary_key=True)
    courseName = models.CharField(max_length=200)
    source = models.CharField(max_length=50)
    duration = models.CharField(max_length=20)
    cat = (
        ('Free','Free'),
        ('Paid','Paid'),
    )
    category = models.CharField(max_length=10,choices=cat,default='Free')
    timeStamp = models.DateTimeField(auto_now_add = True, blank=True)
    courseLink = models.TextField()
    def __str__(self):
        return self.source + '-' + self.courseName

class Trending_Course(models.Model):
    sno = models.AutoField(primary_key=True)
    courseName = models.CharField(max_length=200)
    source = models.CharField(max_length=50)
    duration = models.CharField(max_length=20)
    cat = (
        ('Free','Free'),
        ('Paid','Paid'),
    )
    category = models.CharField(max_length=10,choices=cat,default='Free')
    timeStamp = models.DateTimeField(auto_now_add = True, blank=True)
    courseLink = models.TextField()
    def __str__(self):
        return self.source + '-' + self.courseName