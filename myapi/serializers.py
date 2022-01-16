from rest_framework import serializers
from .models import Profile

class profile_serializer(serializers.ModelSerializer):
    pass
    class Meta:
        model=Profile
        fields='__all__'