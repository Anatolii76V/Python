def make_hashable(item):
    if isinstance(item, dict):
        return tuple(item.items())
    elif isinstance(item, list):
        return tuple(item)
    return item


def keyword_args_to_dict(**kwargs):
    result_dict = {}
    for key, value in kwargs.items():
        result_dict[make_hashable(value)] = key
    return result_dict


result = keyword_args_to_dict(a=1, b=2, c=[3, 4, 5])
print(result)
