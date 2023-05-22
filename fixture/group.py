from model.group import Group


class GroupHelper:
    def __init__(self, app):
        self.app = app

    def open_groups_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name("new")) > 0):
            wd.find_element_by_link_text("groups").click()

    def create(self, group):
        wd = self.app.wd
        self.open_groups_page()
        # init group creation
        wd.find_element_by_name("new").click()
        self.fill_group_form(group)
        # submit group creation
        wd.find_element_by_name("submit").click()
        self.return_to_group_page()
        self.group_cache = None

    def return_to_group_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()

    def open_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()

    def delete_first_group(self):
        self.delete_group_by_index(0)

    def select_group_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def delete_group_by_index(self, index):
        wd = self.app.wd
        self.open_groups_page()
        self.select_group_by_index(index)
        # Submit first group
        wd.find_element_by_name("delete").click()
        self.return_to_group_page()
        self.group_cache = None

    def modify_first_group(self, group):
        self.modify_group_by_index(0)

    def modify_group_by_index(self, group, index):
        wd = self.app.wd
        self.open_groups_page()
        # Select first group
        self.select_group_by_index(index)
        # Submit first group
        wd.find_element_by_name("edit").click()
        self.fill_group_form(group)
        # submit group update
        wd.find_element_by_name("update").click()
        self.return_to_group_page()
        self.group_cache = None

    def select_first_group(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def fill_group_form(self, group):
        wd = self.app.wd
        self.change_field_value(field_name="group_name", text=group.name)
        self.change_field_value(field_name="group_header", text=group.header)
        self.change_field_value(field_name="group_footer", text=group.footer)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def count(self):
        wd = self.app.wd
        self.open_groups_page()
        return len(wd.find_elements_by_name("selected[]"))

    group_cache = None

    def get_group_list(self):
        if self.group_cache is None:
            wd = self.app.wd
            self.group_cache = []
            self.open_groups_page()
            for elements in wd.find_elements_by_css_selector("span.group"):
                text = elements.text
                id = elements.find_element_by_name("selected[]").get_attribute("value")
                self.group_cache.append(Group(name=text, id=id))
        return list(self.group_cache)

    def delete_group_by_id(self, id):
        wd = self.app.wd
        self.open_groups_page()
        self.select_group_by_id(id)
        # Submit first group
        wd.find_element_by_name("delete").click()
        self.return_to_group_page()
        self.group_cache = None

    def select_group_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='%s']" % id).click()

    def modify_group_by_id(self, group, id):
        wd = self.app.wd
        self.open_groups_page()
        self.select_group_by_id(id)
        wd.find_element_by_name("edit").click()
        self.fill_group_form(group)
        # submit group update
        wd.find_element_by_name("update").click()
        self.return_to_group_page()
        self.group_cache = None

    def group_change_info(self, old, new):
        wd = self.app.wd
        if new.name:
            old.name = new.name
        if new.header:
            old.header = new.header
        if new.footer:
            old.footer = new.footer
        return old

    def check_ui(self, check_ui , groups_db, group_ui):
        if check_ui:
            def clean(group):
                return Group(id=group.id, name=group.name.strip())
            assert sorted(map(clean, groups_db), key=Group.id_or_max) == sorted(group_ui, key=Group.id_or_max)
