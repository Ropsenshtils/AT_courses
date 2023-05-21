# -*- coding: utf-8 -*-
from model.contact import Contact


def test_update_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test"))
    contact = Contact(firstname="3kappa", middlename="4middlename", lastname="5lastname")
    old_contacts = app.contact.get_contact_list()
    app.contact.modify_first_contact(contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
