from collections import namedtuple


def return_namedtuple(*x):
    def decorator(func):
        def wrapper(*args, **kwargs):
            a = func(*args, **kwargs)
            if isinstance(a, tuple):
                new_tuple = namedtuple('my_tuple', list(x))
                a = new_tuple(*a)
                return a
            else:
                return a
        return wrapper
    return decorator