def get_pair_digs(file_name):
    return [list(tuple(j)) for j in
            [map(int, i.split()) for i in open(file_name, "r", encoding="utf-8").readlines()][1:]]


def entry_16_not_end_A(list_of_pairs):
    p1, sum_ = 10 ** 7, 0
    for i in list_of_pairs:
        sum_ += max(i[0], i[1])
        if hex(abs(i[0] - i[1]))[-1] != 'a':
            p1 = min(p1, abs(i[0] - i[1]))
    if hex(sum_)[-1] != 'a':
        return sum_
    else:
        return sum_ - p1
def rez_in_line(file_name):
    return sum([max(y[0], y[1]) for y in [list(tuple(j)) for j in [map(int, i.split()) for i in open(file_name,"r",encoding="utf-8").readlines()][1:]]]) if hex(sum([max(y[0], y[1]) for y in [list(tuple(j)) for j in [map(int, i.split()) for i in open(file_name,"r",encoding="utf-8").readlines()][1:]]]))[-1]!='a' else sum([max(y[0], y[1]) for y in [list(tuple(j)) for j in [map(int, i.split()) for i in open(file_name,"r",encoding="utf-8").readlines()][1:]]])-min([abs(x[0] - x[1]) for x in [list(tuple(j)) for j in [map(int, i.split()) for i in open(file_name,"r",encoding="utf-8").readlines()][1:]] if hex(abs(x[0] - x[1]))[-1] != 'a'])



if __name__ == "__main__":
    print("Адекватное решение:", entry_16_not_end_A(get_pair_digs("4a.txt")))
    print("Решение в строку:  ", rez_in_line("4a.txt"))
