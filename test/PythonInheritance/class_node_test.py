from PythonInheritance.class_node import ClassNodeFactory, get_unique_class_name


class BaseClass1:
    def hello_from_base_class_1(self):
        pass


class BaseClass2:
    def hello_from_base_class_2(self):
        pass


class SomeClass(BaseClass1, BaseClass2):
    def hello_from_some_class(self):
        pass


node_factory = ClassNodeFactory()
some_class_node = node_factory.init(SomeClass)


def test_get_unique_class_name__correct_name():
    result = get_unique_class_name(SomeClass)
    expected = "class_node_test.SomeClass"
    assert result == expected, f"Expected {expected}, got {result}"


def test_class_node_init__should_dedupe():
    node_factory.init(SomeClass)
    node_factory.init(BaseClass1)
    node_factory.init(BaseClass2)
    actual_class_node_number = len(node_factory._class_nodes)
    expected_class_node_number = 3
    assert expected_class_node_number == actual_class_node_number, f"Expected {expected_class_node_number}, got {actual_class_node_number}"

# def test_get_all_methods__correct_list():
#     result = sorted(get_all_methods(SomeClass))
#     expected = sorted(["hello_from_base_class_1", "hello_from_base_class_2", "hello_from_some_class"])
#     assert result == expected, f"Expected {expected}, got {result}"


# def test_class_node__correct_distinct_methods():
#     result = sorted(some_class_node.get_distinct_methods())
#     expected = sorted(["hello_from_some_class"])
#     assert result == expected, f"Expected {expected}, got {result}"


# def test_class_node__correct_base_class_names():
#     result = sorted(some_class_node.base_classes.keys())
#     expected = sorted([get_unique_class_name(BaseClass1), get_unique_class_name(BaseClass2)])
#     assert result == expected, f"Expected {expected}, got {result}"
