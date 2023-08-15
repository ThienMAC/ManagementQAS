from django.urls import path
from . import views

urlpatterns = [
    path("departmentTypeList",views.departmentTypeList,name="departmentTypeList"),
    path("departmentTypeAdd",views.departmentTypeAdd,name="departmentTypeAdd"),
    path("departmentTypeUpdate/<int:id>",views.departmentTypeUpdate,name="departmentTypeUpdate"),
    path("departmentTypeDelete/<int:id>",views.departmentTypeDelete,name="departmentTypeDelete"),


    path("roomTypeList",views.roomTypeList,name="roomTypeList"),
    path("roomTypeAdd",views.roomTypeAdd,name="roomTypeAdd"),
    path("roomTypeUpdate/<int:id>",views.roomTypeUpdate,name="roomTypeUpdate"),
    path("roomTypeDelete/<int:id>",views.roomTypeDelete,name="roomTypeDelete"),

    path("documentTypeList",views.documentTypeList,name="documentTypeList"),
    path("documentTypeAdd",views.documentTypeAdd,name="documentTypeAdd"),
    path("documentTypeUpdate/<int:id>",views.documentTypeUpdate,name="documentTypeUpdate"),
    path("documentTypeDelete/<int:id>",views.documentTypeDelete,name="documentTypeDelete"),


    path("folderStructureList",views.folderStructureList,name="folderStructureList"),
    path("folderStructureAdd",views.folderStructureAdd,name="folderStructureAdd"),
    path("folderStructureUpdate/<int:id>",views.folderStructureUpdate,name="folderStructureUpdate"),
    path("folderStructureDelete/<int:id>",views.folderStructureDelete,name="folderStructureDelete"),




]
