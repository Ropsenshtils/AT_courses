from selenium.webdriver.common.by import By
from model.contact import Contact
import re


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
        if contact.homephone is not None:
            wd.find_element_by_name("home").click()
            wd.find_element_by_name("home").clear()
            wd.find_element_by_name("home").send_keys(contact.homephone)
        if contact.mobilephone is not None:
            wd.find_element_by_name("mobile").click()
            wd.find_element_by_name("mobile").clear()
            wd.find_element_by_name("mobile").send_keys(contact.mobilephone)
        if contact.workphone is not None:
            wd.find_element_by_name("work").click()
            wd.find_element_by_name("work").clear()
            wd.find_element_by_name("work").send_keys(contact.workphone)
        if contact.secondaryphone is not None:
            wd.find_element_by_name("fax").click()
            wd.find_element_by_name("fax").clear()
            wd.find_element_by_name("fax").send_keys(contact.secondaryphone)

    def modify_first_contact(self, contact):
        self.modify_contact_by_index(contact, 0)

    def modify_contact_by_index(self, contact, index):
        wd = self.app.wd
        self.open_contact_edit(index)
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
        if self.group_cache is None:
            wd = self.app.wd
            table = "maintable"
            self.contact_cache = []
            self.open_home_page()
            for row in range(2, len(wd.find_elements_by_xpath("//*[@id='maintable']/tbody/tr")) + 1):
                id = wd.find_element_by_xpath(self.cell_handler(column=1, row=row)).find_element_by_tag_name(
                    "input").get_attribute("value")
                lastname = wd.find_element_by_xpath(self.cell_handler(column=2, row=row)).text
                firstname = wd.find_element_by_xpath(self.cell_handler(column=3, row=row)).text
                addreses = wd.find_element_by_xpath(self.cell_handler(column=4, row=row)).text
                emails = wd.find_element_by_xpath(self.cell_handler(column=5, row=row)).text
                all_phones = wd.find_element_by_xpath(self.cell_handler(column=6, row=row)).text
                self.contact_cache.append(Contact(firstname=firstname, lastname=lastname, id=id, all_phones=all_phones,
                                                      all_addresses=addreses, all_emails=emails))
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

    def open_contact_edit(self, index):
        wd = self.app.wd
        self.open_home_page()
        # update first contact
        wd.find_elements(By.XPATH, '//img[@title="Edit"]')[index].click()

    def get_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_edit(index)
        id = wd.find_element_by_name("id").get_attribute("value")
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        middlename = wd.find_element_by_name("middlename").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        home = wd.find_element_by_name("home").get_attribute("value")
        mobile = wd.find_element_by_name("mobile").get_attribute("value")
        work = wd.find_element_by_name("work").get_attribute("value")
        secondaryphone = wd.find_element_by_name("fax").get_attribute("value")
        addresses = wd.find_element_by_name("address").text
        email1 = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        # all_emails= email1 + "\n" + email2 + "\n" + email3
        # all_phones = home + "\n" + mobile + "\n" + work
        return Contact(firstname=firstname, lastname=lastname, middlename=middlename, id=id, homephone=home,
                       mobilephone=mobile, workphone=work, secondaryphone=secondaryphone, all_addresses=addresses,
                       email1=email1, email2=email2, email3=email3)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        homephone = re.search('H: (.*)', text).group(1)
        workphone = re.search('W: (.*)', text).group(1)
        mobilephone = re.search('M: (.*)', text).group(1)
        secondaryphone = re.search('F: (.*)', text).group(1)
        return Contact(homephone=homephone, mobilephone=mobilephone,
                       workphone=workphone, secondaryphone=secondaryphone)

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_elements(By.XPATH, '//img[@title="Details"]')[index].click()

