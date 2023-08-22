from django.contrib import admin
from .models import Customer,Contract

# Register your models here.
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("customerCode", "customerName")
@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    list_display=("contractCode","contractName","contractVersion","contractType","contractSize","contractCustomer")