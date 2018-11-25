from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserChangeForm
from django.utils import timezone
from .models import bio
from django.core.exceptions import ValidationError


class loginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    
class userRegisterForm(UserCreationForm):
    password1 = forms.CharField(label="Password",widget=forms.PasswordInput)
    password2 = forms.CharField(label="Password Confirmation", widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password1','password2']
        
    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if User.objects.filter(email=email).exclude(username=username):
            raise forms.ValidationError(u'Email already been used')
        return email
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        
        if not password1 or not password2:
            raise forms.ValidationError(u'please confrim your password')
        if password1 != password2:
            raise forms.ValidationError(u'Password must match')
            
        return password2

class editProfile(UserChangeForm):
    class Meta:
        model = User
        fields = ['email','username','first_name','last_name','password']

class bio_and_image(forms.Form):
    class Meta:
        model = bio
        fields = ['image']
    
    
        