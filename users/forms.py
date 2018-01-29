from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django.contrib.auth.models import User
from django.contrib.auth.validators import UnicodeUsernameValidator

from .models import UserProfile

username_validator = UnicodeUsernameValidator()

class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=150, validators=[username_validator], required=True)
    first_name = forms.CharField(max_length=50, required=True)
    last_name = forms.CharField(max_length=50, required=False)
    email = forms.EmailField(max_length=255, required=True)
    agree = forms.CharField(max_length=50, required=True, error_messages={
        'required': 'You have not agreed to terms and conditions.'
    })

    def clean_agree(self):
        data = self.clean()['agree']
        if data != 'agree':
            raise forms.ValidationError('You have not agreed to terms and conditions')
        return data

    def clean_email(self):
        email = self.clean()['email']
        try:
            match = User.objects.get(email=email)
        except User.DoesNotExist:
            return email
        raise forms.ValidationError('This email is already in use')

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

# class EditProfileForm(UserChangeForm):
#
#     class Meta:
#         model = UserProfile
#         fields = ('bio', 'location', 'sex', 'dob')
#         exclude = ('password',)
#
#     def clean_password(self):
#         return '' #self.initial['password']


class EditProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        f = self.fields.get('user_permissions', None)
        if f is not None:
            f.queryset = f.queryset.select_related('content_type')
