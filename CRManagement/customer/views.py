from django.shortcuts import render, redirect
from .models import Customer

# Create your views here.
#Start Customer
def customerList(request):

    customers=Customer.objects.all().order_by('id')

    context={
        'customers':customers
    }
    return render(request,"customer/customerList.html", context)


def customerAdd(request):

    context={
            
    }
    if request.method=='POST':
        customerCode=request.POST.get('customerCode')
        customerName=request.POST.get('customerName')
        customerAddress=request.POST.get('customerAddress')
        customerHotline=request.POST.get('customerHotline')
        if request.POST.get('isActive')=='on':
            isActive=True
        else:
            isActive=False
        created_by=request.user
        modified_by=request.user
        customer=Customer(
            customerCode=customerCode,
            customerName=customerName,
            customerAddress=customerAddress,
            customerHotline=customerHotline,
            isActive=isActive,
            created_by=created_by,
            modified_by=modified_by
        )
        customer.save()
        context={
            'customer':customer
        }

        return redirect('customerList')
    else:        
        return render(request,"customer/customerAdd.html", context)
    

def customerUpdate(request,id):

    customer=Customer.objects.get(id=id)
    if customer is None:
        return
    
    if request.method=='POST':
        customerCode=request.POST.get('customerCode')
        customerName=request.POST.get('customerName')
        customerAddress=request.POST.get('customerAddress')
        customerHotline=request.POST.get('customerHotline')
        if request.POST.get('isActive')=='on':
            isActive=True
        else:
            isActive=False
        created_by=request.user
        modified_by=request.user
       
        customer.customerCode=customerCode
        customer.customerName=customerName
        customer.customerAddress=customerAddress
        customer.customerHotline=customerHotline
        customer.isActive=isActive
        customer.created_by=created_by
        customer.modified_by=modified_by
        
        customer.save()
        return redirect('customerList')
    context={
        'customer':customer
    }
    return render(request,"customer/customerUpdate.html", context)

def customerDelete(request,id):
    customer=Customer.objects.get(id=id)
    if customer is None:
        return
    
    else:
        customer.delete()
        return redirect('customerList')

#End Customer


#Start customer Detail
def customerDetail(request):
    context={

    }

    return render(request,"customer/customerDetail.html",context)

#End Customer Detail