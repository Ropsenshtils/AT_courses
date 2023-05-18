# -*- coding: utf-8 -*-
from model.contact import Contact


def test_update_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test"))
    app.contact.modify_first_contact(Contact(firstname="3kappa", middlename="4middlename", lastname="5lastname"))
