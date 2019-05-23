from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class Users(AbstractUser):
    is_admin = models.BooleanField(default=False)
    is_users = models.BooleanField(default=False)


class NormalUSer(models.Model):
    users = models.OneToOneField(
        Users, on_delete=models.CASCADE, primary_key=True)


class Books(models.Model):
    book = models.CharField(max_length=200)
    rating = models.IntegerField(default=0)

    def __str__(self):
        return self.book
