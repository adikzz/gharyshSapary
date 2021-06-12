from django import forms
from .models import *
from django.forms import (
    TextInput
)


class UsersForm(forms.ModelForm):
    username = forms.CharField(widget=TextInput(), required = True)
    full_name = forms.CharField(widget=TextInput(), required = True)
    password = forms.CharField(widget=TextInput(), required=True)

    class Meta:
        model = Users
        fields = [
            'username',
            'full_name',
            'password',
        ]