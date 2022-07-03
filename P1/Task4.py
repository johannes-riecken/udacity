from functools import reduce

from typing import List


class Group(object):
    def __init__(self, _name: str) -> None:
        self.name = _name
        self.groups: List['Group'] = []
        self.users: List[str] = []

    def add_group(self, group: 'Group') -> None:
        self.groups.append(group)

    def add_user(self, user: str) -> None:
        self.users.append(user)

    def get_groups(self) -> List['Group']:
        return self.groups

    def get_users(self) -> List[str]:
        return self.users

    def get_name(self) -> str:
        return self.name


parent = Group("parent")
child = Group("child")
sub_child = Group("sub_child")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)


def is_user_in_group(user: str, group: Group) -> bool:
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    return user in group.get_users() or \
        reduce(lambda a, b: a or b,
               [is_user_in_group(user, x) for x in group.get_groups()], False)


# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large
# values

# Test Case 1
print(is_user_in_group("sub_child_user", parent))  # True
print(is_user_in_group("does_not_exist", parent))  # False

# Test Case 2
print(is_user_in_group("", Group("group")))  # False

# Test Case 3
parent = Group("parent")
parent.add_user("")
print(is_user_in_group("", parent))  # True
