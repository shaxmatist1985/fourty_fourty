from django.http import HttpResponse, Http404, HttpResponseNotFound
from django.shortcuts import render, redirect
from .models import *

menu=[{'title': 'About site', 'url_name': 'about'},
      {'title': 'Add page', 'url_name': 'addpage'},
      {'title': 'Contact', 'url_name': 'contact'},
      {'title': 'Login', 'url_name': 'login'}
      ]

def index(request):
    posts=Man.objects.all()
    context ={
        'posts': posts,
        'menu': menu,
        'title':'main page'
    }
    return render(request, 'first/index.html', context=context)

def about(request):
    return render(request, 'first/about.html', {'menu': menu,'title': 'page about site'})

def addpage(request):
    return HttpResponse('<h1>add page</h1>')

def contact(request):
    return HttpResponse('<h1>contact</h1>')

def login(request):
    return HttpResponse('<h1>login</h1>')

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>this page not found</h1>')