from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect,HttpResponse
from accounts.forms import(
	RegistrationForm,
	EditTaskForm,
	CreateTaskForm)
from .models import Task
from django.contrib.auth.models import User
# Create your views here.
def home(request):
	return redirect('/accounts/login')
def register(request):

	if request.method =='POST':
		form=RegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/accounts/login')
	else:
	    form= RegistrationForm()
	return render(request, 'accounts/reg_forms.html', {'form':form})
def profile(request):
	user=request.user
	args={'user':user}
	return render(request,'accounts/profile.html',args)

def create_task(request):
    user = request.user
  
    if request.method=='POST':
       task=Task.objects.create(user=user)
       form = CreateTaskForm(request.POST)

       if form.is_valid():
          task.task_text = form.cleaned_data['task_text']
          task.save()
          return redirect('/accounts/profile')
    else:
        form=CreateTaskForm()
    return render(request,'accounts/create_task.html',{'form':form}) 

def delete_task(request,task_id):
    task=Task.objects.get(pk=task_id)
    task.delete()
    return redirect('/accounts/profile')
def edit_task(request,task_id):
    user = request.user
  
    if request.method=='POST':
       task=Task.objects.get(pk=task_id)
       form = EditTaskForm(request.POST)

       if form.is_valid():
          task.task_text = form.cleaned_data['task_text']
          task.save()
          return redirect('/accounts/profile')
    else:
        form=EditTaskForm()
    return render(request,'accounts/edit_task.html',{'form':form})    
