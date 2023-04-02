def group_by(func, iterable):
    result_dict = {}
    for item in iterable:
        key = func(item)
        if key in result_dict:
            result_dict[key].append(item)
        else:
            result_dict[key] = [item]
    return result_dict


print(group_by(len, ["hi", "bye", "yo", "try"]))
