from django import forms
from django.core.exceptions import ValidationError

from account_module.models import User


class LoginForm(forms.Form):
    email = forms.EmailField(label='Email', widget=forms.EmailInput())
    password = forms.CharField(widget=forms.PasswordInput(), label='PassWord')


class RegisterForm(forms.Form):
    email = forms.EmailField(label='Email', widget=forms.EmailInput())
    password = forms.CharField(widget=forms.PasswordInput(), label='Password')
    password1 = forms.CharField(widget=forms.PasswordInput(), label='Password Confirmation')

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password1 = cleaned_data.get("password1")
        if password != password1:
            return forms.ValidationError("Passwords did NOT match!!!")
        return cleaned_data


class UserCreateForm(forms.Form):
    full_name = forms.CharField(
        label='Name',
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Name"})
    )

    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(attrs={"class": "form-control", "placeholder": "Email"})
    )
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Password"})
    )
    is_superuser = forms.BooleanField(
        label='Admin Access',
        widget=forms.CheckboxInput(attrs={"class": "form-check-input"}),
        required=False
    )


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["full_name", "email", "password",]
        widgets = {
            "full_name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Name"}),
            "email": forms.EmailInput(attrs={"class": "form-control", "placeholder": "Email"}),
            "password": forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Password"}),
        }
        labels = {
            "full_name": "Name",
            "email": 'Email',
            "password": 'Password',
        }

    def __init__(self, *args, **kwargs):
        # first call parent's constructor
        super(UserEditForm, self).__init__(*args, **kwargs)
        # there's a `fields` property now
        self.fields['full_name'].required = False
        self.fields['email'].required = False
        self.fields['password'].required = False
