# -*- coding: utf-8 -*-
from model.group import Group


def test_add_test_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="kappa", header="chino", footer="blank"))
    app.session.logout()


def test_add_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="", header="", footer=""))
    app.session.logout()
