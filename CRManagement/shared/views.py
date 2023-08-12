from django.shortcuts import render,redirect
from .models import DepartmentType, Department, RoomType,Room,DocumentType,Subsystem
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
# Department
def departmentList(request):

    depts=Department.objects.all().order_by('id')

    context={
        'depts':depts
    }
    return render(request,"shared/departmentList.html", context)


def departmentAdd(request):

    context={
            
    }
    if request.method=='POST':
        deptCode=request.POST.get('deptCode')
        deptName=request.POST.get('deptName')
        if request.POST.get('isActive')=='on':
            isActive=True
        else:
            isActive=False
        created_by=request.user
        modified_by=request.user
        dept=Department(
            deptCode=deptCode,
            deptName=deptName,
            isActive=isActive,
            created_by=created_by,
            modified_by=modified_by
        )
        dept.save()
        context={
            'dept':dept
        }

        return redirect('departmentList')
    else:        
        return render(request,"shared/departmentAdd.html", context)
    

def departmentUpdate(request,id):

    dept=Department.objects.get(id=id)
    if dept is None:
        return
    
    if request.method=='POST':
        deptCode=request.POST.get('deptCode')
        deptName=request.POST.get('deptName')
        if request.POST.get('isActive')=='on':
            isActive=True
        else:
            isActive=False
        created_by=dept.created_by
        modified_by=request.user
       
        dept.deptCode=deptCode
        dept.deptName=deptName
        dept.isActive=isActive
        dept.created_by=created_by
        dept.modified_by=modified_by
        
        dept.save()
        return redirect('departmentList')
    context={
        'dept':dept
    }
    return render(request,"shared/departmentUpdate.html", context)

def departmentDelete(request,id):
    dept=Department.objects.get(id=id)
    if dept is None:
        return
    
    else:
        dept.delete()
        return redirect('departmentList')
    
#End Department

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


#Start Room
def roomList(request):

    rooms=Room.objects.all().order_by('id')

    context={
        'rooms':rooms
    }
    return render(request,"shared/roomList.html", context)


def roomAdd(request):

    context={
            
    }
    if request.method=='POST':
        roomCode=request.POST.get('roomCode')
        roomName=request.POST.get('roomName')
        if request.POST.get('isActive')=='on':
            isActive=True
        else:
            isActive=False
        created_by=request.user
        modified_by=request.user
        room=Room(
            roomCode=roomCode,
            roomName=roomName,
            isActive=isActive,
            created_by=created_by,
            modified_by=modified_by
        )
        room.save()
        context={
            'room':room
        }

        return redirect('roomList')
    else:        
        return render(request,"shared/roomAdd.html", context)
    

def roomUpdate(request,id):

    room=Room.objects.get(id=id)
    if room is None:
        return
    
    if request.method=='POST':
        roomCode=request.POST.get('roomCode')
        roomName=request.POST.get('roomName')
        if request.POST.get('isActive')=='on':
            isActive=True
        else:
            isActive=False
        created_by=request.user
        modified_by=request.user
       
        room.roomCode=roomCode
        room.roomName=roomName
        room.isActive=isActive
        room.created_by=created_by
        room.modified_by=modified_by
        
        room.save()
        return redirect('roomList')
    context={
        'room':room
    }
    return render(request,"shared/roomUpdate.html", context)

def roomDelete(request,id):
    room=Room.objects.get(id=id)
    if room is None:
        return
    
    else:
        room.delete()
        return redirect('roomList')

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

#Start Subsystem
def subsystemList(request):

    subsystems=Subsystem.objects.all().order_by('id')

    context={
        'subsystems':subsystems
    }
    return render(request,"shared/subsystemList.html", context)


def subsystemAdd(request):

    context={
            
    }
    if request.method=='POST':
        subsystemCode=request.POST.get('subsystemCode')
        subsystemName=request.POST.get('subsystemName')
        if request.POST.get('isActive')=='on':
            isActive=True
        else:
            isActive=False
        created_by=request.user
        modified_by=request.user
        subsystem=Subsystem(
            subsystemCode=subsystemCode,
            subsystemName=subsystemName,
            isActive=isActive,
            created_by=created_by,
            modified_by=modified_by
        )
        subsystem.save()
        context={
            'subsystem':subsystem
        }

        return redirect('subsystemList')
    else:        
        return render(request,"shared/subsystemAdd.html", context)
    

def subsystemUpdate(request,id):

    subsystem=Subsystem.objects.get(id=id)
    if subsystem is None:
        return
    
    if request.method=='POST':
        subsystemCode=request.POST.get('subsystemCode')
        subsystemName=request.POST.get('subsystemName')
        if request.POST.get('isActive')=='on':
            isActive=True
        else:
            isActive=False
        created_by=request.user
        modified_by=request.user
       
        subsystem.documentTypeCode=subsystemCode
        subsystem.documentTypeName=subsystemName
        subsystem.isActive=isActive
        subsystem.created_by=created_by
        subsystem.modified_by=modified_by
        
        subsystem.save()
        return redirect('subsystemList')
    context={
        'subsystem':subsystem
    }
    return render(request,"shared/subsystemUpdate.html", context)

def subsystemDelete(request,id):
    subsystem=Subsystem.objects.get(id=id)
    if subsystem is None:
        return
    
    else:
        subsystem.delete()
        return redirect('subsystemList')

#End Subsystem