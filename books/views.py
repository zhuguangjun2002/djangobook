# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

def search_form(request):
    return render(request, 'books/search_form.html')
