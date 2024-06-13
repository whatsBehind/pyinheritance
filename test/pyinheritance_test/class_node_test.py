from pyinheritance.class_node import get_unique_class_name, ClassNodeFactory


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
    actual_subclass_nodes = sorted(subclass_node.name for subclass_node in base_class1_node.get_subclass_nodes())
    expected_subclass_nodes = sorted(["class_node_test.SomeClass"])
    assert actual_subclass_nodes == expected_subclass_nodes, f"Expected {expected_subclass_nodes}, got {actual_subclass_nodes}"


def test_some_class_should_have_correct_root_nodes():
    some_class_node = node_factory.init(SomeClass)
    actual_root_class_nodes = sorted(base_class_node.name for base_class_node in some_class_node.get_root_nodes())
    expected_root_class_nodes = sorted(["class_node_test.BaseClass1", "class_node_test.BaseClass2"])
    assert actual_root_class_nodes == expected_root_class_nodes, f"Expected {expected_root_class_nodes}, got {actual_root_class_nodes}"


def base_class1_should_have_self_as_root_node():
    base_class1_node = node_factory.init(BaseClass1)
    actual_root_nodes = sorted(root_class_node.name for root_class_node in base_class1_node.get_subclass_nodes())
    expected_root_nodes = sorted(["class_node_test.BaseClass1"])
    assert actual_root_nodes == expected_root_nodes, f"Expected {expected_root_nodes}, got {actual_root_nodes}"


def test_class_node_should_be_printed_corrected():
    some_class_node = node_factory.init(SomeClass)
    actual_printed_str = some_class_node.__repr__()
    expected_printed_str = "pyinheritance.class_node._ClassNode(name='class_node_test.SomeClass')"
    assert actual_printed_str == expected_printed_str, f"Expected {expected_printed_str}, got {actual_printed_str}"


def test_methods_in_some_class():
    some_class_node = node_factory.init(SomeClass)
    actual_methods = sorted(some_class_node.get_methods())
    expected_methods = sorted(["hello_from_base_class_1", "hello_from_base_class_2", "hello_from_some_class"])
    assert actual_methods == expected_methods, f"Expected {expected_methods}, got {actual_methods}"


def test_distinct_methods_in_some_class():
    some_class_node = node_factory.init(SomeClass)
    actual_distinct_methods = sorted(some_class_node.get_distinct_methods())
    expected_distinct_methods = sorted(["hello_from_some_class"])
    assert actual_distinct_methods == expected_distinct_methods, f"Expected {expected_distinct_methods}, got {actual_distinct_methods}"
