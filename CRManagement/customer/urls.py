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
    path("customerDetail/contract/<int:customerid>",views.customerDetail,name="customerDetail"),


    #Start Contract
    path("customerDetail/contract/contractList/<int:cusid>",views.contractList,name="contractList"),
    path("customerDetail/contract/contractList/contractAdd/<int:cusid>",views.contractAdd,name="contractAdd"),
    path("customerDetail/contract/contractList/contractUpdate/<int:contractid>",views.contractUpdate,name="contractUpdate"),
    path("customerDetail/contract/contractList/contractDelete/<int:contractid>",views.contractDelete,name="contractDelete"),
    #End Contract

    #Start Analysis

    #End Analysis


    #End Customer Detail
]
