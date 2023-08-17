from django.urls import path
from . import views

urlpatterns = [
    #URL for Customer
    path("customerList",views.customerList,name="customerList"),
    path("customerAdd",views.customerAdd,name="customerAdd"),
    path("customerUpdate/<int:id>",views.customerUpdate,name="customerUpdate"),
    path("customerDelete/<int:id>",views.customerDelete,name="customerDelete"),
    #End URL for Customer

    #Start Customer Detail
    path("customerDetail",views.customerDetail,name="customerDetail"),

    path("customerDetail/contractList",views.contractList,name="contractList"),

    #End Customer Detail
]
