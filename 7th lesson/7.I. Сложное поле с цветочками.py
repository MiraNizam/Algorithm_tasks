"""
I. Сложное поле с цветочками

построить свой маршрут. Надо дойти от левого нижнего до правого верхнего угла, а передвигаться она умеет только вверх
и вправо.

Формат ввода
В первой строке даны размеры поля n и m (через пробел). Оба числа лежат в диапазоне от 1 до 1000. В следующих n строках
задано поле. Каждая строка состоит из m символов 0 или 1 и завершается переводом строки. Если в клетке записана единица,
то в ней растет цветочек.

Формат вывода
Выведите в первой строке максимальное количество цветочков, которое сможет собрать Кондратина. Во второй строке выведите
маршрут в виде последовательности символов «U» и «R», где «U» означает передвижение вверх, а «R» – передвижение вправо.

Если возможных оптимальных путей несколько, то выведите любой.
"""


def field(n, m, matrix):
    dp = [[0] * m for _ in range(n)]
    dp_way = [[""] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            flower_count = int(matrix[i][j])
            if i == 0 and j == 0:
                dp[i][j] = flower_count
            elif i == 0:
                dp[i][j] = dp[i][j - 1] + flower_count
                dp_way[i][j] = "R"
            elif j == 0:
                dp[i][j] = dp[i - 1][j] + flower_count
                dp_way[i][j] = "U"
            else:
                if dp[i - 1][j] > dp[i][j - 1]:
                    dp[i][j] = dp[i - 1][j] + flower_count
                    dp_way[i][j] = "U"
                else:
                    dp[i][j] = dp[i][j - 1] + flower_count
                    dp_way[i][j] = "R"

    route = []
    x, y = n - 1, m - 1

    while x >= 0 and y >= 0:
        if x == 0 and y == 0:
            break
        elif dp_way[x][y] == "R":
            route.append("R")
            y -= 1
        elif dp_way[x][y] == "U":
            route.append("U")
            x -= 1

    return dp[n-1][m-1], ''.join(route[::-1])


def main():
    n, m = map(int, input().split())
    matrix = [input() for _ in range(n)]
    matrix.reverse()

    max_flowers, route = field(n, m, matrix)
    print(max_flowers)
    print(route)


if __name__ == "__main__":
    main()