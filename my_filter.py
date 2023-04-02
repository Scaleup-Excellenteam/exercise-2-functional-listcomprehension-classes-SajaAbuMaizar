def my_filter(func, iterable):
    result = []
    for item in iterable:
        if func(item):
            result.append(item)
    return result


# example usage
def is_even(x):
    return x % 2 == 0


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even_numbers = my_filter(is_even, numbers)
print(even_numbers)
