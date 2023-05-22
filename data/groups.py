from model.group import Group
import random
import string

testdata = [
    Group(name="name1", header="header1", footer="footer1"),
    Group(name="name2", header="header2", footer="footer2")
]

# def random_str(prefix, maxlen):
#     symbols = string.ascii_letters + string.digits
#     return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])
#
#
# group_data = [
#     Group(name=name, footer=footer, header=header)
#     for name in ["", random_str("name", 10)]
#     for footer in ["", random_str("footer", 25)]
#     for header in ["", random_str("name", 25)]
# ]