# -*- coding: utf-8 -*-
import pytest
from application import Application
from group import Group
from contact import Contact


@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_test_group(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(name="kappa", header="chino", footer="blank"))
    app.logout()


def test_add_contact(app):
    app.login(username="admin", password="secret")
    app.create_contact(Contact(firstname="kappa", middlename="middlename", lastname="lastname"))
    app.logout()


def test_add_empty_group(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(name="", header="", footer=""))
    app.logout()
