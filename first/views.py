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
    cats=Category.objects.all()
    context ={
        'posts': posts,
        'cats':cats,
        'menu': menu,
        'title':'main page',
        'cat_selected':0,
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

def show_post(request, post_id):
    return HttpResponse(f'<h1>show post with id</h1><p>{post_id}</p>')

def show_category(request, cat_id):
    posts = Man.objects.filter(cat_id=cat_id)
    cats = Category.objects.all()

    if len(posts) == 0:
        raise Http404

    context = {
        'posts': posts,
        'cats': cats,
        'menu': menu,
        'title': 'main page',
        'cat_selected': cat_id,
    }
    return render(request, 'first/index.html', context=context)

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>this page not found</h1>')