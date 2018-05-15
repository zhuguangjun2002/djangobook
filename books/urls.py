from django.conf.urls import url
from books import views

urlpatterns = [
    url(r'^search/$', views.search),
    url(r'^publishers/$',views.PublisherList.as_view()),
    # url(r'^details/(?P<pk>[0-9]+)/$',PublisherDetail.as_view(), name='publisher-detail'),
    # url(r'^details/(?P<pk>[0-9]+)/$', PublisherDetail.as_view(), name='publisher-detail'),
    url(r'^details/(?P<pk>[0-9]+)/$', views.PublisherDetail.as_view()),
    url(r'^books/$',views.BookList.as_view()),
    url(r'^airchina/$',views.AirchinaBookList.as_view()),
]
