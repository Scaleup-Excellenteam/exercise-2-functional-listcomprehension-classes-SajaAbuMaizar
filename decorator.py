import functools


class TypeErrorWithMsg(TypeError):
    pass


def type_check(correct_type):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(arg):
            if not isinstance(arg, correct_type):
                raise TypeErrorWithMsg(f"Expected {correct_type.__name__}, got {type(arg).__name__}")
            return func(arg)
        return wrapper
    return decorator


@type_check(int)
def times2(num):
    return num * 2


print(times2(2))  # Output: 4
print(times2('foo'))  # Raises TypeErrorWithMsg: Expected int, got str
