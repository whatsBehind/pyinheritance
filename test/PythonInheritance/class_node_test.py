from PythonInheritance.class_node import get_unique_class_name

class TestClass:
    pass

def test_get_unique_class_name_correctNameForTestClass():
    result = get_unique_class_name(TestClass)
    expected = "class_node_test.TestClass"
    assert result == expected, f"Expected {expected}, got {result}"