#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : yang chang jie 
# @Time    : 2020/5/18 17:29
import os

DEBUG = True

#######################数据库相关设置####################################
HOSTNAME = "127.0.0.1"
USERNAME = "root"
DATABASE = "blog"
PORT = "3306"
PASSWORD = "Ycj123456"
DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}'.format(USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE)

SQLALCHEMY_DATABASE_URI = DB_URI

SQLALCHEMY_TRACK_MODIFICATIONS = False

#######################session####################################
SECRET_KEY = os.urandom(10)  # session 设置key
CMS_USER_ID = "AQWERTYUIOP@#$%%"
