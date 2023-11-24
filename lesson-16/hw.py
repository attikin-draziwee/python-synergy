from math import ceil
# Задание 1


class Cash:
    __money = 0

    def __init__(self, start_money):
        self.__money = start_money

    def top_up(self, x):
        self.__money += x

    def count_1000(self):
        return self.__money // 1000

    def take_away(self, x):
        if (self.__money < x):
            print('Error. Don\'t enough money.')
        else:
            self.__money -= x
        return self.__str__

    def __str__(self):
        return f'Balance is {self.__money}'

# Задание 2


class Turtle:
    __x = 0
    __y = 0
    __s = 3

    def __init__(self, x, y, s=2):
        self.__x = x
        self.__y = y
        self.__s = s

    def go_up(self):
        self.__y += self.__s

    def go_down(self):
        self.__y -= self.__s

    def go_left(self):
        self.__x -= self.__s

    def go_right(self):
        self.__x += self.__s

    def evolve(self):
        self.__s += 1

    def degrade(self):
        if (self.__s < 1):
            print("Ошибка. Скорость не может быть меньше единицы.")
            return 0
        self.__s -= 1

    def distance_between(self, p1, p2):
        if (p1 < p2):
            if (p1 < 0):
                return p2 + abs(p1)
            else:
                return p2 - p1
        else:
            if (p2 < 0):
                return p1 + abs(p2)
            else:
                return p1 - p2

    def count_moves(self, x2, y2):
        moves = (self.distance_between(self.__x, x2) +
                 self.distance_between(self.__y, y2)) / self.__s
        if ((moves*10 % 10) != 00):
            return f"Ошибка! Черепашка не сможет добраться до этих координат ({x2}, {y2}) с текущей скоростью."
        else:
            return moves

    def __str__(self):
        return f"x: {self.__x} y: {self.__y} speed: {self.__s}"
