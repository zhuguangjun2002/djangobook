# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

from .models import Publisher, Author, Book

import sys;

# add for support unicode in python2.7
reload(sys);
sys.setdefaultencoding("utf8")

admin.site.register(Publisher)
admin.site.register(Author)
admin.site.register(Book)
