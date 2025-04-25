def expand_around_center(route, left, right):
    n = len(route)
    max_len = 0
    while left >= 0 and right < n and route[left] == route[right]:
        curr_len = right - left + 1
        if curr_len > max_len:
            max_len = curr_len
        left -= 1
        right += 1
    return max_len

def count_best_route(n, route):
    max_len = 0

    for center in range(n):
        length_odd = expand_around_center(route, center, center)
        if length_odd > max_len:
            max_len = length_odd

        length_even = expand_around_center(route, center, center + 1)
        if length_even > max_len:
            max_len = length_even

    return max_len if max_len >= 2 else 0


def main():
    n = int(input())
    route = list(map(int, input().split()))
    result = count_best_route(n, route)
    print(result)


if __name__ == "__main__":
    main()