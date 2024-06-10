from PythonInheritance.class_node import *


class base_class_1:
    def hello_from_base_class_1(self):
        pass


class base_class_2:
    def hello_from_base_class_2(self):
        pass


class some_class(base_class_1, base_class_2):
    def hello_from_some_class(self):
        pass


some_class_node = ClassNode(some_class)


def test_get_unique_class_name__correct_name():
    result = get_unique_class_name(some_class)
    expected = "class_node_test.some_class"
    assert result == expected, f"Expected {expected}, got {result}"


def test_get_all_methods__correct_list():
    result = sorted(get_all_methods(some_class))
    expected = sorted(["hello_from_base_class_1", "hello_from_base_class_2", "hello_from_some_class"])
    assert result == expected, f"Expected {expected}, got {result}"


def test_class_node__correct_distinct_methods():
    result = sorted(some_class_node.get_distinct_methods())
    expected = sorted(["hello_from_some_class"])
    assert result == expected, f"Expected {expected}, got {result}"


def test_class_node__correct_base_class_names():
    result = sorted(some_class_node.base_classes.keys())
    expected = sorted([get_unique_class_name(base_class_1), get_unique_class_name(base_class_2)])
    assert result == expected, f"Expected {expected}, got {result}"
