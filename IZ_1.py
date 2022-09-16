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


def entry_16_not_end_A(list_of_pairs):
    out = 0
    out += max(list_of_pairs[0][0], list_of_pairs[0][1])
    for i in list_of_pairs:
        test_out = out
        test_out += max(i[0], i[1])
        if hex(test_out)[-1] == 'a':
            out += max(i[0], i[1])
        else:
            out += min(i[0], i[1])
    return out


if __name__ == "__main__":
    out_a = entry_16_not_end_A(get_pair_digs("4a.txt"))
    out_b = entry_16_not_end_A(get_pair_digs("4b.txt"))
    print(out_a, out_b)
    print(hex(out_a), hex(out_b))
    print(get_max_sum(get_pair_digs("4a.txt")), get_max_sum(get_pair_digs("4b.txt")))
