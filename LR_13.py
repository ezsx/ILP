def task1():
    class Cat():

        def __init__(self, name, color, weight):
            self.name = name
            self.color = color
            self.weight = weight

        def meow(self):
            print(f"кот по имени: {self.name}, весом в {self.weight} кг, цветом {self.color}, сказал МЯУ!11!")

    def rez():
        some_cat = Cat("Вася", "чернобелый", 7)
        some_cat.meow()

    rez()


def task2():
    class Animal():
        def __init__(self, name):
            self.name = name
            print(f"Родилось животное {name}")

        def eat(self):
            print("Намнём")

        def setName(self, ch_name):
            self.name = ch_name

        def getName(self):
            return self.name

        def MakeNoise(self):
            print(f"{self.name} говорит: Гррр")

    def rez():
        some_animal = Animal("аляулю")
        some_animal.getName()
        some_animal.setName("улюаля")
        some_animal.eat()
        some_animal.MakeNoise()

    rez()


def task3():
    class StringVar:
        def __init__(self, object):
            self.str_ = str(object)

        def set(self, n_str):
            self.str_ = n_str

        def get(self):
            return self.str_

    def rez():
        some_str = StringVar("какой-то текст")
        print(some_str.get())
        some_str.set("новый текст")
        print(some_str.get())

    rez()


def task4():
    class Point:
        def __init__(self, x, y):
            self.x = x
            self.y = y

        def __str__(self):
            return f"({self.x}, {self.y})"

        def __add__(self, other):
            return Point(self.x + other.x, self.y + other.y)

        def __sub__(self, other):
            return Point(self.x - other.x, self.y - other.y)

        def __mul__(self, other):
            return Point(self.x * other.x, self.y * other.y)

        def __truediv__(self, other):
            return Point(self.x / other.x, self.y / other.y)

        def __floordiv__(self, other):
            return Point(self.x // other.x, self.y // other.y)

        def __mod__(self, other):
            return Point(self.x % other.x, self.y % other.y)

        def __pow__(self, other):
            return Point(self.x ** other.x, self.y ** other.y)

        def __lt__(self, other):
            return self.x < other.x and self.y < other.y

        def __le__(self, other):
            return self.x <= other.x and self.y <= other.y

        def __eq__(self, other):
            return self.x == other.x and self.y == other.y

        def __ne__(self, other):
            return self.x != other.x and self.y != other.y

        def __gt__(self, other):
            return self.x > other.x and self.y > other.y

        def __ge__(self, other):
            return self.x >= other.x and self.y >= other.y

    def rez():
        p1 = Point(1, 2)
        p2 = Point(3, 4)
        print(p1 + p2)
        print(p1 - p2)
        print(p1 * p2)
        print(p1 / p2)
        print(p1 // p2)
        print(p1 % p2)
        print(p1 ** p2)
        print(p1 < p2)
        print(p1 <= p2)
        print(p1 == p2)
        print(p1 != p2)
        print(p1 > p2)
        print(p1 >= p2)

    rez()


def task5():
    class Animal():
        def __init__(self, name):
            self.name = name
            print(f"Родилось животное {name}")

        def eat(self):
            print("Намнём")

        def setName(self, ch_name):
            self.name = ch_name

        def getName(self):
            return self.name

        def MakeNoise(self):
            print(f"{self.name} говорит: Гррр")

    class Cat(Animal):
        def __init__(self, name, color, weight):
            super().__init__(name)
            self.color = color
            self.weight = weight
            print(f"Родился кот по имени: {name}, весом в {weight} кг, цветом {color}")

        def meow(self):
            print(f"кот по имени: {self.name}, весом в {self.weight} кг, цветом {self.color}, сказал МЯУ!11!")

        def MakeNoise(self):
            print(f"{self.name} говорит: Мяу")

    def rez():
        some_cat = Cat("Вася", "чернобелый", 7)
        some_cat.meow()
        some_cat.MakeNoise()

    rez()


def task6():
    class Animal():
        def __init__(self, name):
            self.name = name
            print(f"Родилось животное {name}")

        def eat(self):
            print("Намнём")

        def setName(self, ch_name):
            self.name = ch_name

        def getName(self):
            return self.name

        def MakeNoise(self):
            print(f"{self.name} говорит: Гррр")

    class Dog(Animal):
        def __init__(self, name, color, weight):
            super().__init__(name)
            self.color = color
            self.weight = weight
            print(f"Родился собака по имени: {name}, весом в {weight} кг, цветом {color}")

        def bark(self):
            print(f"собака по имени: {self.name}, весом в {self.weight} кг, цветом {self.color}, сказал ГАВ!11!")

        def MakeNoise(self):
            print(f"{self.name} говорит: Гав")

    def rez():
        some_dog = Dog("Бобик", "черный", 10)
        some_dog.bark()
        some_dog.MakeNoise()

    rez()


def task7():
    class Animal():
        def __init__(self, name):
            self.name = name
            print(f"Родилось животное {name}")

        def eat(self):
            print("Намнём")

        def setName(self, ch_name):
            self.name = ch_name

        def getName(self):
            return self.name

        def MakeNoise(self):
            print(f"{self.name} говорит: Гррр")

    class Cat(Animal):
        def __init__(self, name, color, weight):
            super().__init__(name)
            self.color = color
            self.weight = weight
            print(f"Родился кот по имени: {name}, весом в {weight} кг, цветом {color}")

        def meow(self):
            print(f"кот по имени: {self.name}, весом в {self.weight} кг, цветом {self.color}, сказал МЯУ!11!")

        def MakeNoise(self):
            print(f"{self.name} говорит: Мяу")

    class Dog(Animal):
        def __init__(self, name, color, weight):
            super().__init__(name)
            self.color = color
            self.weight = weight
            print(f"Родился собака по имени: {name}, весом в {weight} кг, цветом {color}")

        def bark(self):
            print(f"собака по имени: {self.name}, весом в {self.weight} кг, цветом {self.color}, сказал ГАВ!11!")

        def MakeNoise(self):
            print(f"{self.name} говорит: Гав")

    def rez():
        some_cat = Cat("Вася", "чернобелый", 7)
        some_cat.meow()
        some_cat.MakeNoise()
        some_dog = Dog("Бобик", "черный", 10)
        some_dog.bark()
        some_dog.MakeNoise()
        some_dog_2 = Dog("Шарик", "белый", 5)
        some_dog_2.bark()
        some_dog_2.MakeNoise()
        some_animal = Animal("Какое-то животное")
        some_animal.MakeNoise()

    rez()


if __name__ == "__main__":
    # task1()
    # task2()
    # task3()
    # task4()
    # task5()
    # task6()
    task7()
