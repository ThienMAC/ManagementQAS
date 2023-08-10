from django.urls import path
from . import views

urlpatterns = [
    path("departmentTypeList",views.departmentTypeList,name="departmentTypeList"),
    path("departmentTypeAdd",views.departmentTypeAdd,name="departmentTypeAdd"),
    path("departmentTypeUpdate/<int:id>",views.departmentTypeUpdate,name="departmentTypeUpdate"),
    path("departmentTypeDelete/<int:id>",views.departmentTypeDelete,name="departmentTypeDelete"),
]
