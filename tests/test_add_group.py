# -*- coding: utf-8 -*-
from model.group import Group


def test_add_test_group(app):
    app.group.create(Group(name="1kappa", header="1chino", footer="1blank"))


def test_add_empty_group(app):
    app.group.create(Group(name="", header="", footer=""))
