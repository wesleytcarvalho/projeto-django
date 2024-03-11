from rest_framework import generics
from .models import Post
from .serializers import PostSerializer
from django.shortcuts import render
from .models import Post

class PostListCreate(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

def index(request):
    posts = Post.objects.all()
    return render(request, 'meu_app/index.html', {'posts': posts})