from django import forms

from django.contrib.auth.models import User

class UserForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput)
    username = forms.CharField(max_length=155)

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'password',
            'email'
        )
