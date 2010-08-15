from django import forms

from django.contib.auth.models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields(
            'username',
            'first_name',
            'last_name',
            'password',
            'email'
        )
