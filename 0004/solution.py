#!/usr/bin/python3

def is_palindrome(s: str) -> (bool):
    return s == s[::-1]

def solve() -> (int):
    solution = int(0)

    for i in reversed(range(100, 1000)):
        for j in reversed(range(100, 1000)):
            product =  i * j
            if is_palindrome(str(product)):
                if product > solution:
                    solution = product

    return solution

if __name__ == '__main__':
    print(solve())
