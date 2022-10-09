class Polynomial:

    def __init__(self, degree, coefficient):
        self.degree = degree
        self.coefficient = coefficient

    def __str__(self):
        # gvnocode
        if self.coefficient == "Error":
            print(self.coefficient)
            return ""
        rez = self.build_Polynomial()
        for i in range(len(rez)):
            if i == 0:
                print(rez[i], end='')
                continue
            if i == len(rez):
                continue

            if rez[i][0] == '-':
                print(rez[i].replace("-", " - "), end='')
            else:
                print(" + " + rez[i], end='')
        return ""

    def build_Polynomial(self):
        from termcolor import colored
        rez_arr = []
        i = 0
        for a in self.coefficient:
            if a == 0:
                i += 1
                continue
            if self.degree - i == 0:
                rez_arr.append(str(a))
                continue
            text1 = f"{a}x^"
            text2 = colored(f"{self.degree - i}", 'red')
            rez_arr += [text1 + text2]
            i += 1
        return rez_arr

    def __getitem__(self, x):
        rez = 0
        for i in range(len(self.coefficient)):
            rez += self.coefficient[i] * (x ** (self.degree - i))
        return rez

    def __add__(self, other):
        if self.degree >= other.degree:
            step_i = self.degree - other.degree
            rez_arr = self.coefficient
            for i in range(len(other.coefficient)):
                rez_arr[i + step_i] += other.coefficient[i]

            return Polynomial(self.degree, rez_arr)
        else:
            return "Error"

    def __sub__(self, other):
        if self.degree >= other.degree:
            step_i = self.degree - other.degree
            rez_arr = self.coefficient
            for i in range(len(other.coefficient)):
                rez_arr[i + step_i] -= other.coefficient[i]

            return Polynomial(self.degree, rez_arr)
        else:
            return "Error"

    def __mul__(self, other):
        rez_arr = [0] * (self.degree + other.degree + 1)
        for i in range(len(self.coefficient)):
            for j in range(len(other.coefficient)):
                rez_arr[i + j] += self.coefficient[i] * other.coefficient[j]
        return Polynomial(self.degree + other.degree, rez_arr)


if __name__ == '__main__':
    # add Polynomials
    print("_add Polynomials_")
    f_x = Polynomial(4, [3, 0, -7, 1, -3])
    g_x = Polynomial(3, [2, 5, 3, -2])
    print(f_x)
    print(g_x)
    fg_x = f_x + g_x
    print(fg_x)
    # multiply Polynomials
    print("_multiply Polynomials_")
    f1_x = Polynomial(2, [2, -1, 1])
    g1_x = Polynomial(1, [3, -1])
    print(f1_x)
    print(g1_x)
    fg1_x = f1_x * g1_x
    print(fg1_x)
    print("_sub Polynomials_")
    # sub Polynomials
    print(f1_x)
    print(g1_x)
    fg11_x = f1_x - g1_x
    print(fg11_x)
    print("_count Polynomials_")
    # count Polynomials
    print(f1_x)
    print(f1_x[2])