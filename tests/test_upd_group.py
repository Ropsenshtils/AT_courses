# -*- coding: utf-8 -*-
from model.group import Group


def test_update_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.update(Group(name="kappa4", header="chino4", footer="blank4"))
    app.session.logout()

