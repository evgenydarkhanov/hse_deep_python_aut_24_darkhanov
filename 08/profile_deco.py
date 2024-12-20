import cProfile
import pstats
import io


def profile_deco(func):
    profiler = cProfile.Profile()
    call_count = 0
    err_count = 0

    def inner(*args, **kwargs):
        nonlocal call_count, err_count
        call_count += 1
        profiler.enable()
        try:
            result = func(*args, **kwargs)
        except Exception:
            err_count += 1
            result = None
        finally:
            profiler.disable()
        return result

    def print_stat():
        s = io.StringIO()
        sortby = "cumulative"
        ps = pstats.Stats(profiler, stream=s).sort_stats(sortby)
        ps.print_stats()
        msg = f"func '{func.__name__}' has been called {call_count} time(s) " \
              f"with {err_count} error(s)\n"
        print(msg)
        print(s.getvalue())

    inner.print_stat = print_stat
    return inner


@profile_deco
def add(a, b):
    return a + b


@profile_deco
def sub(a, b):
    return a - b


@profile_deco
def func_with_error():
    raise TypeError


@profile_deco
def func_with_no_error():
    return None


if __name__ == "__main__":

    add(1, 2)
    add(4, 5)
    add(4, '5')

    sub(4, 5)
    sub([4], (5,))

    func_with_error()

    func_with_no_error()

    add.print_stat()
    sub.print_stat()
    func_with_error.print_stat()
    func_with_no_error.print_stat()
