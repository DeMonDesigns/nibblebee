from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.validators import UnicodeUsernameValidator

username_validator = UnicodeUsernameValidator()

class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=150, validators=[username_validator], required=False)
    first_name = forms.CharField(max_length=50, required=True)
    last_name = forms.CharField(max_length=50, required=False)
    email = forms.EmailField(max_length=255, required=True)
    agree = forms.CharField(max_length=50, required=True, error_messages={'required': 'You have not agreed to terms and conditions.'})

    # def clean_agree(self):
    #     data = self.clean_data['agree']
    #     if data != 'agree':
    #         raise forms.ValidationError('You have not agreed to terms and conditions.')
    #     return data

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'agree')

class LoginForm(AuthenticationForm):
    # username = forms.CharField(max_length=150, required=False)
    email = forms.CharField(max_length=255, required=True)
    password = forms.CharField(max_length=30, required=True, widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email', 'password')
