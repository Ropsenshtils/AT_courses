# -*- coding: utf-8 -*-
from model.contact import Contact


def test_update_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.update(Contact(firstname="2kappa", middlename="2middlename", lastname="2lastname"))
    app.session.logout()
