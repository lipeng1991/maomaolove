# coding=utf-8
# create by oldman at 17/7/17
from utils.viewhelper import html_response

t_dir = 'project/'


@html_response(t_dir + 'index.html')
def index(request):
    pass
