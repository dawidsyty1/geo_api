from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        required=True,
        help_text='Leave empty if no change needed',
        style={'input_type': 'password', 'placeholder': 'Password'}
    )
    email = serializers.EmailField(max_length=50, min_length=5, allow_blank=False)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']

    def create(self, validated_data):
        password = validated_data.pop('password', '')

        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()

        return user
