#!/usr/bin/python3

def square_of_the_sum(number: int) -> (int):
    solution: int = 0

    for i in range(1, number+1):
        solution += i

    return solution ** 2

def sum_of_squares(number: int) -> (int):
    solution: int = 0

    for i in range(1, number+1):
        solution += i ** 2

    return solution

def solve(number: int) -> (int):
    return square_of_the_sum(number) - sum_of_squares(number)

if __name__ == '__main__':
    print(solve(100))