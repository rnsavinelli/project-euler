#!/usr/bin/python3

def is_prime(number: int) -> (bool):
    if (number <= 1) :
        return False
    if (number <= 3) :
        return True

    if (number % 2 == 0 or number % 3 == 0) :
        return False

    i: int = 5
    while(i * i <= number) :
        if (number % i == 0 or number % (i + 2) == 0) :
            return False
        i = i + 6

    return True

def solve(amount_of_primes: int) -> (int):
    primes_found: int = 0

    number: int = 0
    while primes_found < amount_of_primes:
        if is_prime(number):
            primes_found += 1
            print(number)
        number += 1

if __name__ == '__main__':
    solve(10001)