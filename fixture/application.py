from selenium import webdriver
from selenium.webdriver.firefox.options import Options

from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper


class Application:
    def __init__(self):
        # расположение firefox отличается от дефолтного(?)
        options = Options()
        options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'

        self.wd = webdriver.Firefox(options=options)
        self.wd.implicitly_wait(30)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)


    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def destroy(self):
        self.wd.quit()
