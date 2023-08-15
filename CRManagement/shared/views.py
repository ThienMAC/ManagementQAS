from django.shortcuts import render,redirect
from .models import DepartmentType, RoomType,DocumentType,FolderStructure
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
        created_by=deptType.created_by
        created_date=deptType.created_date
        modified_by=request.user
       
        deptType.deptTypeCode=deptTypeCode
        deptType.deptTypeName=deptTypeName
        deptType.isActive=isActive
        deptType.created_by=created_by
        deptType.created_date=created_date
        deptType.modified_by=modified_by
        
        deptType.save()
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
    
#End DepartmentType

#Start RoomType
def roomTypeList(request):

    roomTypes=RoomType.objects.all().order_by('id')

    context={
        'roomTypes':roomTypes
    }
    return render(request,"shared/roomTypeList.html", context)


def roomTypeAdd(request):

    context={
            
    }
    if request.method=='POST':
        roomTypeCode=request.POST.get('roomTypeCode')
        roomTypeName=request.POST.get('roomTypeName')
        if request.POST.get('isActive')=='on':
            isActive=True
        else:
            isActive=False
        created_by=request.user
        modified_by=request.user
        roomType=RoomType(
            roomTypeCode=roomTypeCode,
            roomTypeName=roomTypeName,
            isActive=isActive,
            created_by=created_by,
            modified_by=modified_by
        )
        roomType.save()
        context={
            'roomType':roomType
        }

        return redirect('roomTypeList')
    else:        
        return render(request,"shared/roomTypeAdd.html", context)
    

def roomTypeUpdate(request,id):

    roomType=RoomType.objects.get(id=id)
    if roomType is None:
        return
    
    if request.method=='POST':
        roomTypeCode=request.POST.get('roomTypeCode')
        roomTypeName=request.POST.get('roomTypeName')
        if request.POST.get('isActive')=='on':
            isActive=True
        else:
            isActive=False
        created_by=request.user
        modified_by=request.user
       
        roomType.roomTypeCode=roomTypeCode
        roomType.roomTypeName=roomTypeName
        roomType.isActive=isActive
        roomType.created_by=created_by
        roomType.modified_by=modified_by
        
        roomType.save()
        return redirect('roomTypeList')
    context={
        'roomType':roomType
    }
    return render(request,"shared/roomTypeUpdate.html", context)

def roomTypeDelete(request,id):
    roomType=RoomType.objects.get(id=id)
    if roomType is None:
        return
    
    else:
        roomType.delete()
        return redirect('roomTypeList')

#End RoomType


#Start DocumentType
def documentTypeList(request):

    documentTypes=DocumentType.objects.all().order_by('id')

    context={
        'documentTypes':documentTypes
    }
    return render(request,"shared/documentTypeList.html", context)


def documentTypeAdd(request):

    context={
            
    }
    if request.method=='POST':
        documentTypeCode=request.POST.get('documentTypeCode')
        documentTypeName=request.POST.get('documentTypeName')
        if request.POST.get('isActive')=='on':
            isActive=True
        else:
            isActive=False
        created_by=request.user
        modified_by=request.user
        doctype=DocumentType(
            documentTypeCode=documentTypeCode,
            documentTypeName=documentTypeName,
            isActive=isActive,
            created_by=created_by,
            modified_by=modified_by
        )
        doctype.save()
        context={
            'doctype':doctype
        }

        return redirect('documentTypeList')
    else:        
        return render(request,"shared/documentTypeAdd.html", context)
    

def documentTypeUpdate(request,id):

    doctype=DocumentType.objects.get(id=id)
    if doctype is None:
        return
    
    if request.method=='POST':
        documentTypeCode=request.POST.get('documentTypeCode')
        documentTypeName=request.POST.get('documentTypeName')
        if request.POST.get('isActive')=='on':
            isActive=True
        else:
            isActive=False
        created_by=request.user
        modified_by=request.user
       
        doctype.documentTypeCode=documentTypeCode
        doctype.documentTypeName=documentTypeName
        doctype.isActive=isActive
        doctype.created_by=created_by
        doctype.modified_by=modified_by
        
        doctype.save()
        return redirect('documentTypeList')
    context={
        'doctype':doctype
    }
    return render(request,"shared/documentTypeUpdate.html", context)

def documentTypeDelete(request,id):
    doctype=DocumentType.objects.get(id=id)
    if doctype is None:
        return
    
    else:
        doctype.delete()
        return redirect('documentTypeList')

#End DocumentType


#Start Folder Structure
def folderStructureList(request):

    folderStructures=FolderStructure.objects.all().order_by('id')

    context={
        'folderStructures':folderStructures
    }
    return render(request,"shared/folderStructureList.html", context)


def folderStructureAdd(request):

    context={
            
    }
    if request.method=='POST':
        folderStructureCode=request.POST.get('folderStructureCode')
        folderStructureName=request.POST.get('folderStructureName')
        if request.POST.get('isActive')=='on':
            isActive=True
        else:
            isActive=False
        created_by=request.user
        modified_by=request.user
        folderStruct=FolderStructure(
            folderStructureCode=folderStructureCode,
            folderStructureName=folderStructureName,
            isActive=isActive,
            created_by=created_by,
            modified_by=modified_by
        )
        folderStruct.save()
        context={
            'folderStruct':folderStruct
        }

        return redirect('folderStructureList')
    else:        
        return render(request,"shared/folderStructureAdd.html", context)
    

def folderStructureUpdate(request,id):

    folder=FolderStructure.objects.get(id=id)
    if folder is None:
        return
    
    if request.method=='POST':
        folderStructureCode=request.POST.get('folderStructureCode')
        folderStructureName=request.POST.get('folderStructureName')
        if request.POST.get('isActive')=='on':
            isActive=True
        else:
            isActive=False
        created_by=request.user
        modified_by=request.user
       
        folder.folderStructureCode=folderStructureCode
        folder.folderStructureName=folderStructureName
        folder.isActive=isActive
        folder.created_by=created_by
        folder.modified_by=modified_by
        
        folder.save()
        return redirect('folderStructureList')
    context={
        'folder':folder
    }
    return render(request,"shared/folderStructureUpdate.html", context)


def folderStructureDelete(request,id):
    folder=FolderStructure.objects.get(id=id)
    if folder is None:
        return
    
    else:
        folder.delete()
        return redirect('folderStructureList')

#End Folder Structure