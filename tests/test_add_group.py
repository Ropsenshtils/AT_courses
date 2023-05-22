# -*- coding: utf-8 -*-
import pytest
from model.group import Group
import random
import string


def random_str(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


group_data = [
    Group(name=name, footer=footer, header=header)
    for name in ["", random_str("name", 10)]
    for footer in ["", random_str("footer", 25)]
    for header in ["", random_str("name", 25)]
]


@pytest.mark.parametrize("group", group_data, ids=[repr(x) for x in group_data])
def test_add_test_group(app, group):
    old_groups = app.group.get_group_list()
    app.group.create(group)
    assert len(old_groups) + 1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
