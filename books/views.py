# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from .models import Book

# define a listview
from django.views.generic import ListView
from books.models import Publisher

# define a detailview
from django.views.generic import DetailView

def search(request):
    errors= []
    if 'q' in request.GET:
        q = request.GET['q']
        if not q :
            errors.append('Enter a search term.')
        elif len(q) > 20:
            errors.append('Please enter at most 20 characters.')
        else:
            books = Book.objects.filter(title__icontains=q)
            return render(request, 'books/search_results.html',
                          {'books': books, 'query': q})
    return render(request,'books/search_form.html',{'errors':errors})

class PublisherList(ListView):
    model = Publisher
    context_object_name = 'my_favorite_publishers'

class PublisherDetail(DetailView):
    model = Publisher
    # pk_url_kward = 'id'
    # tempalte_name = 'books/publisher_detail.html'

    # def get_context_data(self, **kwargs):
        # # Call the base implementaion first to get a context
        # context = super(PublisherDetail,self).get_context_data(**kwargs)
        # # Add in a QuerySet of all the books
        # #context['book_list'] = Book.objects.all()
        # return context
