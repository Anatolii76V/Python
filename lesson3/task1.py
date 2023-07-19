_list = [1, 2, 2, 3, 4, 4, 5, 5, 0, 0, 6]


def remove_duplicates(_list):
    # Преобразование списка в множество уберет дубликаты
    unique_set = set(_list)

    # Преобразование множества обратно в список
    result_list = list(unique_set)

    return result_list


result_list = remove_duplicates(_list)
print(result_list)
