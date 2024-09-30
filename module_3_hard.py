data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]


def calculate_structure_sum(*data_structure):  # * используем для неограниченного числа параметров
    cal_ = 0
    for i in data_structure:
        if isinstance(i, int):  # isinstance - для определения типа данного используйте функцию
            cal_ += i
        elif isinstance(i, dict):
            cal_ += calculate_structure_sum(*i.items())
        elif isinstance(i, (list, tuple, set)):
            cal_ += calculate_structure_sum(*i)
        elif isinstance(i, str):
            cal_ += len(i)
    return cal_


result = calculate_structure_sum(data_structure)
print(result)
