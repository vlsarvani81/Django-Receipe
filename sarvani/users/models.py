from django.db import models

# Create your models here.
class Users(models.Model):
    email= models.EmailField(max_length=300)
    password = models.CharField(max_length=30)

class Person(models.Model):
    first_name = models.CharField(max_length=70)
    last_name = models.CharField(max_length=70)