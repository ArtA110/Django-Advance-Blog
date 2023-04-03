from rest_framework import serializers
from accounts.models import User, Profile
from django.contrib.auth.password_validation import validate_password
from django.core import exceptions
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class RegistrationSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(max_length=100, write_only=True)

    class Meta:
        model = User
        fields = ["email", "password", "password1"]

    def validate(self, attrs):
        if attrs.get("password") != attrs.get("password1"):
            raise serializers.ValidationError({"password": "passwords doesnt match!"})

        try:
            validate_password(attrs.get("password"))
        except exceptions.ValidationError as e:
            raise serializers.ValidationError({"password": list(e.messages)})
        attrs.pop("password1")
        return super().validate(attrs)

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class CustomTokenOptainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        validated_data = super().validate(attrs)
        validated_data["email"] = self.user.email
        validated_data["user_id"] = self.user.pk
        return validated_data


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
    new_password1 = serializers.CharField(required=True)

    def validate(self, attrs):
        if attrs.get("new_password") != attrs.get("new_password1"):
            raise serializers.ValidationError({"password": "passwords doesnt match!"})

        try:
            validate_password(attrs.get("new_password"))
        except exceptions.ValidationError as e:
            raise serializers.ValidationError({"new_password": list(e.messages)})
        return super().validate(attrs)


class ProfileSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(source="user.email", read_only=True)

    class Meta:
        model = Profile
        fields = [
            "id",
            "email",
            "first_name",
            "last_name",
            "image",
            "description",
        ]


class ResendActivationSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)

    def validate(self, attrs):
        email = attrs.get("email")
        user = User.objects.get(email=email)
        attrs["user"] = user
        return super().validate(attrs)
