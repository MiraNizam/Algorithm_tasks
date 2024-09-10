"""
С. Очень легкая задача
"""


def f(n, x, y, mid):
    first_copy = min(x, y)
    if first_copy > mid:
        return False
    mid -= first_copy
    n -= 1

    counter = mid/x + mid/y

    return counter >= n


def main():
    n = int(input())
    x = int(input())
    y = int(input())

    l = 0
    r = min(x, y)*n + 1

    while r - l > 1:
        mid = l + (r - l) // 2
        if f(n, x, y, mid):
            r = mid
        else:
            l = mid
    return r


if __name__ == "__main__":
    print(main())

