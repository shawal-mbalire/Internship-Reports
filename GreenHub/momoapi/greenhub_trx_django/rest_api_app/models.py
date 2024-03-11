from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from psqlextra.types import PostgresPartitioningMethod
from psqlextra.models import PostgresPartitionedModel
# from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class MyUser(AbstractBaseUser):
    
    phone_num = models.IntegerField(primary_key=True)
    first_name= models.CharField(max_length = 225)
    last_name = models.CharField(max_length = 225)
    email     = models.EmailField(max_length=254)
    password  = models.CharField(max_length = 225)



class Transfer(PostgresPartitionedModel):
    class PartitioningMeta:
        method = PostgresPartitioningMethod.RANGE
        key = ['date']
    STATUS_CHOICES = [
        (0 , 'Not yet attempted'),
        (1 , 'In the process'),
        (2 , 'Successfully completed'),
        (3 , 'Tried but failed'),
        (4 , 'Tried X times and failed.')
    ]
    user_num = models.ForeignKey(MyUser, on_delete = models.CASCADE)
    description= models.TimeField()
    amount = models.IntegerField()
    date = models.DateTimeField(auto_now=False, auto_now_add=True)
    status= models.IntegerField(choices=STATUS_CHOICES)



class Collection(PostgresPartitionedModel):
    class PartitioningMeta:
        method = PostgresPartitioningMethod.RANGE
        key = ['date']
    STATUS_CHOICES = [
        (0 , 'Not yet attempted'),
        (1 , 'In the process'),
        (2 , 'Successfully completed'),
        (3 , 'Tried but failed'),
        (4 , 'Tried X times and failed.')
    ]
    user_num = models.ForeignKey(MyUser, on_delete = models.CASCADE)
    description= models.TimeField()
    amount = models.IntegerField()
    date = models.DateTimeField(auto_now=False, auto_now_add=True)
    status= models.IntegerField(choices=STATUS_CHOICES)