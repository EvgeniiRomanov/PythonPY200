# Заполнить список ста нулями, кроме первого и последнего элементов, которые должны быть равны единице;
import random
from random import *

list_ = []
list_.append(1)
for i in range(1, 99):
    list_.append(0)
list_.append(1)

print(len(list_), list_)
#------------------------------------------------------------
#Сформировать возрастающий список из чётных чисел (количество элементов 45);

list1 = []
for i in range(0, 91, 2):
    list1.append(i)

list1.clear()
# или так
for i in range(0, 90):
    if i % 2 == 0:
        list1.append(i)

print(len(list1), list1)

#Пользователь вводит число. Определить, содержит ли список данное число x. Если содержит,
# то вывести на экран число 7145, если не содержит, то вывести на экран число 5741;

# list2 = [k for k in range(1, 10)]
# print(list2)
# x = int(input("Введите число:"))
# if x in list2:
#     print("7145")
# else:
#     print("5741")

# Найдите сумму и произведение элементов списка. Результаты вывести на экран
list3 = [randrange(1, 100) for i in range(3)]
k = 1
print(list3)
for i in range(len(list3)):
    k = k * list3[i]

print(sum(list3), k)

#Найти наибольший элемент списка и вывести его на экран
list4 = [randrange(1, 100) for i in range(5)]
print(list4)
print(max(list4))

#Определите, есть ли в списке повторяющиеся элементы, если да, то вывести на экран это значение
list5 = [5, 7, 8, 43, 5, 78, 8, 100]
list6 = []
def count_list(x):
    if list5.count(x) > 1:
        if x in list6:
            return None
        else:
            list6.append(x)

print(list(filter(count_list, list5)))
print(list6)

#Поменять местами самый большой и самый маленький элементы списка;
list7 = [randrange(1, 100) for i in range(10)]
print(list7)
max_ind = list7.index(max(list7))
min_ind = list7.index(min(list7))
print(max_ind, min_ind)
list7[max_ind], list7[min_ind] = list7[min_ind], list7[max_ind]
print(list7)