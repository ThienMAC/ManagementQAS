from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def customerList(request):
    context={

    }

    return render(request,"customer/customerList.html",context)