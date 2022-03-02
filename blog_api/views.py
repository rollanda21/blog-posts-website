from django.shortcuts import render
from rest_framework import serializers, generics
from blog.models import Post
from .serializers import PostSerializer

class PostList(generics.ListCreateAPIView):
    queryset = Post.postobjects.all()
    serializer_class = PostSerializer
    

class PostDetail(generics.RetrieveDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer