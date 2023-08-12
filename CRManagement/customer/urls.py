from django.urls import path
from . import views

urlpatterns = [
    #URL for Customer
    path("customerList",views.customerList,name="customerList"),
    path("customerAdd",views.customerAdd,name="customerAdd"),
    path("customerUpdate/<int:id>",views.customerUpdate,name="customerUpdate"),
    path("customerDelete/<int:id>",views.customerDelete,name="customerDelete"),
    #End URL for Customer

]
