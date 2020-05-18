#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : yang chang jie 
# @Time    : 2020/5/18 17:31

from flask import Blueprint

bp = Blueprint("common", __name__, url_prefix="/common")


@bp.route("/")
def index():
    return "common index"
