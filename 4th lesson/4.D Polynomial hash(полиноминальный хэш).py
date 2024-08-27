"""
D. Полиномиальный хеш
"""
a = int(input())
m = int(input())
s = input()


def polynominal_hash(a, m, s):
    a_in_power = 1
    h = 0

    for i in s[::-1]:
        h = (h + ord(i)*a_in_power) % m
        a_in_power = a*a_in_power % m # вариант a_in_power *= a % m будет забирать доп.время
    return h


if __name__ == "__main__":
    print(polynominal_hash(a, m, s))

