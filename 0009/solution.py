#!/usr/bin/python3

def solve() -> (int):
    solved: bool = False

    a: int = 0
    b: int = 0
    c: int = 0

    while not solved:
        a += 1

        first_equation_solved: bool = False

        c = a
        while not first_equation_solved and c <= 1000 - a - b:
            c += 1


            first_equation: int = (2 * (a + c) * (a - 1000)) + (1000 ** 2)

            if first_equation == 0:
                first_equation_solved = True
                solved = True


    for b in range(a + 1, c):
        if a + b + c == 1000:
            break

    print("a = ", a)
    print("b = ", b)
    print("c = ", c)

    return a * b * c

if __name__ == '__main__':
    print(solve())

