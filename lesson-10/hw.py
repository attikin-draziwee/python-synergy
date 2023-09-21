# Задание 1

pets = dict()

pet_name = input('Введите имя питомца: ')
pets[pet_name] = {
	'type' : input('Вид питомца: '),
	'age' : int(input('Возраст питомца: ')),
	'name_owner' : input('Имя владельца: ')
}

output_age = ''
pet = pets[list(pets.keys())[0]]

if ((pet_age:=pet['age']) >= 5 and pet_age <= 20) or (pet_age > 20 and (pet_age % 10 >= 5 and pet_age % 10 <=9) or (pet_age % 10 == 0 or pet_age % 100 == 0)):
	output_age = 'лет'
elif pet['age'] % 10 == 1:
	output_age = 'год'
else:
	output_age = 'года'

print(f"Это {pet['type']} по кличке \"{pet_name}\". Возраст питомца: {pet['age']} {output_age}. Имя владельца: {pet['name_owner']}")

# Задание 2

my_dict = dict()

for i in range(-5, 11):
	my_dict[i] = i**i