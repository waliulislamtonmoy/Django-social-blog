from django.urls import path


from django.contrib.auth import views as auth_view


from Appuser.views import RegisterView ,logout_user,Profileview


urlpatterns = [
    path("signup/",RegisterView.as_view(),name="signup"),
    path("login",auth_view.LoginView.as_view(template_name="appuser/Login.html"),name="login"),
    path("logout/",view=logout_user,name="logout"),
    path("profile/",Profileview.as_view(),name='profile')
]
