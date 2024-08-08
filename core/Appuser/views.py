from django.shortcuts import render,redirect

from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout
from django.shortcuts import HttpResponsePermanentRedirect 
from django.urls import reverse

from django.contrib.auth.mixins import LoginRequiredMixin
from .models import UserUpdateForm,UserProfileUpdateForm

# Create your views here.


def logout_user(request):
    logout(request)
    return HttpResponsePermanentRedirect(reverse("login"))

class RegisterView(View):
    def get(self,request):      
        form=UserCreationForm()
        return render(request,"appuser/Register.html",{"form":form})
    def post(self,request):
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
        return redirect("signup")
    
class Profileview(LoginRequiredMixin,View):
    def get(self,request):
        p_form=UserProfileUpdateForm(instance=request.user.profile)
        u_form=UserUpdateForm(instance=request.user)
        context={
            "p_form":p_form,
            "u_form":u_form
        }
        return render(request,"appuser/Profile.html",context)
    
    def post(self,request,*args, **kwargs):
        p_form=UserProfileUpdateForm(request.POST, request.FILES,instance=request.user.profile)
        u_form=UserUpdateForm(request.POST,instance=request.user)
        u_form.save()
        p_form.save()
        return redirect("profile")
        
    

        