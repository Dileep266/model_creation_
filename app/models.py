from django.db import models

# Create your models here.

class State(models.Model):
    sname=models.CharField(max_length=100,primary_key=True)
    cm=models.CharField(max_length=100)

    def __str__(self):
        return self.sname

class Capital(models.Model):
    sname=models.OneToOneField(State,on_delete=models.CASCADE)
    capname=models.CharField(max_length=100,default='amaravathi')
    govt=models.CharField(max_length=100)

    def __str__(self):
        return self.capname
