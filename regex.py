import re
text = "Что такое Регулярные выражения и как их использовать? Говоря простым  языком, регулярное     выражение — это последовательность символов, используемая для   поиска и замены текста в строке или файле! Как уже было упомянуто, \nих   поддерживает множество языков общего назначения: Python, Perl, R. Так что изучение регулярных выражений рано или поздно пригодится."

# Пример работы  findall, match, search
pattern = r"регулярн\w*\s+выражен\w*"
result = re.findall(pattern, text, re.I) # где re.I - устанавливает ФЛАГ поиск регистра
print(result)

# Замена фразы
result = re.sub(pattern, "RegEx", text)
print(result)