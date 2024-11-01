# Подробнее о функциях
def calculate_structure_sum(data):
    k = 0
    if not data:
        return k
    for el in data:
        if isinstance(el, (int, float)):
            k += el
        elif isinstance(el, str):
            k += len(el)
        elif isinstance(el, dict):
            k += calculate_structure_sum(el.items())
        else:
            k += calculate_structure_sum(el)
    return k


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]
print(calculate_structure_sum(data_structure))
