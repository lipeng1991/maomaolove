# coding=utf-8
# create by oldman at 17/7/17
from django.conf.urls import url

from project.view import index

project_urls = [
    url(r'index/$', index, name='index')
]
