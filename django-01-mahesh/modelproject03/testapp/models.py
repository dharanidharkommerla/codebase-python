from django.db import models

# Create your models here.
class Student(models.Model):
    sId = models.IntegerField()
    sName = models.CharField(max_length=70)
    sEmail = models.CharField(max_length=100)
    sMobileNo = models.BigIntegerField()
    sMarks = models.IntegerField()
    sAddress = models.TextField()
