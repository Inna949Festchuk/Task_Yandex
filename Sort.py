# Дан неупорядоченный массив из печатных ASCII символов
# Опишите своими словами (без кода и псевдокода) алгоритм сортировки, 
# позволяющий упорядочить этот массив по алфавиту за линейное время
# Необходимо описать действия на каждом шаге алгоритма
# Возможен ли стабильный вариант такого алгоритма сортировки?

def QuickSort(A):
    ''' Этот алгоритм, чаще называемый просто «быстрая сортировка» (англ. Quicksort) 
    придуман английским ученым Чарльзом Хоаром в 1960 году
    https://foxford.ru/wiki/informatika/bystraya-sortirovka-hoara-python,
    https://ru.wikipedia.org/wiki/%D0%91%D1%8B%D1%81%D1%82%D1%80%D0%B0%D1%8F_%D1%81%D0%BE%D1%80%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D0%BA%D0%B0
    A - строка символов ASCII '''
    import random
    if len(A) <= 1:
        return A
    else:
        q = random.choice(A)
        L = []
        M = []
        R = []
        for elem in A:
            if elem < q:
                L.append(elem) 
            elif elem > q: 
                R.append(elem) 
            else: 
                M.append(elem)
        return QuickSort(L) + M + QuickSort(R)

A = input('Введите сроку: ')
S = QuickSort(A)
print(S)

# Быстрая сортировка (Quick Sort)
# https://neerc.ifmo.ru/wiki/index.php?title=%D0%A1%D0%BE%D1%80%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D0%BA%D0%B8
# https://ru.wikipedia.org/wiki/%D0%91%D1%8B%D1%81%D1%82%D1%80%D0%B0%D1%8F_%D1%81%D0%BE%D1%80%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D0%BA%D0%B0
# 
# Быстрая сортировка (Quick Sort)
# Ввод: Строка неупорядоченных символов А
# Решение:
# Если количество элементов А <=  1 
#     Возврат: А
# Иначе
#     Рандомный выбор опорного элемента из А
#     Для элемента в А
#         Если элемент меньше (левее) опорного присвоить массиву L
#         Иначе если элемент больше (правее) опорного присвоить массиву R
#         Иначе присвоить опорный элемент массиву M
#     Возврат: сортированный массив L + M + сортированный массив R

# Этот алгоритм использует неустойчивое 
# разделение исходного массива на две части.  
# Чтобы сделать его стабильным нужно реализовать устойчивое разделение
# исходного массива. Применить вместо  "Быстрой сортировки", 
# "Сортировку слиянием" При этом  
# сначала осуществляется рекурсивное разделение исходного массива 
# на части до тех пор, пока в каждой части массива не окажется 
# один или ноль элементов (на каждом шаге рекурсии осуществляется 
# разделение пополам). После этого каждый полученный элемент 
# сравнивается с соседом и сливается с ним, 
# в конечном итоге, получается отсортированный массив.
# https://ru.wikipedia.org/wiki/%D0%A1%D0%BE%D1%80%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D0%BA%D0%B0_%D1%81%D0%BB%D0%B8%D1%8F%D0%BD%D0%B8%D0%B5%D0%BC#/media/%D0%A4%D0%B0%D0%B9%D0%BB:Merge-sort-example-300px.gif