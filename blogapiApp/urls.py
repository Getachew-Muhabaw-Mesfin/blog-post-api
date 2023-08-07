from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('all-posts/', views.getAllPosts),
    path('create-new-post/',views.createNewPost),
    path('delete-post/', views.deletePost),
    path('get-post/', views.getPost),
    path('update-post/', views.updatePost),
]
