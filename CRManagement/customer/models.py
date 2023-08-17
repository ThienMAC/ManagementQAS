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


class Contract(models.Model):
    contractCode=models.CharField(max_length=50,blank=False)
    contractName=models.CharField(max_length=200,blank=False)
    contractVersion=models.CharField(max_length=20,blank=False)
    contractType=models.CharField(max_length=200,blank=False)
    contractSize=models.FloatField()
    contractBase64str=models.FileField()
    contractCustomer=models.ForeignKey(Customer,related_name='Contract_Customer_2_contracCustomer',on_delete=models.CASCADE)
    created_date=models.DateTimeField(auto_now_add=True, blank=True)
    created_by=models.ForeignKey(User,related_name='user_Contract_2created_by',on_delete=models.CASCADE)
    modified_date=models.DateTimeField(auto_now_add=True, blank=True)
    modified_by=models.ForeignKey(User,related_name='user_Contract_2modified_by',on_delete=models.CASCADE)

    def __str__(self):
        return self.contractName



