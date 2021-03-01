from django.shortcuts import render

# Create your views here.
from comments.models import Comments
from comments.serializers import CommentSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly
from BullbearyAPI.permissions import IsOwnerOrReadOnly
from rest_framework.response import Response
from rest_framework import mixins, views

class CommentList(generics.ListCreateAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        queryset = Comments.objects.all()
        filter_value = self.request.query_params.get('postid', None)
        if filter_value is not None:
            queryset = queryset.filter(post_id=filter_value)
        return queryset

class CommentDetail(generics.CreateAPIView, generics.RetrieveUpdateDestroyAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]
                          
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)