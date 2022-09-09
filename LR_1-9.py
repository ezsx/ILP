def task1_var4():  # решаем в лоб
    minutes, hours = int(input("Enter minutes: ")), 0
    while minutes > 59:
        minutes -= 60
        hours += 1
        if hours > 23:
            hours = 0
    if minutes < 10:
        minutes = "0" + str(minutes)
    if hours < 10:
        hours = "0" + str(hours)
    print(f"{hours}:{minutes}")
    return 0


def task2_var11():  # можно проще например через массив, но так более основательно
    class Point:
        def __init__(self, x, y):
            self.x = x
            self.y = y

        def __str__(self):
            return f"({self.x}, {self.y})"

        def horse_move(self, other):
            if abs(self.x - other.x) == 1 and abs(self.y - other.y) == 2 or abs(self.x - other.x) == 2 and abs(
                    self.y - other.y) == 1:
                return True
            else:
                return False

    a = Point(int(input("Enter x1: ")), int(input("Enter y1: ")))
    b = Point(int(input("Enter x2: ")), int(input("Enter y2: ")))
    print(a.horse_move(b))
    return 0


def task3_var15():  # все просто
    angle = float(input("Enter angle: "))
    while angle > 360:
        angle -= 360
    print(f"{int(angle // 30)} час(ов/a),{int(angle % 30 * 2)} минут(а) {int(angle % 0.5 * 120)} секунд(а)")
    return 0


def task4_var11():  # как то слишком тупо
    cards_number = int(input("Enter number of cards: "))
    for i in range(1, cards_number + 1):
        card_number = int(input("Enter card number: "))
        if card_number != i:
            print(f"Потеряна карта {i}")
    return 0


def task5_var2():  # первые задачи были сложнее
    str = input("Enter string: ")
    print(f"количество слов: {str.count(' ') + 1}")
    return 0


def task6_var7():  # .............
    sred, sum, kol = 0, 0, 0
    num = int(input("Enter number: "))
    while (num != 0):
        sum, kol = sum + num, kol + 1
        num = int(input("Enter number: "))
    sred = sum / kol
    print(f"Среднее арифметическое: {sred}")
    return 0


def task7_var1():  # срезы наше все
    from random import randint
    lst = [randint(-10, 10) for i in range(20)]
    print(lst)
    print(lst[::2])
    return 0


def task8_var6():  # всеоббщеее иииииууууууууу
    n = int(input("Enter n: "))

    def fib(n):
        if n in (1, 2):
            return 1
        return fib(n - 1) + fib(n - 2)

    print(fib(n))
    return 0


def task9_var4(): #это была самой прикольной
    def create_list(n,a,b):
        arr = [i for i in range(1, n)]
        return arr[0:a][::-1]+[0]+arr[0:b:]
    nn=int(input("Enter n: "))
    grr = [create_list(nn, i, nn - i - 1) for i in range(nn)]
    for i in grr:
        print(*i)


if __name__ == "__main__":
    # task1_var4()
    # task2_var11()
    # task3_var15()
    # task4_var11()
    # task5_var2()
    # task6_var7()
    # task7_var1()
    # task8_var6()
    task9_var4()

    pass
