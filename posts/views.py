from django.shortcuts import render

# Create your views here.
# code omitted for brevity
from posts.models import Posts
from posts.serializers import PostSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from BullbearyAPI.permissions import IsOwnerOrReadOnly
from rest_framework.response import Response

class PostList(generics.ListCreateAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsOwnerOrReadOnly,)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.views += 1
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)