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


def test_some_class_should_have_correct_bases():
    some_class_node = node_factory.init(SomeClass)
    actual_base_class_nodes = sorted(base_class_node.name for base_class_node in some_class_node.get_base_class_nodes())
    expected_base_class_nodes = sorted(["class_node_test.BaseClass1", "class_node_test.BaseClass2"])
    assert actual_base_class_nodes == expected_base_class_nodes, f"Expected {expected_base_class_nodes}, got {actual_base_class_nodes}"


def test_base_class1_should_have_correct_subclasses():
    base_class1_node = node_factory.init(BaseClass1)
    actual_base_class_nodes = sorted(subclass_node.name for subclass_node in base_class1_node.get_subclass_nodes())
    expected_base_class_nodes = sorted(["class_node_test.SomeClass"])
    assert actual_base_class_nodes == expected_base_class_nodes, f"Expected {expected_base_class_nodes}, got {actual_base_class_nodes}"

