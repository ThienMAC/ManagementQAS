from django.urls import path
from . import views

urlpatterns = [
    path("customerList",views.customerList,name="customerList"),
    path("addCustomer",views.addCustomer,name="addCustomer"),
    path("updateCustomer",views.updateCustomer,name="updateCustomer"),
]
