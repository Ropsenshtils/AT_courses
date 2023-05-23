from model.contact import Contact
from model.group import Group
import random
from fixture.orm import ORMFixture


def test_add_contact_to_group(app, orm, db):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    group = random.choice(db.get_group_list())
    if len(orm.get_contacts_not_in_group(group)) == 0:
        app.contact.create(Contact(firstname="test"))
    contact = random.choice(orm.get_contacts_not_in_group(group))
    app.contact.add_contact_to_group(contact, group)
    assert contact in orm.get_contacts_in_group(group)

def test_remove_contact_from_group(app, orm, db):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    group = random.choice(db.get_group_list())
    if len(orm.get_contacts_in_group(group)) != 0:
        contact=random.choice(orm.get_contacts_in_group(group))
    elif len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="test"))
        contact=random.choice(db.get_contact_list())
        app.contact.add_contact_to_group(contact, group)
    else:
        contact = random.choice(db.get_contact_list())
        app.contact.add_contact_to_group(contact, group)

    app.contact.remove_from_group(contact, group)
    assert contact not in orm.get_contacts_in_group(group)





