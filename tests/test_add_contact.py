# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string


def random_str(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " " * 10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


contact_data = [
    Contact(firstname=firstname, middlename=middlename, lastname=lastname)
    for firstname in ["", random_str("firstname", 10)]
    for middlename in ["", random_str("middlename", 10)]
    for lastname in ["", random_str("lastname", 10)]
]


@pytest.mark.parametrize("contact", contact_data, ids=[repr(x) for x in contact_data])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
