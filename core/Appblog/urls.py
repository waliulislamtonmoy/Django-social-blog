from django.urls import path

from .views import HomePage,PostDetails,CreatePost,PostDeleteView


urlpatterns = [
    path("",HomePage.as_view(),name="home"),
    path("post/<int:pk>/",PostDetails.as_view(),name="postdetails"),
    path("create/",CreatePost.as_view(),name="create"),
    path("delete/<int:pk>/",PostDeleteView.as_view(),name="delete"),
]
