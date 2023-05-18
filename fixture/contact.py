from selenium.webdriver.common.by import By


class ContactHelper:
    def __init__(self, app):
        self.app = app

    def create(self, contact):
        wd = self.app.wd
        # init contact creation
        wd.find_element_by_link_text("add new").click()
        # fill contact firm
        self.fill_firm(contact)
        # submit contact creation
        wd.find_element_by_name("submit").click()

    def delete_first_contact(self):
        wd = self.app.wd
        self.open_home_page()
        # Select first contact
        wd.find_element_by_name("selected[]").click()
        # Submit first contact
        wd.find_element(By.XPATH, '//input[@value="Delete"]').click()
        wd.switch_to.alert.accept()
        # wd.find_element_by_xpath('//input[@value="Delete"]')

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
        wd = self.app.wd
        self.open_home_page()
        # update first contact
        wd.find_element(By.XPATH, '//img[@title="Edit"]').click()
        # fill contact firm
        self.fill_firm(contact)
        # submit contact creation
        wd.find_element_by_name("update").click()

    def count(self):
        wd = self.app.wd
        self.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    def open_home_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/") & len(wd.find_elements_by_link_text("add new")) > 0):
            wd.find_element_by_link_text("home").click()
