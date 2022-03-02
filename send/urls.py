from django.urls import path, include
from . import views
from .views import ContactSuccessView, ContactView

app_name = 'send'

urlpatterns = [
    
    path("",ContactView.as_view(),name= "contact" ),
    path('success/', ContactSuccessView.as_view(), name = "success"),
]
