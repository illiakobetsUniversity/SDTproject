import functools


__all__ = ['as_singleton']


def as_singleton(callable_object):
    @functools.wraps(callable_object)
    def singleton_wrapper(*args, **kwargs):
        if singleton_wrapper.instance is None:
            singleton_wrapper.instance = callable_object(*args, **kwargs)
        return singleton_wrapper.instance
    singleton_wrapper.instance = None
    return singleton_wrapper

