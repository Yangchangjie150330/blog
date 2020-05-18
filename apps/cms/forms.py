#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : yang chang jie 
# @Time    : 2020/5/18 17:32

from wtforms import Form, StringField, PasswordField, IntegerField
from wtforms.validators import Email, InputRequired, Length


class LoginForm(Form):
    email = StringField(validators=[Email(message="你输入的邮箱格式错误"), InputRequired(message="请输入邮箱")])
    password = PasswordField(validators=[Length(4, 12, message="密码的长度在4-12位之间"), ])
    remember = IntegerField()
