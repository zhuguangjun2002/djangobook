from django.conf.urls import url
from books import views

urlpatterns = [
    url(r'^search/$', views.search),
    url(r'^publishers/$',views.PublisherList.as_view()),
    url(r'^publishers/(?P<pk>[0-9]+)/$', views.PublisherDetail.as_view(), name='publisher-detail'),
    #url(r'^publishers/(?P<pk>[0-9]+)/$', views.hello_publisher),
    # url(r'^books/$',views.BookList.as_view()),
    url(r'^airchina/$',views.AirchinaBookList.as_view()),
    url(r'^books/([\w-]+)/$',views.PublisherBookList.as_view()),
    url(r'^authors/(?P<pk>[0-9]+)/$', views.AuthorDetailView.as_view(), name='author-detail'),
]
