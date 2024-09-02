"""
A. Поисковая система

-- ПРИНЦИП РАБОТЫ --
все строится на работе со словарями и выбором индекса, для дальнейшей итерации. Сначала мы обрабатываем входящий поток
информации. Подсчитываем слова в документах, вытаскиваем из запроса слова, которые будем подсчитывать по документу.
Работа с документом, создается defaultdict с defaultdict внутри. Ключом внешнего словаря является слова, ключом
внутреннего индекс номер документа, значением кол-во вхождений в документ. На этом предварительная работа с документом
заканчивается. После слова из запроса итерируются по индексам собирая информацию по кол-ву слов в документе. Полученная
информация сортируется и выводится топ-5 элементов.

-- ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ --
Словари подсчитывают по циклам всю полученную информацию и передают дальше. Сортировка итоговых данных делается сначала
по убыванию веса, потом по возрастанию индекса документа

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --

Средняя временная сложность составления поискового индекса - О(n*w)
Средняя временная сложность выполнения всех запросов - О(q*m)
Средняя временная сложность сортировки - О(qlogq)
Средняя временная сложность всего алгоритма - О(n*w + (q*m+qlogq)), где
n - количество документов,
m - количество запросов к поисковому индексу,
w - среднее количество слов в документе,
q - среднее количество слов в запросе.

-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
логика подсчета: мы храним все слова по всем документам, храним слова по запросам и дополнительно создаем defaultdict, он содержит слова
всех документов поэтому охота добавить еще + n*w, тогда сложность О(2n*w + m*q), константу опускаем.

Пространственная сложность - О(n*w + m*q)

-- ID успешной посылки --
https://contest.yandex.ru/contest/24414/run-report/117308327/

"""

from collections import Counter, defaultdict


def create_document_index(documents):
    indexes = defaultdict(lambda: defaultdict(int))

    for doc_index, document in enumerate(documents, start=1):
        for word, count in document.items():
            indexes[word][doc_index] += count
    return indexes


def calculate_document_weight(indexes, request):
    document_weights = defaultdict(int)
    for word in request:
        if word in indexes:
            for doc_index, count in indexes[word].items():
                document_weights[doc_index] += count
    return list(document_weights.items())


def main():
    no_docs = int(input())
    documents = [Counter(input().split()) for _ in range(no_docs)]

    requests_no = int(input())
    requests = [set(input().split(" ")) for _ in range(requests_no)]

    indexes = create_document_index(documents)

    for request in requests:
        request_result = calculate_document_weight(indexes, request)

        top_result = sorted(request_result, key=lambda x: (-x[1], x[0]))[:5] # Сортировка итоговых данных делается
        # сначала по убыванию веса, потом по возрастанию индекса документа
        print(" ".join([str(i[0]) for i in top_result]))


if __name__ == "__main__":
    main()
