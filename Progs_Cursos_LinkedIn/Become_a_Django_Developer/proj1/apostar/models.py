from django.db import models

from django.contrib.auth.models import User

# Create your models here.
class Aposta(models.Model):
    numero1=models.IntegerField()
    numero2=models.IntegerField()
    numero3=models.IntegerField()
    numero4=models.IntegerField()
    numero5=models.IntegerField()