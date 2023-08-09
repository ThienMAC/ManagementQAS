from django.urls import path
from . import views

urlpatterns = [
    path("documentList",views.documentList,name="documentList"),
    path("updateDocument",views.updateDocument,name="updateDocument"),
]
