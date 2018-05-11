# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from .models import Book


def search_form(request):
    return render(request, 'books/search_form.html')

def search(request):
    if 'q' in request.GET:
        q = request.GET['q']
        books = Book.objects.filter(title__icontains=q)
        html = []
        for book in books:
            title = book.title
            publisher = book.publisher
            html.append('<tr><td>{0}</td><td>{1}</td></tr>'.format(title,publisher))
        #html = '<table>{0}</table>'.format('\n'.join(html))
        html = '<html><body><table>{0}</table></body></html>'.format('\n'.join(html))
        return HttpResponse(html)
    else:
        return HttpResponse('You submitted an empty form.')
