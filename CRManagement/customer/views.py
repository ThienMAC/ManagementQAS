from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
#Customer management
def customerList(request):
    context={

    }

    return render(request,"customer/customerList.html",context)


def addCustomer(request):

    context={

    }
    return render(request,'customer/addCustomer.html',context)


def updateCustomer(request):

    context={

    }
    return render(request,'customer/updateCustomer.html',context)

#End Customer Management

#Subsystem Management
def subsystemList(request):
    context={

    }
    return render(request,'customer/subsystemList.html',context)


def addSubsystem(request):
    context={

    }
    return render(request,'customer/addSubsystem.html',context)


def updateSubsystem(request):
    context={

    }
    return render(request,'customer/updateSubsystem.html',context)

#End Subsystem Management