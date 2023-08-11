from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.

#Start DepartmentType
class DepartmentType(models.Model):
    deptTypeCode=models.CharField(max_length=50,blank=False)
    deptTypeName=models.CharField(max_length=200,blank=False)
    isActive=models.BooleanField()
    created_date=models.DateTimeField(auto_now_add=True, blank=True)
    created_by=models.ForeignKey(User,related_name='user2created_by',on_delete=models.CASCADE)
    modified_date=models.DateTimeField(auto_now_add=True, blank=True)
    modified_by=models.ForeignKey(User,related_name='user2modified_by',on_delete=models.CASCADE)

    def __str__(self):
        return self.deptTypeName
#End departmentType


#Start Department
class Department(models.Model):
    deptCode=models.CharField(max_length=50,blank=False)
    deptName=models.CharField(max_length=200,blank=False)
    isActive=models.BooleanField()
    created_date=models.DateTimeField(auto_now_add=True, blank=True)
    created_by=models.ForeignKey(User,related_name='user_Department_2created_by',on_delete=models.CASCADE)
    modified_date=models.DateTimeField(auto_now_add=True, blank=True)
    modified_by=models.ForeignKey(User,related_name='user_Department_2modified_by',on_delete=models.CASCADE)

#End Department