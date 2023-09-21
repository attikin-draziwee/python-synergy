from random import randint

# Задание 1
num = int(input("Введите число: "))
if num != 0:
    if num > 0:
        print('положительное', end=' ')
    else:
        print('отрицательное', end=' ')
    print('нечетное' if num % 2 else 'четное', 'число')
else:
    print('нулевое число')

# Задание 2
word = input('Please, write english word: ')
count_vowels, count_consonants = 0, 0
vowels = {
    'a': 0,
    'e': 0,
    'i': 0,
    'o': 0,
    'u': 0
}

for i in word:
    if i in vowels.keys():
        vowels[i] += 1
    else:
        count_consonants += 1

count_vowels = sum(vowels.values())

print(f'The word {word} has {len(word)} letters, where:',
      f'The number of consonants is {count_consonants}',
      f'The number of vowels is {count_vowels}', sep='\n')

print('The number of vowels in alphabetical order:')
print(*(f'# {letter} - {count}' for letter,
      count in vowels.items()), sep='\n')

# Задание 3
min_amount = int(input('Минимальная сумма вложений: '))
michael_amount = randint(0, min_amount*2)
ivan_amount = randint(0, min_amount*2)

print('Сумма у Майкла: ', michael_amount)
print('Сумма у Ивана: ', ivan_amount)


if ivan_amount >= min_amount and michael_amount >= min_amount:
    print(2)
elif ivan_amount >= min_amount or michael_amount >= min_amount:
    print('Mike' if michael_amount >= min_amount else 'Ivan')
elif ivan_amount + michael_amount >= min_amount:
    print(1)
else:
    print(0)
