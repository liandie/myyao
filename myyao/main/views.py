#!/usr/bin/env python
# encoding: utf-8
"""
@version: python3.6.5
@author: myyao
@license: python
@contact: longzinziyan@gmail.com
@software: PyCharm
@file: views.py
@time: 2018/4/13 20:37
"""

from django.shortcuts import render


def girl(request):
    return render(request, 'girl.html')

def boy(request):
    return render(request, 'boy.html')

def blog1(request):
    return render(request, 'blog1/index.html')

def blog1_share(request):
    return render(request, 'blog1/share.html')

def blog1_list(request):
    return render(request, 'blog1/list.html')

def blog1_about(request):
    return render(request, 'blog1/about.html')

def blog1_gbook(request):
    return render(request, 'blog1/gbook.html')

def blog1_info(request):
    return render(request, 'blog1/info.html')

def blog1_infopic(request):
    return render(request, 'blog1/infopic.html')

def blog2(request):
    return render(request, 'blog2/index.html')