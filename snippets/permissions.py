#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: permissions.py
@time: 2021/4/30 11:44
@desc: 
"""
from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    自定义权限只允许对象的所有者编辑它。
    """

    def has_object_permission(self, request, view, obj):
        # 读取权限允许任何请求
        # 所以我们总是允许GET,HEAD,或OPTIONS请求。
        if request.method in permissions.SAFE_METHODS:
            return True

        # 只有该snippet 的所有者才允许写权限
        return obj.owner == request.user
