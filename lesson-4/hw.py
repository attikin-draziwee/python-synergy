# Задание 1
a, b = map(float, input('Введите стороны прямоугольника через пробел: ').split())
rect_square = a*b
rect_perimeter = a*2+b*2
print("Площадь: ", rect_square, ", периметр: ", rect_perimeter)

# Задание 2
num = int(input("Введите пятизначное число: "))
formula = (((num % 100 // 10) ** (num % 10)) * (num %
           1000 // 100)) / (num // 10_000 - num // 1000 % 10)
print(formula)
