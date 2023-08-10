from django.shortcuts import render,redirect
from .models import DepartmentType
from django.contrib.auth.models import User

# Create your views here.

# DepartmentType
def departmentTypeList(request):

    deptTypes=DepartmentType.objects.all().order_by('id')

    context={
        'deptTypes':deptTypes
    }
    return render(request,"shared/departmentTypeList.html", context)


def departmentTypeAdd(request):

    context={
            
    }
    if request.method=='POST':
        deptTypeCode=request.POST.get('deptTypeCode')
        deptTypeName=request.POST.get('deptTypeName')
        print(request.POST.get('isActive'))
        if request.POST.get('isActive')=='on':
            isActive=True
        else:
            isActive=False
        created_by=request.user
        modified_by=request.user
        deptType=DepartmentType(
            deptTypeCode=deptTypeCode,
            deptTypeName=deptTypeName,
            isActive=isActive,
            created_by=created_by,
            modified_by=modified_by
        )
        deptType.save()
        context={
            'deptType':deptType
        }

        return redirect('departmentTypeList')
    else:        
        return render(request,"shared/departmentTypeAdd.html", context)


def departmentTypeUpdate(request,id):

    deptType=DepartmentType.objects.get(id=id)
    if deptType is None:
        return
    
    if request.method=='POST':
        deptTypeCode=request.POST.get('deptTypeCode')
        deptTypeName=request.POST.get('deptTypeName')
        if request.POST.get('isActive')=='on':
            isActive=True
        else:
            isActive=False
        modified_by=request.user
        # deptType=DepartmentType(
        #     deptTypeCode=deptTypeCode,
        #     deptTypeName=deptTypeName,
        #     isActive=isActive,
        #     modified_by=modified_by
        # )
        deptType.update(
            deptTypeCode=deptTypeCode,
            deptTypeName=deptTypeName,
            isActive=isActive,
            modified_by=modified_by
        )      

        return redirect('departmentTypeList')
    context={
        'deptType':deptType
    }
    return render(request,"shared/departmentTypeUpdate.html", context)


def departmentTypeDelete(request,id):
    deptType=DepartmentType.objects.get(id=id)
    if deptType is None:
        return
    
    else:
        deptType.delete()
        return redirect('departmentTypeList')