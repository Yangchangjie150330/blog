#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : yang chang jie 
# @Time    : 2020/5/18 23:40

from flask import session, redirect, url_for
from functools import wraps
import config


def login_required(func):
    @wraps(func)
    def inner(*args, **kwargs):
        if config.CMS_USER_ID in session:  # 判断user_id是否在session中 存在就是的登录过
            return func(*args, **kwargs)
        else:
            return redirect(url_for("cms.cms_login"))
    return inner
