from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.
class Customer(models.Model):
    customerCode=models.CharField(max_length=50,blank=False)
    customerName=models.CharField(max_length=200,blank=False)
    customerAddress=models.CharField(max_length=2000,blank=True)
    customerHotline=models.CharField(max_length=20,blank=True)
    isActive=models.BooleanField()
    created_date=models.DateTimeField(auto_now_add=True, blank=True)
    created_by=models.ForeignKey(User,related_name='user_Customer_2created_by',on_delete=models.CASCADE)
    modified_date=models.DateTimeField(auto_now_add=True, blank=True)
    modified_by=models.ForeignKey(User,related_name='user_Customer_2modified_by',on_delete=models.CASCADE)


    def __str__(self):
        return self.customerName