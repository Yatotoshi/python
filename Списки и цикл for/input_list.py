# Ввести и вывести список. Длину списка пользователь вводит заранее.

list_len = int(input('Введите длину списка: '))

l = []
print('Введите список:')
for i in range(list_len):
    el = input()
    l = l + [el]

print(l)