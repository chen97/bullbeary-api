from tags.models import Tags
from rest_framework import serializers

class TagSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    posts = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Tags
        fields = ['id', 'name', 'owner', 'posts']
