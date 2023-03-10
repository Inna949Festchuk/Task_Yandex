import re
# text = "Что такое Регулярные выражения и как их использовать? Говоря простым  языком, регулярное     выражение — это последовательность символов, используемая для   поиска и замены текста в строке или файле! Как уже было упомянуто, \nих   поддерживает множество языков общего назначения: Python, Perl, R. Так что изучение регулярных выражений рано или поздно пригодится."

# # Пример работы  findall, match, search
# pattern = r"регулярн\w*\s+выражен\w*"
# result = re.findall(pattern, text, re.I) # где re.I - устанавливает ФЛАГ поиск регистра
# print(result)

# # Замена фразы
# result = re.sub(pattern, "RegEx", text)
# print(result)

# Напишите регулярное выражение, 
# которое позволяет выделить все 
# строки отвечающие условиям:
# Состоят только из букв
# Одна и только одна из букв является заглавной

txt = "bOnd007", "Bond", "ёЁ", "Мама", "авТо", "гриБ", "Яблоко", "яБлоко", "ябЛоко", "яблОко", "яблоКо", "яблокО", "агент007", "стриж", "ГТО", "Три богатыря"

for x in txt:
    c = re.findall(r"(^[а-яёa-z]*[А-ЯЁA-Z][а-яёa-z]*)$", x)
    print(c)

# если разбирать паттерн, то логика такая - строка может начинаться со строчных 
# символов (кириллица или латиница) в кол-ве от нуля до бесконечности [а-яёa-z]*, 
# далее должны встречаться прописные символы в кол-ве не более одного [А-ЯЁA-Z], 
# ну и после прописного символа должны быть только строчные в любом кол-ве 
# от нуля до бесконечности[а-яёa-z]*
# ^ - начало строки
# $ - конец строки

# Ссылки на тренировки
# https://regex101.com/
# https://habr.com/ru/post/349860/
# Ссылки на таблицы кодировок
# https://wiki.iarduino.ru/page/encoding-arduino/