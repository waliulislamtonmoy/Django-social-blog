from django.shortcuts import render

# Create your views here.
from . models import Post
from django.http import HttpResponse
from django.views.generic import ListView

class HomePage(ListView):
    model=Post
    template_name="appblog/Home.html"
    context_object_name='posts'