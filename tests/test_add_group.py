# -*- coding: utf-8 -*-
import pytest
from fixture.application import Application
from model.group import Group
from model.contact import Contact


@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_test_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="kappa", header="chino", footer="blank"))
    app.session.logout()


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.create_contact(Contact(firstname="kappa", middlename="middlename", lastname="lastname"))
    app.session.logout()


def test_add_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="", header="", footer=""))
    app.session.logout()
