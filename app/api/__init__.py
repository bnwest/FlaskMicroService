from flask_restplus import Namespace
from .v1.api import build_namespaces as nsv1


_NS_LIST = [
    nsv1,
]


def construct_versioned_namespace(version_number):
    def do_construct(path_root, description=""):
        ns = Namespace('/'.join([path_root, version_number]), description=description)
        return ns
    return do_construct


def register_apis(api):
    for ns_builder in _NS_LIST:
        for ns in ns_builder(construct_versioned_namespace):
            assert ns
            api.add_namespace(ns)
