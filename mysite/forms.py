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
