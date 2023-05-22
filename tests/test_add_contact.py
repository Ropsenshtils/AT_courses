from model.contact import Contact


def test_add_contact(app, json_contacts, db, check_ui):
    contact = json_contacts
    old_contacts = db.get_contact_list()
    app.contact.create(contact)
    new_contacts = db.get_contact_list()
    old_contacts.append(contact)
    assert len(old_contacts) == len(new_contacts)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    app.contact.check_ui(check_ui=check_ui, contacts_db=new_contacts, contacts_ui=app.contact.get_contact_list())
