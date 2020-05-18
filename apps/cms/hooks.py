#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : yang chang jie 
# @Time    : 2020/5/19 0:51

import config
from flask import session, g
from .models import CMSUser
from .views import bp

# g对象绑定用户信息  可以后端和模板中进行使用
@bp.before_request
def before_request():
    if config.CMS_USER_ID in session:
        user_id = session.get(config.CMS_USER_ID)
        user = CMSUser.query.get(user_id)
        if user:
            g.cms_user = user