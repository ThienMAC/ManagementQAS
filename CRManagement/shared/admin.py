from django.contrib import admin
from .models import DepartmentType, Department,RoomType,Room,DocumentType,Subsystem

# Register your models here.
admin.site.register(DepartmentType)
admin.site.register(Department)
admin.site.register(RoomType)
admin.site.register(Room)
admin.site.register(DocumentType)
admin.site.register(Subsystem)
