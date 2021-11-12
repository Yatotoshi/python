# Посчитать количество вхождений введенного символа в веденной
# строке

in_str = input('Введите строку: ')
sym = input('Введите символ: ')
count = 0

for c in in_str:
    if c == sym:
        count = count + 1

print(count)
