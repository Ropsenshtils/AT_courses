from model.group import Group


def test_add_test_group(app, db, json_groups, check_ui):
    group = json_groups
    old_groups = db.get_group_list()
    app.group.create(group)
    new_groups = db.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    app.group.check_ui(check_ui=check_ui, groups_db=new_groups, group_ui=app.group.get_group_list())
