from rest_framework import serializers
from .models import User


class SignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name', 'email', 'password']

    email = serializers.EmailField(
        required=True,
        write_only=True,
        max_length=255,
    )

    password = serializers.CharField(
        required=True,
        write_only=True,
    )

    name = serializers.CharField(
        required=True,
    )

    def save(self, **kwargs):
        user = super().save()
        user.email = self.validated_data['email']
        user.name = self.validated_data['email']
        user.set_password(self.validated_data['password'])
        user.save()
        return user

    def validate(self, data):
        email = data.get('email', None)

        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError("user already exists")

        return data

class LoginSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = User
        fields = ['email', 'password']

    email = serializers.EmailField(
        required=True,
        write_only=True,
        max_length=255,
    )

    password = serializers.CharField(
        required=True,
        write_only=True,
    )

    def validate(self, data):

        email = data.get('email', None)
        password = data.get('password', None)

        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)

            if not user.check_password(password):
                raise "비밀번호가 틀립니다"

        else:
            raise "해당 이메일이 존재하지 않습니다."

        return data