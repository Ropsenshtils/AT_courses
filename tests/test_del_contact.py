from model.contact import Contact


def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test"))
    old_contacts = app.contact.get_contact_list()
    app.contact.delete_first_contact()
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts[0:1] = []
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_click_contact(app):
    wd = app.wd
    app.contact.open_home_page()
    table = "maintable"
    row = 2
    # wd.find_element_by_xpath(app.contact.cell_handler(table=table, column=1, row=row)).find_element_by_tag_name(
    #     "input").get_attribute("value")
    wd.find_element_by_xpath(app.contact.cell_handler(table=table, column=1, row=row)).click()
    wd.find_element_by_xpath('//input[@value="Delete"]').click()
    wd.switch_to.alert.accept()
