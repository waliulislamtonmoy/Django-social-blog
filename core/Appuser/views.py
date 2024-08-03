from django.shortcuts import render,redirect

from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout
from django.shortcuts import HttpResponsePermanentRedirect 
from django.urls import reverse

from django.contrib.auth.mixins import LoginRequiredMixin

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
        return render(request,"appuser/Profile.html")
    

        