from django.urls import path

from .views import HomePage,PostDetails,CreatePost,PostDeleteView,PostUpdateView


urlpatterns = [
    path("",HomePage.as_view(),name="home"),
    path("post/<int:pk>/",PostDetails.as_view(),name="postdetails"),
    path("create/",CreatePost.as_view(),name="create"),
    path("delete/<int:pk>/",PostDeleteView.as_view(),name="delete"),
    path("update/<int:pk>/",PostUpdateView.as_view(),name="update"),
]
