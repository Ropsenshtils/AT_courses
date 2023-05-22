# -*- coding: utf-8 -*-
from model.group import Group
import random


def test_modify_first_group(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    old_groups = db.get_group_list()
    new_group = Group(name="kappa4", header="chino4", footer="blank4")
    group = random.choice(old_groups)
    group = app.group.group_change_info(group, new_group)
    app.group.modify_group_by_id(group, group.id)
    new_groups = db.get_group_list()
    old_groups[new_groups.index(group)] = group
    assert len(old_groups) == len(new_groups)
    assert old_groups == new_groups
    app.group.check_ui(check_ui=check_ui, groups_db=new_groups, group_ui=app.group.get_group_list())
