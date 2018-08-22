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
from django.conf.urls import url
from .import views 



urlpatterns = [
    url(r'^girl$|^girl/',views.girl,name='girl'),
    url(r'^boy$|^boy/',views.boy,name='boy'),
    url(r'^blog1$',views.blog1,name='blog1'),
    url(r'^blog1_share$',views.blog1_share,name='blog1_share'),
    url(r'^blog1_list$',views.blog1_list,name='blog1_list'),
    url(r'^blog1_about$',views.blog1_about,name='blog1_about'),
    url(r'^blog1_gbook$',views.blog1_gbook,name='blog1_gbook'),
    url(r'^blog1_info$',views.blog1_info,name='blog1_info'),
    url(r'^blog1_infopic$',views.blog1_infopic,name='blog1_infopic'),
]
