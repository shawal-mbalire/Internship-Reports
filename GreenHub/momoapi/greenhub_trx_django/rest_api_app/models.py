from django.db import models
from django.contrib.auth.models import AbstractBaseUser

# Create your models here.
class MyUser(AbstractBaseUser):
    
    phone_num = models.IntegerField(primary_key=True)
    first_name= models.CharField(max_length = 225)
    last_name = models.CharField(max_length = 225)
    email     = models.EmailField(max_length=254)
    password  = models.CharField(max_length = 225)



class Transfer(models.Model):
    STATUS_CHOICES = {
        0 : "Not yet attempted",
        1 : "In the process",
        2 : "Completed Succesfully",
        3 : "tried but failed keep trying",
        4 : "tried x times and failed"
    }
    user_num = models.ForeignKey(MyUser, on_delete = models.CASCADE)
    description= models.TimeField()
    amount = models.IntegerField()
    date = models.DateTimeField(auto_now=False, auto_now_add=True)
    status= models.IntegerField(choices = STATUS_CHOICES)



class Collection(models.Model):
    STATUS_CHOICES = {
        0 : "Not yet attempted",
        1 : "In the process",
        2 : "Completed Succesfully",
        3 : "tried but failed keep trying",
        4 : "tried x times and failed"
    }
    user_num = models.ForeignKey(MyUser, on_delete = models.CASCADE)
    description= models.TimeField()
    amount = models.IntegerField()
    date = models.DateTimeField(auto_now=False, auto_now_add=True)
    status= models.IntegerField(choices = STATUS_CHOICES)