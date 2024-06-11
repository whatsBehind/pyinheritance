import threading


class ClassNodeFactory:

    def __init__(self):
        self._class_nodes: dict[str, "_ClassNode"] = {}
        self._lock = threading.RLock()
        self._blocklist: list[type] = [object]

    def init(self, cls_type: type) -> "_ClassNode":
        return self._get_or_create(cls_type)

    def _get_or_create(self, cls_type: type) -> "_ClassNode":
        with self._lock:
            cls_name = get_unique_class_name(cls_type)
            if cls_name not in self._class_nodes.keys():
                class_node = _ClassNode(cls_type, self)
                self._class_nodes[cls_name] = class_node

            return self._class_nodes[cls_name]

    def get_base_class_nodes(self, cls_type: type):
        base_class_nodes = []
        with self._lock:
            for base_class in cls_type.__bases__:
                if base_class in self._blocklist:
                    continue
                base_class_node = self._get_or_create(base_class)
                base_class_nodes.append(base_class_node)
            return base_class_nodes

    def get_subclass_nodes(self, cls_type: type):
        subclass_nodes = []
        with self._lock:
            for subclass in cls_type.__subclasses__():
                if subclass in self._blocklist:
                    continue
                subclass_node = self._get_or_create(subclass)
                subclass_nodes.append(subclass_node)
            return subclass_nodes


class _ClassNode:

    def __init__(self, cls_type: type, node_factory: ClassNodeFactory):
        self.name = get_unique_class_name(cls_type)
        self.cls_type = cls_type
        self._base_class_nodes: list[_ClassNode] | None = None
        self._subclass_nodes: list[_ClassNode] | None = None
        self._root_nodes: list[_ClassNode] | None = None
        self.node_factory = node_factory

    def get_base_class_nodes(self) -> list["_ClassNode"]:
        if self._base_class_nodes is None:
            self._base_class_nodes = self.node_factory.get_base_class_nodes(self.cls_type)
        return self._base_class_nodes

    def get_subclass_nodes(self) -> list["_ClassNode"]:
        if self._subclass_nodes is None:
            self._subclass_nodes = self.node_factory.get_subclass_nodes(self.cls_type)
        return self._subclass_nodes

    def get_root_nodes(self) -> list["_ClassNode"]:
        if self._root_nodes is None:
            self.get_base_class_nodes()
            if not self._base_class_nodes:
                # return self if self has no base_class_nodes
                self._root_nodes = [self]
            else:
                self._root_nodes = [base_class_root_node for base_class_node in self._base_class_nodes for
                                    base_class_root_node in base_class_node.get_root_nodes()]
        return self._root_nodes

    def __str__(self) -> str:
        return self.__repr__()

    def __repr__(self) -> str:
        return f"{self.__class__.__module__}.{self.__class__.__name__}(name={self.name!r})"


def get_unique_class_name(cls: type) -> str:
    return f"{cls.__module__}.{cls.__name__}"


# def get_all_methods(cls: type) -> list[str]:
#     public_methods = set()
#     for attr in dir(cls):
#         print(attr)
#         if callable(getattr(cls, attr)) and not attr.startswith("__"):
#             public_methods.add(attr)
#     return list(public_methods)


if __name__ == "__main__":
    pass
