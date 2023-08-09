from django.shortcuts import render

# Create your views here.
def documentList(request):
    context={

    }

    return render(request,"document/documentList.html",context)