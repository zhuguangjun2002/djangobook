# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

from django.db import models

class Publisher(models.Model):
    name = models.CharField(max_length=30,verbose_name='名字')
    address = models.CharField(max_length=50,verbose_name='地址')
    city = models.CharField(max_length=60,verbose_name='城市')
    state_province = models.CharField(max_length=30,verbose_name='省份/直辖市')
    country = models.CharField(max_length=50,verbose_name='国家')
    website = models.URLField(verbose_name='网站')

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name='出版商'
        verbose_name_plural = "出版商"


class Author(models.Model):
    first_name = models.CharField(max_length=30,verbose_name='名')
    last_name = models.CharField(max_length=40,verbose_name='姓')
    email = models.EmailField(blank=True,verbose_name ='电子邮箱')

    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)

    class Meta:
        verbose_name='作家'
        verbose_name_plural = "作家"

class BookManager(models.Manager):
    def title_count(self,keyword):
        return self.filter(title__icontains=keyword).count()

class Book(models.Model):
    title = models.CharField(max_length=100,verbose_name='书名')
    authors = models.ManyToManyField(Author,verbose_name='作者')
    publisher = models.ForeignKey(Publisher,verbose_name='出版商')
    publication_date = models.DateField(blank=True, null=True,verbose_name='出版日期')
    num_pages = models.IntegerField(blank=True,null=True,verbose_name='页数')
    objects = BookManager()

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name='图书'
        verbose_name_plural = "图书"
