import re
from random import randrange
from model.contact import Contact


def test_compare_home_page_and_edit(app):
    index = randrange(len(app.contact.get_contact_list()))
    contact_from_home_page = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_info_from_edit_page(index)
    assert contact_from_home_page.id == contact_from_edit_page.id
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname
    assert contact_from_home_page.firstname == contact_from_edit_page.firstname
    assert contact_from_home_page.all_addresses == contact_from_edit_page.all_addresses
    assert contact_from_home_page.all_emails == merge_emails_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.all_phones == merge_phone_like_on_home_page(contact_from_edit_page)


def test_compare_home_page_and_db(app, db):
    contacts_db = sorted(db.get_contact_list(), key=Contact.id_or_max)
    contacts_ui = sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
    emails = list(map(merge_emails_like_on_home_page, contacts_db))
    phones = list(map(merge_phone_like_on_home_page, contacts_db))
    addresses = list(map(addresses_like_on_home_page, contacts_db))
    for i in range(len(contacts_db)):
        assert contacts_ui[i].id == contacts_db[i].id
        assert contacts_ui[i].lastname == contacts_db[i].lastname
        assert contacts_ui[i].firstname == contacts_db[i].firstname
        assert contacts_ui[i].all_addresses == addresses[i]
        assert contacts_ui[i].all_emails == emails[i]
        assert contacts_ui[i].all_phones == phones[i]


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phone_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None, [contact.homephone, contact.mobilephone,
                                                                 contact.workphone]))))


def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            filter(lambda x: x is not None, [contact.email1, contact.email2,
                                                             contact.email3])))


def addresses_like_on_home_page(contact):
    return re.sub("\r", "", contact.all_addresses)
