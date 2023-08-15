from django.contrib import admin
from .models import DepartmentType,RoomType,DocumentType,FolderStructure

# Register your models here.
admin.site.register(DepartmentType)
admin.site.register(RoomType)
admin.site.register(DocumentType)
admin.site.register(FolderStructure)
