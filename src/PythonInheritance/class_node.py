class ClassNode:
    def __init__(self, cls: type) -> None:
        self.cls = cls
        self.name = get_unique_class_name(cls)
        self.base_classes: dict[str, ClassNode] = get_base_class_nodes(cls)
        self.all_methods: list[str] = get_all_methods(cls)
        self.distinct_methods: list[str] = self.get_distinct_methods()

    def get_distinct_methods(self) -> list[str]:
        base_class_methods = set()
        for base_class_node in self.base_classes.values():
            base_class_methods.add(base_class_node.all_methods)
        return [method for method in self.all_methods if method not in base_class_methods]


def get_unique_class_name(cls: type) -> str:
    return f"{cls.__module__}.{cls.__name__}"


def get_base_class_nodes(cls: type) -> dict[str, ClassNode]:
    base_class_nodes = {}
    for base_class in list(cls.__bases__):
        base_class_node = ClassNode(base_class)
        base_class_nodes[get_unique_class_name(base_class)] = base_class_node
    return base_class_nodes


def get_all_methods(cls: type) -> list[str]:
    public_methods = set()
    for attr in dir(cls):
        print(attr)
        if callable(getattr(cls, attr)) and not attr.startswith("__"):
            public_methods.add(attr)
    return list(public_methods)


if __name__ == "__main__":
    print(get_all_methods(ClassNode))
