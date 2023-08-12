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

    def __str__(self):
        return self.deptName

#End Department

#Start RoomType
class RoomType(models.Model):
    roomTypeCode=models.CharField(max_length=50,blank=False)
    roomTypeName=models.CharField(max_length=200,blank=False)
    isActive=models.BooleanField()
    created_date=models.DateTimeField(auto_now_add=True, blank=True)
    created_by=models.ForeignKey(User,related_name='user_RoomType_2created_by',on_delete=models.CASCADE)
    modified_date=models.DateTimeField(auto_now_add=True, blank=True)
    modified_by=models.ForeignKey(User,related_name='user_RoomType_2modified_by',on_delete=models.CASCADE)

    def __str__(self):
        return self.roomTypeName
#End RoomType

#Start Room
class Room(models.Model):
    roomCode=models.CharField(max_length=50,blank=False)
    roomName=models.CharField(max_length=200,blank=False)
    isActive=models.BooleanField()
    created_date=models.DateTimeField(auto_now_add=True, blank=True)
    created_by=models.ForeignKey(User,related_name='user_Room_2created_by',on_delete=models.CASCADE)
    modified_date=models.DateTimeField(auto_now_add=True, blank=True)
    modified_by=models.ForeignKey(User,related_name='user_Room_2modified_by',on_delete=models.CASCADE)

    def __str__(self):
        return self.roomName

#End Room

#Start DocumentType
class DocumentType(models.Model):
    documentTypeCode=models.CharField(max_length=50,blank=False)
    documentTypeName=models.CharField(max_length=200,blank=False)
    isActive=models.BooleanField()
    created_date=models.DateTimeField(auto_now_add=True, blank=True)
    created_by=models.ForeignKey(User,related_name='user_DocumentType_2created_by',on_delete=models.CASCADE)
    modified_date=models.DateTimeField(auto_now_add=True, blank=True)
    modified_by=models.ForeignKey(User,related_name='user_DocumentType_2modified_by',on_delete=models.CASCADE)

    def __str__(self):
        return self.documentTypeName

#End DocumentType

#Start Subsystem
class Subsystem(models.Model):
    subsystemCode=models.CharField(max_length=50,blank=False)
    subsystemName=models.CharField(max_length=200,blank=False)
    isActive=models.BooleanField()
    created_date=models.DateTimeField(auto_now_add=True, blank=True)
    created_by=models.ForeignKey(User,related_name='user_Subsystem_2created_by',on_delete=models.CASCADE)
    modified_date=models.DateTimeField(auto_now_add=True, blank=True)
    modified_by=models.ForeignKey(User,related_name='user_Subsystem_2modified_by',on_delete=models.CASCADE)

    def __str__(self):
        return self.subsystemName

#End Subsystem
