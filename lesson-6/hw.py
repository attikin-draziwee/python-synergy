# Задание 1
n = int(input("Введите число N: "))
count_zero = 0
print("Количество нулей: ", len(list(j for i in range(1, n+1)
      if (j := int(input("Введите целое число: "))) == 0)))

# Задание 2
x = int(input('Введите натуральное число X: '))
count_divided = 0
for i in range(1, 2_000_000_000):
    if i > x:
        break
    elif x % i == 0:
        count_divided += 1
        print(f'Делитель {x} = ', i)

print('Количество делителей = ', count_divided)

# Задание 3
a = int(input("Введите число A: "))
b = int(input("Введите число B: "))

print(*(j for j in range(a, b+1) if not j % 2))
