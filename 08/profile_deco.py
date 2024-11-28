import cProfile
import pstats
import io


def profile_deco(func):
    profiler = cProfile.Profile()
    call_count = 0

    def inner(*args, **kwargs):
        nonlocal call_count
        call_count += 1
        profiler.enable()
        result = func(*args, **kwargs)
        profiler.disable()
        return result

    def print_stat():
        s = io.StringIO()
        sortby = "cumulative"
        ps = pstats.Stats(profiler, stream=s).sort_stats(sortby)
        ps.print_stats()
        print(f"func '{func.__name__}' has been called {call_count} time(s)\n")
        print(s.getvalue())

    inner.print_stat = print_stat
    return inner


@profile_deco
def add(a, b):
    return a + b


@profile_deco
def sub(a, b):
    return a - b


if __name__ == "__main__":

    add(1, 2)
    add(4, 5)
    sub(4, 5)

    add.print_stat()
    sub.print_stat()
