from fixture.orm import ORMFixture
from model.group import Group

db = ORMFixture(host='localhost',
                database='addressbook',
                user='root',
                password='')

try:
    l = db.get_contacts_in_group(Group(id="151"))
    for items in l:
        print(items)
    print(len(l))
finally:
    pass
