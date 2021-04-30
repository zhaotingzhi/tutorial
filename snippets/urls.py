#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: urls.py
@time: 2021/4/30 06:53
@desc: 
"""
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from snippets import views

urlpatterns = [
    # # 使用函数装饰器
    # path('snippets/', views.snippet_list),
    # path('snippets/<int:pk>/', views.snippet_detail),
    # 使用基于类的视图
    path('snippets/', views.SnippetList.as_view()),
    path('snippets/<int:pk>/', views.SnippetsDetail.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)
