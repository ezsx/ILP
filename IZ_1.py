def get_pair_digs(file_name):
    f = open(file_name, "r", encoding="utf-8")
    all_dig = []
    for line in f:
        all_dig += line.split()
    out = []
    for dig1, dig2 in zip(all_dig[1::2], all_dig[2::2]):
        out.append([int(dig1), int(dig2)])
    f.close()
    return out


def get_max_sum(list_of_pairs):
    out = 0
    for i in list_of_pairs:
        out += max(i[0], i[1])
    return out


def choose_max_in_list(list_of_pairs):
    out = []
    for i in list_of_pairs:
        if i[0] > i[1]:
            out += [i[0]]
        else:
            out += [i[1]]
    return out


def entry_16_not_end_A(list_of_pairs):
    # можно сделать все невероятно проще и быстрее
    # если последовательно получать данные
    # но так как я уже завел списки то вот так:
    from math import inf
    # берем максимальный элемент из всех пар
    max_16_not_end_A = choose_max_in_list(list_of_pairs)
    # если такой список не оканчивается на a, то возвращаем его
    if hex(sum(max_16_not_end_A))[-1] != 'a':
        return sum(max_16_not_end_A)
    else:
        # иначе меняем в списке минимальный элемент и запоминаем его чтоб снова не убрать
        while hex(sum(max_16_not_end_A))[-1] == 'a':
            deleted = []

            m_elem = min(max_16_not_end_A,  key=lambda x: x if x not in deleted else -inf)
            m_elem_index = max_16_not_end_A.index(m_elem)
            max_16_not_end_A[m_elem_index] = list_of_pairs[m_elem_index][0] + list_of_pairs[m_elem_index][1] - m_elem
            deleted.append(m_elem)
        return sum(max_16_not_end_A)


if __name__ == "__main__":
    out_a = entry_16_not_end_A(get_pair_digs("4a.txt"))
    out_b = entry_16_not_end_A(get_pair_digs("4b.txt"))
    print("Максимальная сумма не оканчивающаяся на а: ", hex(out_a)[2:], hex(out_b)[2:])
    print("                                           ", out_a, out_b, "\n")
    print("                       Максимальная сумма: ", hex(get_max_sum(get_pair_digs("4a.txt")))[2:],
          hex(get_max_sum(get_pair_digs("4b.txt")))[2:])
    print("                                           ", get_max_sum(get_pair_digs("4a.txt")),
          get_max_sum(get_pair_digs("4b.txt")))
