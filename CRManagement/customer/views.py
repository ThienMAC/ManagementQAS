from django.shortcuts import render, redirect,get_object_or_404
from .models import Customer,Contract
from shared.models import FolderStructure

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
def customerDetail(request,customerid):

    folders=FolderStructure.objects.all().order_by('id')
    customer=Customer.objects.get(id=customerid)
    if customer is None:
        return


    context={
        'folders':folders,
        'customer':customer
    }

    return render(request,"customer/customerDetail.html",context)

def contractList(request,cusid):

    customer=Customer.objects.get(id=cusid)

    if customer is None:
        return
    
    contracts=Contract.objects.filter(contractCustomer=customer.id).order_by('id')

    context={
        'contracts':contracts,
        'customer':customer
    }

    return render(request,"customer/customerDetail/contract/contractList.html",context)

def contractAdd(request,cusid):

    customer=Customer.objects.get(id=cusid)
    if customer is None:
        return
    context={
         'customer':customer   
    }
    if request.method=='POST':
        contractCode=request.POST.get('contractCode')
        contractName=request.POST.get('contractName')
        contractVersion=request.POST.get('contractVersion')
        contractType=request.POST.get('contractType')
        contractSize=request.POST.get('contractSize')        
        if request.POST.get('contractStatus')=='on':
            contractStatus=True
        else:
            contractStatus=False
        contractCustomer=customer
        contractBase64str=request.POST.get('contractBase64str')

        created_by=request.user
        modified_by=request.user
        contract=Contract(
            contractCode=contractCode,
            contractName=contractName,
            contractVersion=contractVersion,
            contractType=contractType,
            contractSize=contractSize,
            contractStatus=contractStatus,
            contractCustomer=contractCustomer,
            contractBase64str=contractBase64str,
            created_by=created_by,
            modified_by=modified_by
        )
        contract.save()
        context={
            'contract':contract,
            'customer':customer
        }

        return redirect('contractList',cusid)
    else:        
        return render(request,"customer/customerDetail/contract/contractAdd.html", context)
    

def contractUpdate(request,contractid):
   
    contract=Contract.objects.get(id=contractid)
    
    if contract is None:
        return
    
    customer=Customer.objects.get(customerName=contract.contractCustomer)

    if customer is None:
        return
    context={
        'contract':contract,
    }

    if request.method=='POST':
        contractCode=request.POST.get('contractCode')
        contractName=request.POST.get('contractName')
        contractVersion=request.POST.get('contractVersion')
        contractType=request.POST.get('contractType')
        contractSize=request.POST.get('contractSize')        
        if request.POST.get('contractStatus')=='on':
            contractStatus=True
        else:
            contractStatus=False
        contractBase64str=request.POST.get('contractBase64str')
        created_by=request.user
        modified_by=request.user
       
        contract.contractCode=contractCode
        contract.contractName=contractName
        contract.contractVersion=contractVersion
        contract.contractType=contractType
        contract.contractSize=contractSize
        contract.contractStatus=contractStatus
        contract.contractBase64str=contractBase64str
        contract.created_by=created_by
        contract.modified_by=modified_by
        
        contract.save()

        return redirect('contractList',customer.id)
    else:        
        return render(request,"customer/customerDetail/contract/contractUpdate.html", context)
    

def contractDelete(request,contractid):
    contract=Contract.objects.get(id=contractid)
    if contract is None:
        return

    else:
        customer=Customer.objects.get(customerName=contract.contractCustomer)
        contract.delete()
        return redirect('contractList',customer.id)

#End Customer Detail