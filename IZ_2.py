class Polynomial:

    def __init__(self, degree, coefficient):
        self.degree = degree
        self.coefficient = coefficient

    def __str__(self):
        # for the start we get list with strings where we contain
        # information about every term, each string looks like this:
        # "±a*x^b" where a is coefficient[i] and b is degree-i
        # we construct the certain string with the polynomial
        # and print it in console
        if self.coefficient == "Error":
            print(self.coefficient)
            return ""
        rez = self.build_Polynomial(True)
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

    def write_Poynomial_in_file(self, file_name, type_write):
        rez = self.build_Polynomial(False)
        with open(file_name, type_write, encoding="utf-8") as f:
            for i in range(len(rez)):
                if i == 0:
                    f.write(rez[i])
                    continue
                if i == len(rez):
                    continue

                if rez[i][0] == '-':
                    f.write(rez[i].replace("-", " - "))
                else:
                    f.write(" + " + rez[i])
            f.write("\n")

    def build_Polynomial(self, console):
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
            # if we print in console we use termcolor
            # to make the output more beautiful
            # (i specialy use this library, and not use standart colors codes
            # cuz it looks awful)
            if console:
                from termcolor import colored
                text2 = colored(f"{self.degree - i}", 'red')
            else:
                text2 = f"{self.degree - i}"
            rez_arr += [text1 + text2]
            i += 1
        return rez_arr  # ['±a[0]*x^(b-0)', '±a[1]*x^(b-1)', ...]

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
    fg_x.write_Poynomial_in_file("rez.txt", "a")
