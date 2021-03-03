from django.shortcuts import render

# Create your views here.
from comments.models import Comments
from comments.serializers import CommentSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly
from BullbearyAPI.permissions import IsOwnerOrReadOnly
from rest_framework.response import Response
import operator


class CommentList(generics.ListCreateAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    # Customise to get comments based on post id, 
    # for example localhost:8080/comments/?postid=1
    def get_queryset(self):
        queryset = Comments.objects.all()

        # Getting query param and initialise it
        filter_value = self.request.query_params.get('postid', None)

        # Filtering the query param from db result
        if filter_value is not None:
            queryset = queryset.filter(post_id=filter_value)

        # Sorting the result
        for comment in queryset:
            if comment.parent_id is not None:
                comment.newid = float(str(comment.parent_id)+"."+str(comment.id))
            else:
                comment.newid = float(str(comment.id)+".0")
        queryset = sorted(queryset, key=operator.attrgetter('newid'))
        
        return queryset

class CommentDetail(generics.CreateAPIView, generics.RetrieveUpdateDestroyAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]
                          
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)