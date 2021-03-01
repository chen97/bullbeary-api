from django.shortcuts import render

# Create your views here.
from tags.models import Tags
from tags.serializers import TagSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly
from BullbearyAPI.permissions import IsOwnerOrReadOnly
from rest_framework.response import Response

class TagList(generics.ListCreateAPIView):
    queryset = Tags.objects.all()
    serializer_class = TagSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class TagDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tags.objects.all()