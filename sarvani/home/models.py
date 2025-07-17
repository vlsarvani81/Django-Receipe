from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Student(models.Model):
    #id=models.AutoField() django automatically adds
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    email=models.EmailField()
    address = models.TextField(null=True,blank=True)
    #image=models.ImageField()
    #file=models.FileField()

    def __str__(self) -> str:
        return self.name
    
class Receipe(models.Model):
    user=models.ForeignKey(User, on_delete=models.SET_NULL, null = True, blank = True)
    rn=models.CharField(max_length=100)
    rd=models.TextField()
    ri=models.ImageField(upload_to="receipe")

class Feedback(models.Model):
    name = models.CharField(max_length=100, )
    comment = models.TextField(verbose_name="Your Feedback") 
