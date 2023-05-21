import re
from random import randrange

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
