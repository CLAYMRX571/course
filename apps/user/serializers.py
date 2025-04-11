from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import CustomUser

class UserSerializers(serializers.ModelSerializer):
    password_reset = serializers.CharField(write_only=True, required=False)
    password = serializers.CharField(write_only=True)
    image = serializers.ImageField(required=False)
    role = serializers.CharField(required=False)

    class Meta:
        model = CustomUser
        fields = '__all__'

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return CustomUser.objects.create(**validated_data)