from django.urls import path
from . import views


urlpatterns = [
    path("setupDepartment",views.setupDepartment,name="setupDepartment"),
    path("setupSubsystem",views.setupSubsystem,name="setupSubsystem"),
]
