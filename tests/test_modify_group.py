# -*- coding: utf-8 -*-
from model.group import Group


def test_modify_first_group(app):
    app.group.modify_first_group(Group(name="kappa4", header="chino4", footer="blank4"))


def test_modify_first_group_name(app):
    app.group.modify_first_group(Group(name="kappa4"))


def test_modify_first_group_header(app):
    app.group.modify_first_group(Group(header="chino4"))


def test_modify_first_group_footer(app):
    app.group.modify_first_group(Group(footer="blank4"))
