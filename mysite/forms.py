# -*- coding: utf-8 -*-

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100,label='主题')
    email = forms.EmailField(required=False, label='你的邮箱地址')
    message = forms.CharField(widget=forms.Textarea,label='信息')

    def clean_message(self):
        message = self.cleaned_data['message']
        num_words = len(message.split())
        if num_words < 4:
            raise forms.ValidationError("Not engough words!")
        return message

class LoginForm(forms.Form):
    username = forms.CharField(max_length=10,label='用户名')
    password = forms.CharField(max_length=20, label='密码')

    def clean_username(self):
        username = self.cleaned_data['username']
        num_char = len(username)
        if num_char < 4:
            raise forms.ValidationError("username must has at least 4 charactors!")
        return username

    def clean_password(self):
        password = self.cleaned_data['password']
        num_char = len(password)
        if num_char < 4:
            raise forms.ValidationError("Password must at least 4 charactors!")
        return password

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30,required=False,help_text='Optional.')
    last_name = forms.CharField(max_length=30,required=False,help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required.Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','password1','password2',)
