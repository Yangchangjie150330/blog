#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : yang chang jie 
# @Time    : 2020/5/18 17:28


import config
from flask import Flask, render_template
from front.views import bp as fbp
from apps.cms.views import bp as cbp
from common.views import bp as conp

from exts import db

app = Flask(__name__)

app.config.from_object(config)
app.register_blueprint(fbp)
app.register_blueprint(cbp)
app.register_blueprint(conp)

db.init_app(app)

if __name__ == '__main__':
    app.run()
