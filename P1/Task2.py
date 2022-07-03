import os
from typing import Iterable


def find_files(suffix: str, path: str) -> Iterable[str]:
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    c_files = []
    entries = os.listdir(path)
    for e in entries:
        p = os.path.join(path, e)
        if os.path.isfile(p):
            if e[len(e)-len(suffix):] == suffix:
                c_files.append(p)
        else:
            c_files += find_files(suffix, p)
    return c_files


# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large
# values

# Test Case 1
# prints the same as `find ./testdir -name '*.c'`
print("\n".join(find_files('.c', './testdir')))

# Test Case 2
# prints same as `find ./testdir -type f`
print("\n".join(find_files('', './testdir')))

# Test Case 3
# prints same as `find testdir/subdir3 -type f`
print("\n".join(find_files('', 'testdir/subdir3')))
