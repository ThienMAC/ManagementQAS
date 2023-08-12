from django.contrib import admin
from .models import DepartmentType,RoomType,DocumentType

# Register your models here.
admin.site.register(DepartmentType)
admin.site.register(RoomType)
admin.site.register(DocumentType)
