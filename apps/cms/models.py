#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : yang chang jie 
# @Time    : 2020/5/18 17:31
from datetime import datetime
from werkzeug.security import check_password_hash, generate_password_hash
from exts import db


class CMSUser(db.Model):
    __tablename__ = "cms_user"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), nullable=False)
    _password = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)
    join_time = db.Column(db.DateTime, default=datetime.now)

    def __init__(self, username, password, email):
        self.password = password
        self.email = email
        self.username = username

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, raw_password):
        # generate_password_hash对密码进行加密
        self._password = generate_password_hash(raw_password)

    # 验证密码是否相等
    def check_password(self, raw_password):
        return check_password_hash(self.password, raw_password)
