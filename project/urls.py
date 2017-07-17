# coding=utf-8
# create by oldman at 17/7/17
from django.conf.urls import url
from django.views.generic import TemplateView

from project.view import index

project_urls = [
    url(r'index/$', index, name='index'),
]
