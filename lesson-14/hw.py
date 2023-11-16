# Задание 1

my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]


def print_list(elements, ind=0):
    print(elements[ind], ' # Конец списка' if ind == len(elements) - 1 else '')
    return elements[ind] if ind == (len(elements) - 1) else print_list(elements, ind + 1)


print_list(my_list)
