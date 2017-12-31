from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegistrationForm(UserCreationForm):
	class Meta:
		model = User
		fields ={
		    'username',
		    'first_name',
		    'last_name',
		    'email',
		    'password1',
		    'password2',
		}
	def save(self,commit=True):
		user = super(RegistrationForm,self).save(commit=False)
		user.first_name = self.cleaned_data['first_name']
		user.last_name = self.cleaned_data['last_name']
		user.email = self.cleaned_data['email']

		if commit:
			user.save()
		return user

class CreateTaskForm(forms.Form):
	task_text=forms.CharField(max_length=200)
	def clean_task_data(self):
		data=self.cleaned_data['task_text']
		return data