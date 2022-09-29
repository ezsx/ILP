import re


def find_def_in_string(string):
    if re.findall(r'def ', string) == ['def ']:
        return True
    return False


def find_octothorpe_in_string(string):
    if re.findall(r'^#', string) == ['#']:
        return True
    return False


# find octothorpe in first line and def in second line
def octothorpe_first_line_def_second_line(lines):
    if len(lines) < 2:
        return False
    if find_octothorpe_in_string(lines[0]) and find_def_in_string(lines[1]):
        return True
    return False


def format_def_string(string):
    return string.replace('def ', '').replace('(', '').replace("\n", "")


def input_file_name():
    name = str(input("Введите имя файла: "))
    if name.find(" ") != -1:
        print("Имя файла не должно содержать пробелов")
        return input_file_name()
    if name == "":
        return None, False
    try:
        file = open(name, 'r', encoding='utf-8'), None
        return file
    except FileNotFoundError:
        print("Файл не найден")
        return input_file_name()


def task12_var1(file_name):
    return [print(i) for i in open(file_name, 'r').read().splitlines()[:10]]

def task12_var3(file_name, file_name2):
    return [print(i) for i in open(file_name, 'r').read().splitlines()],[print(i) for i in open(file_name2, 'r').read().splitlines()]
def task12_var5(file_name):
    return print(max([i for i in open(file_name, 'r').read().splitlines()],key=len))

def task12_var(file_name):
    while True:
        f = input_file_name()
        if f[1] == False:
            break
        lines = f[0].readlines()
        comented_defs, not_comented_defs, comented_defs_names, not_comented_defs_names = 0, 0, [], []

        for line1, line2 in zip(lines, lines[1:]):
            if find_def_in_string(line2):
                if octothorpe_first_line_def_second_line([line1, line2]):
                    comented_defs += 1
                    comented_defs_names.append(format_def_string(line2))
                else:
                    not_comented_defs += 1
                    not_comented_defs_names.append(format_def_string(line2))
        print(f"Коментированных функций: {comented_defs}")
        print(f"Не коментированных функций: {not_comented_defs}")
        print(f"Имена коментированных функции: {comented_defs_names}")
        print(f"Имена НЕкоментированных функций: {not_comented_defs_names}")
    f[0].close()
    pass

def task12_var7(file_name):
    from collections import Counter
    return print(Counter([i for i in open(file_name, 'r').read().splitlines()]).most_common(1))

def task12_var9():
    src = list(map(str, input().split()))
    print(src)
    src1=[]
    for i in src:
        if i.isdigit():
            src1.append(int(i))
            continue
        try:
            if i == "отл":
                src1.append(5)
            if i == "хор":
                src1.append(4)
            if i == "удол":
                src1.append(3)
        except ValueError:
            print("Неверный ввод")
    print(src1)





if __name__ == "__main__":
    task12_var7("staff_files/text.txt")
    task12_var9()


