"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from . import views

# How to Use Django's Built-in Login System
# By Vitor Freitas
# https://simpleisbetterthancomplex.com/tutorial/2016/06/27/how-to-use-djangos-built-in-login-system.html
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView

# use core app 's `signup` 
from core import views as core_views

# add `django-debug-toolbar`
from django.conf import settings
from django.conf.urls import include, url

urlpatterns = [
    url(r'^mhome/$',TemplateView.as_view(template_name='mhome.html'),name='mhome'),
    url(r'^mlogin/$',views.my_view,name='mlogin'),
    url(r'^mlogout/$',views.logout_view,name='mlogout'),
    #url(r'^$',TemplateView.as_view(template_name='home.html'),name='home'),
    url(r'^$', core_views.home, name='home'),
    url(r'^signup/$', core_views.signup, name='signup'),
    url(r'^profile_detail/$', core_views.profile_detail, name='profile_detail'),
    url(r'^update_profile/$', core_views.update_profile, name='update_profile'),
    url(r'^login/$',auth_views.login,{'template_name':'login.html'},name='login'),
    url(r'^logout/$',auth_views.logout,{'template_name':'logout.html','next_page': '/'},name='logout'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
           core_views.activate, name='activate'),
    url(r'^account_activation_sent/$', core_views.account_activation_sent, name='account_activation_sent'),
    url(r'^password_reset/$',auth_views.password_reset,name='password_reset'),
    url(r'^password_reset_done/$',auth_views.password_reset_done,name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',auth_views.password_reset_confirm, name='password_reset_confirm'),
    url(r'^reset/done/$', auth_views.password_reset_complete, name='password_reset_complete'),
    url(r'^admin/', admin.site.urls),
    url(r'^hello/$',views.hello),
    url(r'^time/$', views.current_datetime),
    url(r'^time/plus/(\d{1,2})/$', views.hours_ahead),
    url(r'^meta/$', views.display_meta),
    url(r'^contact/$',views.contact),
    url(r'^contact/thanks/$',views.contact_thanks),
    url(r'^myimage/$',views.my_image),
    url(r'^mycsv/$',views.my_csv),
    url(r'^', include('books.urls')),
]

if settings.DEBUG:
   import debug_toolbar
   urlpatterns += [
       url(r'^__debug__/', include(debug_toolbar.urls)),
   ]
