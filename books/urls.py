from django.conf.urls import url
from books import views
from books.views import PublisherList,PublisherDetail

urlpatterns = [
    url(r'^search/$', views.search),
    url(r'^publishers/$',PublisherList.as_view()),
    # url(r'^details/(?P<pk>[0-9]+)/$',PublisherDetail.as_view(), name='publisher-detail'),
    # url(r'^details/(?P<pk>[0-9]+)/$', PublisherDetail.as_view(), name='publisher-detail'),
    url(r'^details/(?P<pk>[0-9]+)/$', PublisherDetail.as_view()),
]
