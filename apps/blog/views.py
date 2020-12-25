# apps/blog/views.py

from django.shortcuts import render
from .models import Post, Categoria


def home(request):
	posts = Post.objects.filter(estado = True)
	context = {
		'posts':posts,
	}
	return render(request, 'index.html', context)


def general(request):
	posts = Post.objects.filter(
		estado = True,
		categoria = Categoria.objects.get(nombre = 'General')
	)
	context = {
		'posts':posts,
	}	
	return render(request, 'general.html', context)


def programming(request):
	posts = Post.objects.filter(
		estado = True,
		categoria = Categoria.objects.get(nombre = 'Programming')
	)
	context = {
		'posts':posts,
	}	
	return render(request, 'programming.html', context)


def tutorial(request):
	posts = Post.objects.filter(
		estado = True,
		categoria = Categoria.objects.get(nombre = 'Tutorial')
	)
	context = {
		'posts':posts,
	}	
	return render(request, 'tutorial.html', context)


def technology(request):
	posts = Post.objects.filter(
		estado = True,
		categoria = Categoria.objects.get(nombre = 'Technology')
	)
	context = {
		'posts':posts,
	}	
	return render(request, 'technology.html', context)


def videogame(request):
	posts = Post.objects.filter(
		estado = True,
		categoria = Categoria.objects.get(nombre = 'Videogame')
	)
	context = {
		'posts':posts,
	}	
	return render(request, 'videogame.html', context)
	

