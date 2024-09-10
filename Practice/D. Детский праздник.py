

def f(n, t, y, z, m, mid):
    counter = 0

    for i in n:
        time = mid
        #t[i] - за сколько надувает шар i-ый надувающий
        #z[i] - сколько шаров надувает i-ый надувающий подряд
        #y[i] - отдых между подходами

        local_counter = mid // (t[i] * z[i] + y[i]) # полные циклы
        left = mid - (t[i]*z[i]+y[i])* local_counter # сколько минут осталось после полных итераций,
        counter += local_counter * z[i] + min(left // t[i], z[i])
    return counter >= m


def main():
    m  = int(input()) # кол-во шариков
    n = int(input()) # кол-во человек
    t = list() # время надувания шарика
    y = list() # после этого количества шариков отдыхает
    z = list() # время отдыха

    l = -1
    r = n * t[0] + (m/z[0]+1)*y[0]+1

    while r - l > 1:
        mid = l + (r - l) // 2
        #  минимизируем время
        # true - если можно надуть m шариков за mid секунд
        if f(n, t, y, z, m, mid):
            r = mid
        else:
            l = mid

    for i in range(n):
        local_counter = r // (t[i] * z[i] + y[i])  # полные циклы
        left = r - (t[i] * z[i] + y[i]) * local_counter  # сколько минут осталось после полных итераций,
        value = min(m, local_counter * z[i] + min(left // t[i], z[i]))
        n -= value

    return r


if __name__ == "__main__":
    print(main())
