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

# 覆盖`get_queryset`方法
from django.shortcuts import get_object_or_404

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
    #model = Publisher
    queryset = Publisher.objects.order_by('city')
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

class BookList(ListView):
    queryset = Book.objects.order_by('-publication_date')
    context_object_name = 'book_list'

# 航空工业出版商的图书列表
class AirchinaBookList(ListView):
    context_object_name = 'book_list'
    queryset = Book.objects.filter(publisher__name='航空工业出版社')
    template_name = 'books/airchina_list.html'

class PublisherBookList(ListView):
    template_name = 'books/books_by_publisher.html'

    def get_queryset(self):
        self.publisher = get_object_or_404(Publisher,name=self.args[0])
        return Book.objects.filter(publisher=self.publisher)

    def get_context_data(self, **kwargs):
        # Call the base implementaion first to get a context
        context = super(PublisherBookList,self).get_context_data(**kwargs)
        # Add in the publisher
        context['publisher'] = self.publisher
        return context ## Perform Extra Work
