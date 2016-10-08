from django.shortcuts import render
from .models import Register
from .forms import RegisterForm
from django.http import HttpResponse

def index(request):
	#name = request.getParameter()
	return HttpResponse(registration.html)
	return render("Hello World!")


def	post_new(request):
	form = RegisterForm()
	return render(request, 'registration.html', {'form': form})

def upload_image(request):
	form = GallaryForm()
	return render(request, 'registration.html', {'form': form})

def register(request):
	return render(request, 'registration.html', {})
	
