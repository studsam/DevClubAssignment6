from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect,HttpResponse
from accounts.forms import(RegistrationForm,)
# Create your views here.
def home(request):
	return HttpResponse('Hello. Welcome to Home Page')
def register(request):

	if request.method =='POST':
		form=RegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/accounts')
	else:
	    form= RegistrationForm()
	return render(request, 'accounts/reg_forms.html', {'form':form})
def profile(request):
	user=request.user
	args={'user':user}
	return render(request,'accounts/profile.html',args)
