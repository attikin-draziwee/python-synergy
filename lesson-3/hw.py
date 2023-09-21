from math import floor

# Задание 1
pet = {
    "animal": input('Что у вас за животное? '),
    "name": input('Как его зовут? '),
    "age": floor(float(input('Возрат в годах? ').replace(',', '.')))
}

print(
    f'Это {pet["animal"]} по кличке "{pet["name"]}". Возраст: {pet["age"]} года.')

# Задание 2
evolution = [
    'habilis',
    'rudolfensis',
    'erectus',
    'georgicus',
    # 'ergaster',
    # 'antecessor',
    # 'cepranensis',
    # 'heidelbergensis',
    # 'rhodesiensis',
    # 'neanderthalensis',
    # 'sapiens sapiens'
]

incorrect_answers = []
answer__list = []

print("#"*20)
print(f"Введите все {len(evolution)} стадий эволюции человека: ")
for i in evolution:
    answer__list.append({'answer': input("Homo ").lower(), 'correct': i})
    if answer__list[-1]['answer'] != i:
        incorrect_answers.append(answer__list[-1])

print("_"*20)
print("Ваша последовательность: ")
print(*(answer['answer'] for answer in answer__list), sep="=>")
print("–"*20)

if len(incorrect_answers):
    print("Неверно! Верная последовательность: ",
          '=>'.join(evolution), sep="\n")
    print("Вы ошиблись в этих местах: ")
    print(
        *(f'x {answer["correct"]} != {answer["answer"]}' for answer in incorrect_answers), sep="\n")
else:
    print("Все верно, вы молодец!")
