# code omitted for brevity
from rest_framework import serializers
from votes.models import Votes
from django.contrib.auth.models import User


class VoteSerializer(serializers.ModelSerializer):
    vote_sender = serializers.ReadOnlyField(source='vote_sender.username')

    class Meta:
        model = Votes
        fields = ['id', 'vote_sender', 'up_vote']