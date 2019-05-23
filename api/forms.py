from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.forms import ModelForm
from api.models import Users, NormalUSer, Books


class UserSignUpForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = Users

    @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_users = True
        if commit:
            user.save()
        return user


class AdminSignUpForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = Users

    @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_admin = True
        if commit:
            user.save()
        return user


class BookForm(ModelForm):
    class Meta:
        model = Books
        fields = ['book']
