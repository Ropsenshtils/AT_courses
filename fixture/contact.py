from selenium.webdriver.common.by import By
from model.contact import Contact


class ContactHelper:
    def __init__(self, app):
        self.app = app

    def create(self, contact):
        wd = self.app.wd
        self.open_home_page()
        # init contact creation
        wd.find_element_by_link_text("add new").click()
        # fill contact firm
        self.fill_firm(contact)
        # submit contact creation
        wd.find_element_by_name("submit").click()
        self.contact_cache = None

    def delete_first_contact(self):
        wd = self.app.wd
        self.delete_contact_by_index(0)

    def fill_firm(self, contact):
        wd = self.app.wd
        if contact.firstname is not None:
            wd.find_element_by_name("firstname").click()
            wd.find_element_by_name("firstname").clear()
            wd.find_element_by_name("firstname").send_keys(contact.firstname)
        if contact.middlename is not None:
            wd.find_element_by_name("middlename").click()
            wd.find_element_by_name("middlename").clear()
            wd.find_element_by_name("middlename").send_keys(contact.middlename)
        if contact.lastname is not None:
            wd.find_element_by_name("lastname").click()
            wd.find_element_by_name("lastname").clear()
            wd.find_element_by_name("lastname").send_keys(contact.lastname)

    def modify_first_contact(self, contact):
        self.modify_contact_by_index(contact, 0)

    def modify_contact_by_index(self, contact, index):
        wd = self.app.wd
        self.open_home_page()
        # update first contact
        wd.find_elements(By.XPATH, '//img[@title="Edit"]')[index].click()
        # fill contact firm
        self.fill_firm(contact)
        # submit contact creation
        wd.find_element_by_name("update").click()
        self.contact_cache = None

    def count(self):
        wd = self.app.wd
        self.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    def open_home_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/") & len(wd.find_elements_by_link_text("add new")) > 0):
            wd.find_element_by_link_text("home").click()

    def cell_handler(self, column, row):
        table = "maintable"
        cell_xpath = "//*[@id='" + str(table) + "']/tbody/tr[" + str(row) + "]/td[" + str(column) + "]"
        return cell_xpath

    contact_cache = None

    def get_contact_list(self):
        wd = self.app.wd
        table = "maintable"
        self.contact_cache = []
        self.open_home_page()
        for row in range(2, len(wd.find_elements_by_xpath("//*[@id='maintable']/tbody/tr")) + 1):
            id = wd.find_element_by_xpath(self.cell_handler(column=1, row=row)).find_element_by_tag_name(
                "input").get_attribute("value")
            firstname = wd.find_element_by_xpath(self.cell_handler(column=3, row=row)).text
            lastname = wd.find_element_by_xpath(self.cell_handler(column=2, row=row)).text
            self.contact_cache.append(Contact(firstname=firstname, lastname=lastname, id=id))
        return list(self.contact_cache)

    def select_contact_by_index(self, index):
        wd = self.app.wd
        index += 2
        wd.find_element_by_xpath(self.cell_handler(column=1, row=index)).click()

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        # Select first contact
        self.select_contact_by_index(index)
        # Submit first contact
        wd.find_element_by_xpath('//input[@value="Delete"]').click()
        wd.switch_to.alert.accept()
        self.contact_cache = None
