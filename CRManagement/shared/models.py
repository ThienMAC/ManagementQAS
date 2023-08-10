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