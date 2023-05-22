# -*- coding: utf-8 -*-
from model.contact import Contact
from random import randrange
import random

def test_update_some_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test"))
    contact = Contact(firstname="3kappa", middlename="4middlename", lastname="5lastname")
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact.id = old_contacts[index].id
    app.contact.modify_contact_by_index(contact, index)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

def test_update_some_contact_2(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="test"))
    new_contact = Contact(firstname="Нашевся", middlename="4middlename", lastname="5lastname")
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    contact = app.contact.contact_change_info(contact, new_contact)
    app.contact.modify_contact_by_id(contact, contact.id)
    new_contacts = db.get_contact_list()
    old_contacts[new_contacts.index(contact)] = contact
    assert len(old_contacts) == len(new_contacts)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    app.contact.check_ui(check_ui=check_ui, contacts_db=new_contacts, contacts_ui=app.contact.get_contact_list())
