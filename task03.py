# 3 Реализуйте алгоритм перемешивания списка. Встроенный алгоритм SHUFFLE не использовать!
# Реализовать свой метод
from random import randint
import random

size = int(input("Введите размер списка "))
min = int(input("Введите границы значений элементов списка: min = "))
max = int(input("Введите границы значений элементов списка: max = "))
my_list = []
for i in range(size):
    my_list.append(randint(min, max))
print(f'Список: {my_list}')
count = random.randint(3, 100)           #Кол-во смены элементов в списке
for i in range(count):
    index1 = random.randint(0, size-1)   #Рандомный индекс для смены
    index2 = random.randint(0, size-1)   #Второй рандомный индекс для смены
    value = my_list[index1]
    my_list[index1] = my_list[index2]
    my_list[index2] = value
print(f'Перемешанный список: {my_list}')
