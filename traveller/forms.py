from django import forms
from .models import Traveller
from django.contrib.auth.forms import UserCreationForm

class UserRegistrationForm(UserCreationForm):
	"""docstring for UserRegisterForm"""
	#email = forms.EmailField()

	class Meta:
		model = Traveller
		fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']