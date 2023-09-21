import math
# Задание 1

n = int(input('Введите количество строк: '))
n_arr = [int(input('Введите число: ')) for a in range(0, n)]
n_arr.reverse()
print(n_arr)

# Задание 2

j = int(input("вводите число N: "))
my_arr = list(map(int, input("Введите все числа: ").split()))[:j]
def movArr(arr):
	return [arr[i] for i in range(-1, len(arr)-1)]

print(movArr(my_arr))

# Задание 3

def arrRemove(arr):
	arr.remove(max(arr))
	arr.remove(arr[0])

def optimal_weight(arr, max_weight):
	result = []
	arr.sort(reverse=True)
	while (len(arr) > 1):
		if ((weight:= arr[0] + max(arr)) <= max_weight):
			result.append(weight)
			arrRemove(arr)
		elif ((weight:= arr[0] + min(arr)) <= max_weight):
			result.append(weight)
			arrRemove(arr)
		else:
			result.append(arr[0])
			arr.remove(arr[0])
	if len(arr) == 1:
		result.extend(arr)
	return result
			
max_weight = int(input('Вводите максимальную массу одной лодки: '))
fisher_men = int(input('Количество рыбаков на берегу: '))

fisher_weight = [int(input(f'Введите вес {i+1} рыбака: ')) for i in range(fisher_men)]

print('Минимальное количество лодок =', len(optimal_weight(fisher_weight, max_weight)))

