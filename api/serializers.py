from rest_framework import serializers
from .models import Users, Books
from django.contrib.auth.hashers import make_password


class UsersSerializers(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('id', 'username', 'password','is_admin', 'is_users')
        write_only_fields = ('password',)


class BooksSerializers(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = ('id', 'book', 'rating')