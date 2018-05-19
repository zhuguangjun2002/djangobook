from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254,help_text='Required.Inform a valid email address.')
    birth_date = forms.DateField(help_text='Required.Format: YYYY-MM-DD')

    class Meta:
        model = User
        #fields = ('username','birth_date','password1','password2',)
        fields = ('username','email','birth_date','password1','password2',)

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name','last_name','email')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio','location','birth_date','role')
