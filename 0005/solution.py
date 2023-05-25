#!/usr/bin/python3

def solve(number: int) -> (int):
    solution: int = 0;
    solved = False

    while not solved:
        solution = solution + 1

        for i in range(1, number+1):
            if not(solution % i == 0):
                break
            else:
                if i == number:
                    solved = True

    return solution

if __name__ == '__main__':
    print(solve(20))
