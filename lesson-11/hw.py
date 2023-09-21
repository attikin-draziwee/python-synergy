# Задание 1

def factorial(n: int):
	iter = 1
	for i in range(1, n+1):
		iter *= i
	return iter

list_fact = [factorial(i) for i in range(6,0,-1)]

# Задание 2

pets = {
	1:
		{
			"Мухтар": {
				"Вид питомца": "Собака",
				"Возраст питомца": 9,
				"Имя владельца": "Павел"
			},
		},
	2:
		{
			"Каа": {
				"Вид питомца": "желторотый питон",
				"Возраст питомца": 19,
				"Имя владельца": "Саша"
			},
		},
}

def create(ID:int):
	pet_name = input('Введите имя питомца: ')
	pets[ID] = {
		pet_name : {
			'Вид питомца' : input('Вид питомца: '),
			'Возраст питомца' : int(input('Возраст питомца: ')),
			'Имя владельца' : input('Имя владельца: ')
		}
	}
	
def read(pet_read:dict):
	pet_name = list(pet_read.keys())[0]
	pet = pet_read[pet_name]
	pet_age = pet['Возраст питомца']
	return f"Это {pet['Вид питомца']} по кличке \"{pet_name}\". Возраст питомца: {pet_age} {get_suffix(pet_age)}. Имя владельца: {pet['Имя владельца']}"

def update(ID:int):
	create(ID)
	
def delete(ID:int):
	global pets
	pets.pop(ID)
	c = 1
	new_pets = dict()
	for i, v in pets.items():
		new_pets[c] = v
		c+=1
	pets = new_pets

def get_pet(ID:int):
	return pets[ID] if ID in pets.keys() else False

def get_suffix(age:int):
	if ((pet_age:=age) >= 5 and pet_age <= 20) or (pet_age > 20 and (pet_age % 10 >= 5 and pet_age % 10 <=9) or (pet_age % 10 == 0 or pet_age % 100 == 0)):
		return 'лет'
	elif age % 10 == 1:
		return'год'
	else:
		return'года'

command = ''

while(True):
	try:
		command = input('Введите команду: ')
		match command:
			case 'create':
				create(len(pets.keys())+1)
			case 'read':
				print(read(get_pet(int(input("Введите ID питомца: ")))))
			case 'update':
				update(int(input("Введите ID питомца: ")))
			case 'delete':
				delete(int(input("Введите ID питомца: ")))
			case 'stop':
				break
			case _:
				print('Неизвестная команда!')
	except Exception as error:
		print('Ошибка!', error)
			
