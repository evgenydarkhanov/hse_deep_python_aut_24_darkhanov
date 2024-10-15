from typing import Optional, List
from functools import wraps


def retry_deco(repeat: Optional[int] = None, errors: Optional[List] = None):
    def inner_deco(func):
        @wraps(func)
        def func_log(func, i, *args, res=None, err=None, **kwargs):
            string_to_print = f'run "{func.__name__}" with ' \
                              f'positional args = {args}, ' \
                              f'keyword kwargs = {kwargs}, '
            if res is not None:
                print(string_to_print + f'attempt = {i+1}, result = {res}')
            if err is not None:
                print(
                    string_to_print +
                    f'attempt = {i+1}, exception = {type(err).__name__}'
                )

        @wraps(func)
        def inner(*args, **kwargs):
            if errors is not None and repeat is not None:
                if repeat < 0:
                    raise ValueError("'repeat' must be >= 0")
                for i in range(repeat):
                    try:
                        result = func(*args, **kwargs)
                        func_log(func, i, *args, res=result, **kwargs)
                        return result
                    except tuple(errors) as error:
                        func_log(func, i, *args, err=error, **kwargs)
                        return None
                    except Exception as error:
                        func_log(func, i, *args, err=error, **kwargs)
                        continue

            elif repeat is not None and errors is None:
                if repeat < 0:
                    raise ValueError("'repeat' must be >= 0")
                for i in range(repeat):
                    try:
                        result = func(*args, **kwargs)
                        func_log(func, i, *args, res=result, **kwargs)
                        return result
                    except Exception as error:
                        func_log(func, i, *args, err=error, **kwargs)
                        continue

            elif errors is not None and repeat is None:
                try:
                    result = func(*args, **kwargs)
                    func_log(func, 0, *args, res=result, **kwargs)
                    return result
                except tuple(errors) as error:
                    func_log(func, 0, *args, err=error, **kwargs)
                    return None
                except Exception as error:
                    func_log(func, 0, *args, err=error, **kwargs)
                    return None

            else:
                try:
                    result = func(*args, **kwargs)
                    func_log(func, 0, *args, res=result, **kwargs)
                    return result
                except Exception as error:
                    func_log(func, 0, *args, err=error, **kwargs)
                    return None

        return inner
    return inner_deco
