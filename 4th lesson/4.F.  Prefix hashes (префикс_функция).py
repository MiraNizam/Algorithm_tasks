"""
F. Префиксные хеши
"""


def compute_prefix_hashes(a, m, s):
    n = len(s)
    h = [0] * (n + 1) # собираем хеши префиксов, h[0] = 0 - это будет удобно для подсчета h в цикле
    a_in_power = [1] * (n + 1) # собираем степени коэффициента a

    for i in range(1, n + 1):
        h[i] = (h[i-1] * a + ord(s[i-1])) % m # по методу Горнера высчитываем хеши всех префиксов
        a_in_power[i] = (a_in_power[i-1] * a) % m # собираем степени а, по модулю. т.к. иначе будет потрачено много памяти
    return h, a_in_power


def get_substring_hash(h, a_in_power, m, l, r):
    """ Разберем как происходит вычисление подстроки x = [5, 8]
    получаем информацию:

    h[r] = h[8] = h["abcdefgh"] = 436420
    h[l - 1] = h[5 - 1] = h["abcd"] = 873887
    a_in_power[r-l+1] = a_in_power[8-5+1] = 81
    h[x] = h[5, 8] = h("efgh") = (h["abcdefgh"] - h["abcd"] * 81) % 1000009 = (436420 - 225227 * 81) % 1000009 = 193195

    """
    return (h[r] - h[l - 1] * a_in_power[r-l+1]) % m # считаем хеши подстрок методом скользящего окна, используя префиксные хеши, которые собрали ранее.


def main():
    a = int(input())
    m = int(input())
    s = input()
    substring_numbers = int(input())
    h, a_in_power = compute_prefix_hashes(a, m, s)

    for _ in range(substring_numbers):
        start, stop = map(int, input().split(" "))
        print(get_substring_hash(h, a_in_power, m, start, stop))


if __name__ == "__main__":
    main()

