from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegistrationForm

def home(request):
	context = {
		#"posts": Post.objects.all()
		'title': 'Traveller Home'
	}
	return render(request, 'traveller/home.html', context)

def main(request):
	context = {
		#"posts": Post.objects.all()
		'title': 'Traveller Main'
	}
	return render(request, 'traveller/main.html', context)

from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegistrationForm

def signup(request):
	if request.method == "POST":
		form = UserRegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f'Congratulations {username}, Your account has been created! You are now able to log in.')
			return redirect('login')
	else:
		form = UserRegistrationForm()
	return render(request, 'traveller/signup.html', {'form': form} )
