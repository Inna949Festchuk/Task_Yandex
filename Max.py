# Дан массив неповторяющихся чисел, который был отсортирован, 
# а затем циклически сдвинут на неизвестное число позиций.
# Опишите без кода и псевдокода алгоритм поиска максимума в таком массиве
# Оцените сложность предложенного алгоритма
# Изменится ли сложность если массив содержит повторяющиеся числа?

def shift(lst, steps):
    # Циклический сдвиг https://younglinux.info/python/task/shift
    if steps < 0:
        steps = abs(steps)
        for i in range(steps):
            lst.append(lst.pop(0))
    else:
        for i in range(steps):
            lst.insert(0, lst.pop())
    # Поиск максимального (минимального) элемента в списке
    # http://krivaksin.ru/python-rabota-so-spiskami-osnovnyie-algoritmyi-pri-rabote-so-spiskom/       
    sorted(lst) # Сортировка списка
    maximum = lst[0]
    for i in range(1, len(lst)):
        if lst[i] > maximum: # Заменить на <, при поиске минимума
            maximum = lst[i]
    return lst, maximum

nums = [4, 4, 6, 1, 6, 4, 4, 1, 0, 15]
s = 4 
print(f'Исходный массив:\n {nums}',
      f'\nЦиклически сдвинутый на {s} позиции массив'
      f' и его максимум:\n {shift(nums, s)}')

# Оценка сложности алгоритма
# https://tproger.ru/articles/computational-complexity-explained/