from rest_framework import serializers
from .models import SocialPost


class SocialPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialPost
        fields = ["id", "title", "body", "author", "created_at"]
        read_only_fields = ["id", "created_at"]


