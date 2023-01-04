'''Поиск простых чисел'''
nn = input('Введите натуральное число: ')
lpn = []
for n in range(2, int(nn)):
    if int(n) == 2:
        prime_number = n
    for k in range(2, int(n)): # составное число
        if int(n) % k == 0:
            prime_number = ''
            break
        elif int(n) % k != 0: # простое число
            prime_number = n
    lpn.append(prime_number)        
print(lpn)