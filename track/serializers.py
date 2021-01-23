from rest_framework import serializers
from core.models import Track
import json


class TrackSerializer(serializers.ModelSerializer):
    """Serializer for Tag objects"""
    locations = serializers.JSONField()

    class Meta:
        model = Track
        fields = ('name', 'locations')
        # fields = 'email'
