def build_namespaces(create_ns_func):
    ns_partial = create_ns_func('v1')

    from api.v1.predict_construction_time.app import init_app as init1
    #from api.v1.do_something_else.app import init_app as init2

    namespaces = [init_app(ns_partial) for init_app in [init1]]
    return namespaces