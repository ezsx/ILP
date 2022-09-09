from random import randint


def test_list():
    lst = [randint(1, 10) for i in range(5)]
    print(lst)
    return lst


def task10_var1():
    print(len(set(test_list())))


def task10_var2():
    print(len(set(test_list()) & set(test_list())))


def task10_var3():
    print(sorted(set(test_list()).intersection(set(test_list()))))


def task10_var4():
    lst = test_list()
    s_lst = set(lst)
    for i in s_lst:
        if lst.count(i) > 1:
            print(f"{i} YES")
        else:
            print(f"{i} NO")


def task10_var5():
    kub1 = set(test_list())
    kub2 = set(test_list())
    print(kub1 & kub2)
    print(kub1 - kub2)
    print(kub2 - kub1)


def task10_var6():
    import requests

    word_site = "https://www.mit.edu/~ecprice/wordlist.10000"

    response = requests.get(word_site)
    WORDS = response.content.split()  # .splitlines()

    def generate_word():
        return WORDS[randint(0, len(WORDS))].decode("utf-8")

    def generate_str():
        return [generate_word() for i in range(randint(1, 10))]

    def generate_list_str():
        return [generate_str() for i in range(randint(1, 10))]

    inp = generate_list_str()
    set_all_words = set()
    for i in inp:
        set_all_words.update(i)
    print(set_all_words)
    print(len(set_all_words))

    pass


def task10_var7():
    # загаданное число
    n = randint(10, 10)
    set_a = set([i for i in range(1, n)])
    # выбранные числа
    from random import choice
    saved_rand = randint(3, 7)
    list_ans = [choice(["YES", "NO"]) for i in range(saved_rand)]
    list_sets = [set(test_list()) for i in range(saved_rand)]
    print("____________________________________________________")
    print(set_a, " делаем множество от загаданного числа")
    print(list_sets, " делаем множество от выбранных чисел")
    print(list_ans, " ответы на вопросы")

    for i in list_sets:
        if list_ans[list_sets.index(i)] == "YES":
            set_a = set_a & i
        else:
            set_a = set_a - i
        if len(set_a) == 0:
            break
    print(set_a)

    pass


def task10_var8():
    # загаданное число
    n = randint(7, 12)
    set_a = set([i for i in range(1, n)])
    saved_rand = randint(3, 7)
    list_sets = [set(test_list()) for i in range(saved_rand)]
    print("____________________________________________________")
    print(list_sets)
    print(set_a)
    for i in list_sets:
        if len(i) > len(set_a) / 2:
            set_a = set_a & i
            print(f"YES {set_a}")
        else:
            set_a = set_a - i
            print(f"NO {set_a}")

        if len(set_a) == 0:
            break
    print(set_a)


def task10_var9():
    n = randint(7, 15)
    languages = ["english", "french", "german", "spanish", "italian", "russian", "china", "japan", "korea", "india",
                 "arab", "turk", "portugal", "poland", "ukraine", "belarus", "bulgaria", "czech", "hungary", "romania",
                 "sweden", "finland", "norway", "denmark", "netherlands", "belgium", "luxembourg", "switzerland",
                 "austria", "greece", "turkey", ]

    from random import choices
    list_languages = [set(choices(languages, k=randint(1, len(languages)))) for i in range(n)]
    print(list_languages)
    min_languages = languages
    all_languages = set()
    for i in list_languages:
        if len(i) < len(min_languages):
            min_languages = i
        all_languages.update(i)

    print(min_languages)
    print(all_languages)


def task10_var10():
    # N, K = [int(s) for s in input().split()]
    # work_days = set([day for day in range(1, N + 1) if day % 7 not in (6, 0)])
    # no_strikes = set(work_days)
    # for party in range(K):
    #     a, b = [int(s) for s in input().split()]
    #     max_strikes = (N - a) // b + 1
    #     no_strikes -= {a + b * i for i in range(max_strikes)}
    # print(len(work_days) - len(no_strikes))

    N = randint(50, 1000)
    K = randint(5, 15)
    bast_list = [set([i for i in range(randint(1, N - 1), N, randint(5, 20)) if i % 7 not in (6, 0)]) for j in range(K)
                 if j != 0]
    work_days = set([day for day in range(1, N) if day % 7 not in (6, 0)])
    print(work_days)
    print(len(work_days))
    print(bast_list)

    not_or = set()
    for i in bast_list:
        work_days = work_days - i
        not_or = not_or ^ i

    print(work_days)  # без забастовок совсем
    print(not_or)  # только с 1 забастовкой
    print(work_days | not_or)  # без забастовок или только с 1 забастовкой
    print(len(work_days | not_or))  # ответ


def task11_var4():
    from collections import Counter

    text = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt
    ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris
    nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit
    esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt
    in culpa qui officia deserunt mollit anim id est laborum."""

    text2 = "some text to test algorithm for task 11 var 4 done by me and my friend in 2020 year with love love love very much thanks for all and good luck to all my friends and family and all people in the world"

    myLine = text.split()  # split() без аргументов делит по пробельным символам, в том числе и по переносам строк
    d = Counter(myLine)  # один проход с подсчетом в словаре - примерно O(n)
    max_encounters = max(d.values())  # нахождение максимума - О(n)
    most_common_word = min(word for word, count in d.items() if
                           count == max_encounters)  # нахождение минимального из максимально частых слов O(n*m) (m - количество самых частых слов)
    print(most_common_word)  # получаем слово "in"

    # или получаем список через d.most_common(1) и выводим первый элемент списка

    print(d) # сам список для наглядности


if __name__ == "__main__":
    # task10_var1()
    # task10_var2()
    # task10_var3()
    # task10_var4()
    # task10_var4()
    # task10_var5()
    # task10_var6()
    # task10_var7()
    # task10_var8()
    # task10_var9()
    # task10_var10()
    task11_var4()
    pass
