import numpy as np
from time import time


def time_decorator(func):
    # This function shows the execution time of
    # the function object passed
    def wrap_func(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        print(f'Function {func.__name__!r} executed in {(t2 - t1):.4f}s')
        return result

    return wrap_func


def random_range_integers(low: int, high: int, size: int, seed=0, unique=True) -> list:
    """

    :param low:
    :param high:
    :param size:
    :param seed:
    :param unique:
    :return: specified sized list range with unique values, can be have
    both positive and negative integers.
    """
    np.random.seed(seed)
    if unique:
        return list(set(np.random.randint(low=low, high=high, size=size)))
    else:
        return list(np.random.randint(low=low, high=high, size=size))
