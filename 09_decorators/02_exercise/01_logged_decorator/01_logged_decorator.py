def logged(function):
    def wrapper(*args):
        res = f"you called {function.__name__}" \
              f"({', '.join(str(arg) for arg in args)})\n" \
              f"it returned {function(*args)}"
        return res

    return wrapper


@logged
def func(*args):
    return 3 + len(args)


print(func(4, 4, 4))
