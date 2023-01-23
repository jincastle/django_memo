from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from rest_framework_simplejwt.tokens import RefreshToken


# Create your models here.
class User(AbstractUser, PermissionsMixin):

    class Meta:
        db_table = 'user'

    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)

    def generate_token(self):
        token = RefreshToken.for_user(self)
        refresh = str(token)
        access = str(token.access_token)
        return {'access': access, 'refresh': refresh}

    def __str__(self):
        return "{}({})".format(self.name, self.email)