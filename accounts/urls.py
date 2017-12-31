
from django.urls import path
from . import views
from django.contrib.auth.views import login,logout

urlpatterns = [
   path('',views.home),
   path('login/', login, {'template_name':'accounts/login.html'}),
   path('logout/', logout, {'template_name':'accounts/logout.html'}),
   path('register/',views.register,name='register'),
   path('profile/',views.profile,name='view_profile'),
   path('profile/create_task',views.create_task,name='create_task'),
   path('profile/delete_task/<int:task_id>',views.delete_task,name='delete_task')
]