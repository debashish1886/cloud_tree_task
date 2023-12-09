from django.db import models

class StudentModels(models.Model):
    idno=models.IntegerField(primary_key=True)
    fname=models.CharField(max_length=20)
    lname=models.CharField(max_length=10)
    age=models.IntegerField()
    email=models.EmailField()

