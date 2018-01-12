def singleton(func):
    instances = {}

    def get_instance(*args, **kwargs):
        print (args, kwargs)
        if func not in instances:
            instances[func] = func(*args, **kwargs)
        return instances[func]
    return get_instance

