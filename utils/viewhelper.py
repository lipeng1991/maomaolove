# coding=utf-8
# create by oldman at 17/7/17
from functools import wraps

from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render


def html_response(tpl):
    def _html_response(fn):
        @wraps(fn)
        def wrapper(request, *args, **kwargs):
            try:
                data = fn(request, *args, **kwargs)
                if isinstance(data, HttpResponse):
                    return data
                return render(request, tpl, data)
            except:

                raise
        return wrapper
    return _html_response


def html_response_header(tpl, header_dic):
    def _html_response(fn):
        @wraps(fn)
        def wrapper(request, *args, **kwargs):
            try:
                data = fn(request, *args, **kwargs)
                if isinstance(data, HttpResponse):
                    return data
                resp = render(request, tpl, data)
                if isinstance(header_dic, dict):
                    for key, value in header_dic.items():
                        resp[key] = value
                return resp
            except:
                raise

        return wrapper

    return _html_response


def json_response(fn):
    @wraps(fn)
    def wrapper(request, *args, **kwargs):
        try:
            data = fn(request, *args, **kwargs)
        except Exception as e:
            data = {
                'status': 'fail',
            }
        return JsonResponse(data, safe=False)

    return wrapper