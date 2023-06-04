from django.contrib.auth.forms import PasswordResetForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    mobile_number = forms.CharField(max_length=15, required=True)

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'name', 'email', 'dob', 'mobile_number')

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if CustomUser.objects.filter(username=username).exists():
            raise forms.ValidationError(
                'This username is already taken. Please choose a different one.')
        return username

    def clean_mobile_number(self):
        mobile_number = self.cleaned_data.get('mobile_number')
        if not mobile_number.isdigit():
            raise forms.ValidationError(
                'Mobile number should only contain digits.')
        return mobile_number


class CustomPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(
        label='Email',
        max_length=254,
        widget=forms.EmailInput(
            attrs={'autocomplete': 'email', 'class': 'form-control'})
    )
