
from django.urls import path
from . import views
from django.contrib.auth.views import login,logout

urlpatterns = [
   path('',views.home),
]