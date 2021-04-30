#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: urls.py
@time: 2021/4/30 06:53
@desc: 
"""
from django.urls import path, re_path, include
from rest_framework import renderers
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns

from snippets import views

# urlpatterns = [
#     # 使用根路由
#     path('', views.api_root),
#     # 为高亮代码片段添加一个url模式
#     path('snippets/<int:pk>/highlight/', views.SnippetHighlight.as_view()),
#     # # 使用函数装饰器
#     # path('snippets/', views.snippet_list),
#     # path('snippets/<int:pk>/', views.snippet_detail),
#     # 使用基于类的视图
#     path('snippets/', views.SnippetList.as_view()),
#     path('snippets/<int:pk>/', views.SnippetsDetail.as_view()),
#     path('users/', views.UserList.as_view()),
#     path('users/<int:pk>/', views.UserDetail.as_view()),
#
# ]
# urlpatterns = format_suffix_patterns(urlpatterns)

# # API endpoints
# urlpatterns = format_suffix_patterns([
#     re_path(r'^$', views.api_root),
#     re_path(r'^snippets/$',
#             views.SnippetList.as_view(),
#             name='snippet-list'),
#     re_path(r'^snippets/(?P<pk>[0-9]+)/$',
#             views.SnippetDetail.as_view(),
#             name='snippet-detail'),
#     re_path(r'^snippets/(?P<pk>[0-9]+)/highlight/$',
#             views.SnippetHighlight.as_view(),
#             name='snippet-highlight'),
#     re_path(r'^users/$',
#             views.UserList.as_view(),
#             name='user-list'),
#     re_path(r'^users/(?P<pk>[0-9]+)/$',
#             views.UserDetail.as_view(),
#             name='user-detail')
# ])
#
# # 可浏览API的登录和注销视图
# urlpatterns += [
#     re_path(r'^api-auth/', include('rest_framework.urls',
#                                    namespace='rest_framework')),
# ]
# from snippets.views import UserViewSet, SnippetViewSet, api_root
#
# snippet_list = SnippetViewSet.as_view({
#     'get': 'list',
#     'post': 'create'
# })
# snippet_detail = SnippetViewSet.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy'
# })
# snippet_highlight = SnippetViewSet.as_view({
#     'get': 'highlight'
# }, renderer_classes=[renderers.StaticHTMLRenderer])
# user_list = UserViewSet.as_view({
#     'get': 'list'
# })
# user_detail = UserViewSet.as_view({
#     'get': 'retrieve'
# })
#
# urlpatterns = format_suffix_patterns([
#     re_path(r'^$', api_root),
#     re_path(r'^snippets/$', snippet_list, name='snippet-list'),
#     re_path(r'^snippets/(?P<pk>[0-9]+)/$', snippet_detail, name='snippet-detail'),
#     re_path(r'^snippets/(?P<pk>[0-9]+)/highlight/$', snippet_highlight, name='snippet-highlight'),
#     re_path(r'^users/$', user_list, name='user-list'),
#     re_path(r'^users/(?P<pk>[0-9]+)/$', user_detail, name='user-detail')
# ])

# 创建路由器并注册我们的视图
router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet)
router.register(r'users', views.UserViewSet)

# API URL现在由路由器自动确定。
# 另外，我们还要包含可浏览的API的登录URL。
urlpatterns = [
    re_path(r'^', include(router.urls)),
    re_path(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
