from django.shortcuts import render

# Create your views here.
from votes.models import Votes
from votes.serializers import VoteSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from BullbearyAPI.permissions import IsOwnerOrReadOnly
from rest_framework.response import Response

class VoteList(generics.ListCreateAPIView):
    queryset = Votes.objects.all()
    serializer_class = VoteSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(vote_sender=self.request.user)

class VoteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Votes.objects.all()
    serializer_class = VoteSerializer
    permission_classes = (IsOwnerOrReadOnly,)
