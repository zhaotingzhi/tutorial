#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: urls.py
@time: 2021/4/30 06:53
@desc: 
"""
from django.urls import path

from snippets import views

urlpatterns = [
    path('snippets/', views.snippet_list),
    path('snippets/<int:pk>/', views.snippet_detail),
]
