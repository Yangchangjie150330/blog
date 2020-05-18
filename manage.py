#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : yang chang jie 
# @Time    : 2020/5/18 18:01


from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from server import app
from exts import db
from apps.cms import models as cms_models

CMSUSer = cms_models.CMSUser

manager = Manager(app)
db.init_app(app)
Migrate(app, db)
manager.add_command("db", MigrateCommand)


@manager.option("-u", "--username", dest="username")
@manager.option("-p", "--password", dest="password")
@manager.option("-e", "--email", dest="email")
def create_user(username, password, email):
    user = CMSUSer(username=username, password=password, email=email)
    db.session.add(user)
    db.session.commit()
    print("cms添加用户的成功")


if __name__ == '__main__':
    manager.run()
