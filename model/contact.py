from sys import maxsize


class Contact:
    def __init__(self, firstname=None, middlename=None, lastname=None, id=None, homephone=None, mobilephone=None,
                 workphone=None, secondaryphone=None, all_phones=None, all_addresses=None, all_emails=None, email1=None,
                 email2=None, email3=None):
        self.id = id
        self.lastname = lastname
        self.firstname = firstname
        self.all_addresses = all_addresses
        self.all_emails = all_emails
        self.email1 = email1
        self.email2 = email2
        self.email3 = email3
        self.all_phones = all_phones
        self.homephone = homephone
        self.mobilephone = mobilephone
        self.workphone = workphone
        self.secondaryphone = secondaryphone
        self.middlename = middlename

    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.firstname, self.lastname)

    def __eq__(self, other):
        return (
                       self.id is None or other.id is None or self.id == other.id) and self.firstname == other.firstname and self.lastname == other.lastname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
