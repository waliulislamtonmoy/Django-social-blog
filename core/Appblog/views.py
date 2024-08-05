from django.shortcuts import render

# Create your views here.
from . models import Post
from django.http import HttpResponse
from django.views.generic import ListView,DetailView,CreateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin

class HomePage(ListView):
    model=Post
    template_name="appblog/Home.html"
    context_object_name='posts'
    ordering=["-id"]
    
    
class PostDetails(DetailView):
    model=Post
    template_name='appblog/Detailsblog.html'
    
class CreatePost(LoginRequiredMixin,CreateView):
    model=Post
    fields=['title','content']
    template_name="appblog/Newpost.html"
    success_url="/"
    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model=Post 
    template_name='appblog/Deleteview.html'
    success_url="/"
    def test_func(self):
        post=self.get_object()
        if self.request.user == post.author:
            return True
        return False
    
    
    
    
        
        
    
    