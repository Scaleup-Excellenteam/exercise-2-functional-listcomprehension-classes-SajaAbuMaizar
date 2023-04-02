def zipwith(func, *iterables):
    return [func(*args) for args in zip(*iterables)]


print(zipwith(max, (5, 4), (2, 5), (6, -6)))