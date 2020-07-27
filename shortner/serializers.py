from rest_framework import serializers
from .models import TinyURL


class TinyURLSerialzier(serializers.Serializer):
    original_url = serializers.URLField(required=True)
    short_url = serializers.CharField(required=False, read_only=True)

    def create(self, validated_data):
        short_url = TinyURL.objects.create(**validated_data)
        short_url.generate_url_hash()
        return short_url


