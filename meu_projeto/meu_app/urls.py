from django.urls import path
from . import views

urlpatterns = [
    path('api/posts/', views.PostListCreate.as_view(), name='post-list-create'),
    path('', views.index, name='index'),
]
