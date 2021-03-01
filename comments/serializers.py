# code omitted for brevity
from comments.models import Comments
from rest_framework import serializers
from django.contrib.auth.models import User

class CommentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Comments
        fields = ['id', 'body', 'owner', 'post', 'parent', 'created']