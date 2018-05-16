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

urlpatterns = [
    url(r'^$',TemplateView.as_view(template_name='home.html'),name='home'),
    url(r'^my_login/$',views.my_view),
    url(r'^login/$',auth_views.login,{'template_name':'login.html'},name='login'),
    url(r'^logout/$',auth_views.logout,{'template_name':'logout.html','next_page': '/'},name='logout'),
    url(r'^admin/', admin.site.urls),
    url(r'^hello/$',views.hello),
    url(r'^time/$', views.current_datetime),
    url(r'^time/plus/(\d{1,2})/$', views.hours_ahead),
    url(r'^meta/$', views.display_meta),
    url(r'^contact/$',views.contact),
    url(r'^contact/thanks/$',views.contact_thanks),
    url(r'^', include('books.urls')),
]
