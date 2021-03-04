# code omitted for brevity
from rest_framework import serializers
from django.contrib.auth.models import User
from comments.models import Comments
from votes.models import Votes
from votes.serializers import VoteSerializer

class CommentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    votes = VoteSerializer(many=True, read_only=True)

    class Meta:
        model = Comments
        fields = ['id', 'body', 'owner', 'post', 'parent', 'created', 'votes']