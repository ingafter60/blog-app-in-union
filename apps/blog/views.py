# apps/blog/views.py

from django.shortcuts import render


def home(request):
	return render(request, 'index.html')

def general(request):
	return render(request, 'general.html')

def programming(request):
	return render(request, 'programming.html')

def tutorial(request):
	return render(request, 'tutorial.html')

def technology(request):
	return render(request, 'technology.html')
	
def videogame(request):
	return render(request, 'videogame.html')
