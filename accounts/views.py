from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect,HttpResponse
# Create your views here.
def home(request):
	return HttpResponse('Hello. Welcome to Home Page')