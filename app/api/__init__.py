from .v1.api import build_namespaces as nsv1


_NS_LIST = [
    nsv1,
]


def register_apis(api):
    for ns_builder in _NS_LIST:
        api.add_namespace(ns_builder())
