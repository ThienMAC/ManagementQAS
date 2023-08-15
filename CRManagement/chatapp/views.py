from django.shortcuts import render

# Create your views here.
def chat_index(request):
    context={

    }

    return render(request,"chatapp/chat_index.html",context)
    