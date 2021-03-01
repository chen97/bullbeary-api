# code omitted for brevity
from rest_framework import serializers
from posts.models import Posts
from django.contrib.auth.models import User

class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Posts
        fields = ['id', 'title', 'content', 'owner', 'comments', 'tags', 'views', 'last_edit', 'datetime']

class UserSerializer(serializers.ModelSerializer):
    posts = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    tags = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'posts', 'comments', 'tags']