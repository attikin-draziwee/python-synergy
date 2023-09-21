# Задание 1

n = int(input("вводите число N: "))
my_arr = set(input("Введите все числа: ").split()[:n])
print(len(my_arr))

## Задание 2

first_list = set(a for a in input('Введите первый список из чисел через пробел: ').split())
second_list = set(a for a in input('Введите второй список из чисел через пробел: ').split())
print('length:', len(first_list.intersection(second_list)))

# Задание 3

sets = set()
print(*(f"{a} - YES" if (a in sets) else f"{sets.add(a) or a} - NO" for a in input("Введите числа через пробел: ").split()), sep="\n")