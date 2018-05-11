# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from .models import Book

def search(request):
    error= False
    if 'q' in request.GET:
        q = request.GET['q']
        if not q :
            error = True
        else:
            books = Book.objects.filter(title__icontains=q)
            return render(request, 'books/search_results.html',
                          {'books': books, 'query': q})
    return render(request,'books/search_form.html',{'error':error})
