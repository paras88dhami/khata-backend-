from rest_framework import serializers
from .models import User


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ("full_name", "email", "phone", "password")

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class LoginSerializer(serializers.Serializer):
    identifier = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        identifier = data.get("identifier")
        password = data.get("password")

        user = (
            User.objects.filter(email=identifier).first()
            or User.objects.filter(phone=identifier).first()
        )

        if not user or not user.check_password(password):
            raise serializers.ValidationError("Invalid credentials")

        return user
