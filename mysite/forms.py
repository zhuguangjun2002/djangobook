# -*- coding: utf-8 -*-

from django import forms

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
