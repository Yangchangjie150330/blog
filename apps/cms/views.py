#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : yang chang jie 
# @Time    : 2020/5/18 17:31

from flask import Blueprint, render_template, request, redirect, session, url_for, g
from flask.views import MethodView
from .forms import LoginForm
from .models import CMSUser

from .decorators import login_required
import config

bp = Blueprint("cms", __name__, url_prefix="/cms")


@bp.route("/")
@login_required
def index():
    """cms首页显示
    """
    return render_template("cms/cms_index.html")

class CMSLoginView(MethodView):
    """
    注册登录
    """

    def get(self, message=None):
        return render_template("cms/cms_login.html", message=message)

    def post(self):
        print(request.form)
        form = LoginForm(request.form)
        result = form.validate()
        if result:
            email = form.email.data
            password = form.password.data
            remember = form.remember.data
            print(email, password, remember)
            user = CMSUser.query.filter_by(email=email).first()
            if user and user.check_password(password):
                session[config.CMS_USER_ID] = user.id
                if remember:  # cookie存储的时间比较长 过期时间为31天
                    session.permanent = True
                return redirect(url_for("cms.index"))
            else:
                errinfo = form.errors
                print(errinfo)
                return self.get(message=errinfo)

        else:
            errinfo = form.errors.popitem()[1][0]
            return self.get(message=errinfo)

class CMSLogoutView(MethodView):
    """注销用户
    """
    def get(self):
        del session[config.CMS_USER_ID]
        return redirect(url_for("cms.cms_login"))

class CMSProfileView(MethodView):
    def get(self):
        pass

    def post(self):
        pass



bp.add_url_rule("/login", endpoint="cms_login", view_func=CMSLoginView.as_view("cms_login"))
bp.add_url_rule("/logout", endpoint="cms_logout", view_func=CMSLogoutView.as_view("cms_logout"))
bp.add_url_rule("/profile", endpoint="cms_profilet", view_func=CMSProfileView.as_view("cms_profilet"))
