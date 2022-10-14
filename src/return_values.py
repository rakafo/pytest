from constants import constant1


def return_val():
    foo1 = 1
    return foo1


def return_multiple():
    foo1 = 1
    foo2 = 2
    return [foo1, foo2]


def return_val_from_external():
    return constant1


def return_dict():
    foo = {"key1": "value1"}
    return foo
