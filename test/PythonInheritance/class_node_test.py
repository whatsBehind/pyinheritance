from PythonInheritance.class_node import *


class BaseClass1:
    def hello_from_base_class_1(self):
        pass


class BaseClass2:
    def hello_from_base_class_2(self):
        pass


class SomeClass(BaseClass1, BaseClass2):
    def hello_from_some_class(self):
        pass


some_class_node = ClassNode(SomeClass)


def test_get_unique_class_name__correct_name():
    result = get_unique_class_name(SomeClass)
    expected = "class_node_test.some_class"
    assert result == expected, f"Expected {expected}, got {result}"


def test_get_all_methods__correct_list():
    result = sorted(get_all_methods(SomeClass))
    expected = sorted(["hello_from_base_class_1", "hello_from_base_class_2", "hello_from_some_class"])
    assert result == expected, f"Expected {expected}, got {result}"


def test_class_node__correct_distinct_methods():
    result = sorted(some_class_node.get_distinct_methods())
    expected = sorted(["hello_from_some_class"])
    assert result == expected, f"Expected {expected}, got {result}"


def test_class_node__correct_base_class_names():
    result = sorted(some_class_node.base_classes.keys())
    expected = sorted([get_unique_class_name(BaseClass1), get_unique_class_name(BaseClass2)])
    assert result == expected, f"Expected {expected}, got {result}"
