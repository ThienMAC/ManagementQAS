from django.shortcuts import render

# Create your views here.
def documentList(request):
    context={

    }

    return render(request,"document/documentList.html",context)


def updateDocument(request):
    context={

    }

    return render(request,"document/updateDocument.html",context)
