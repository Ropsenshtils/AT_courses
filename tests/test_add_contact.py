# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(firstname="kappa", middlename="middlename", lastname="lastname"))
    app.session.logout()
