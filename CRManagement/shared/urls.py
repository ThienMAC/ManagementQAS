from django.urls import path
from . import views

urlpatterns = [
    path("departmentTypeList",views.departmentTypeList,name="departmentTypeList"),
    path("departmentTypeAdd",views.departmentTypeAdd,name="departmentTypeAdd"),
    path("departmentTypeUpdate/<int:id>",views.departmentTypeUpdate,name="departmentTypeUpdate"),
    path("departmentTypeDelete/<int:id>",views.departmentTypeDelete,name="departmentTypeDelete"),

    path("departmentList",views.departmentList,name="departmentList"),
    path("departmentAdd",views.departmentAdd,name="departmentAdd"),
    path("departmentUpdate/<int:id>",views.departmentUpdate,name="departmentUpdate"),
    path("departmentDelete/<int:id>",views.departmentDelete,name="departmentDelete"),


    path("roomTypeList",views.roomTypeList,name="roomTypeList"),
    path("roomTypeAdd",views.roomTypeAdd,name="roomTypeAdd"),
    path("roomTypeUpdate/<int:id>",views.roomTypeUpdate,name="roomTypeUpdate"),
    path("roomTypeDelete/<int:id>",views.roomTypeDelete,name="roomTypeDelete"),


    path("roomList",views.roomList,name="roomList"),
    path("roomAdd",views.roomAdd,name="roomAdd"),
    path("roomUpdate/<int:id>",views.roomUpdate,name="roomUpdate"),
    path("roomDelete/<int:id>",views.roomDelete,name="roomDelete"),



]
