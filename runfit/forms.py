from django import forms
from django.contrib.auth.models import User
from runfit.models import Person, Coach, Order


class UserForm(forms.ModelForm):
    email = forms.CharField(max_length=100, required=True)
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ("username", "password", "first_name", "last_name", "email")


class UserFormForEdit(forms.ModelForm):
    email = forms.CharField(max_length=100, required=True)

    class Meta:
        model = User
        fields = ("first_name", "last_name", "email")


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ("phone", "avatar")


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ("coach", "pick_training", "total")
