# Домашняя работа 4

from random import randint
    
# Задача 22:

# Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа.
# n - кол-во элементов первого набора.
# m - кол-во элементов второго набора.
# Значения генерируются случайным образом.

# Input: 11 6
# (значения сгенерированы случайным образом [2 4 6 8 10 12 10 8 6 4 2] и  [3 6 9 12 15 18])
# Output: 11 6
# 6 12

# n = int(input('введите кол-во элементов первого набора: '))
# arrayN = [randint(0, 30) for i in range(0, n)] # создаем первый набор
# m = int(input('введите кол-во элементов второго набора: '))
# arrayM = [randint(0, 30) for i in range(0, m)] # создаем второй набор
# print(f'{arrayN}\n{arrayM}') 

# arrayN.sort()
# arrayM.sort()

# temp = -999
# arrayEnd = []

# if n >= m and n > 0 and m > 0: # ищу совпадения по набору с наименьшим количеством элементов
#     for i in arrayM:
#         for j in arrayN:
#             if i == j and temp < j:
#                 temp = j
#                 arrayEnd.append(temp)
# else:
#     for i in arrayN:
#         for j in arrayM:
#             if i == j and temp < j:
#                 temp = j
#                 arrayEnd.append(temp)

# if not arrayEnd:
#     print(f'в наборах нет совпадений')
# else:
#     print(f'в наборах найдены совпадения чисел {arrayEnd}')


# Задача 24:
# В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке, причем кусты высажены только 
# по окружности. 
# Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растет N кустов. Эти кусты обладают 
# разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод – на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из управляющего модуля 
# и нескольких собирающих модулей. 
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и 
# с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль, 
# находясь перед некоторым кустом заданной во входном файле грядки.

# Input: 4
# (значения сгенерированы случайным образом [4 2 3 1] )
# Output: 9

bushes = int(input('введите кол-во элементов первого набора: '))
blueberryBushes = [randint(0, 10) for i in range(0, bushes)] # создаем грядку
print(blueberryBushes)
blueberryBushes = blueberryBushes + blueberryBushes[:2] # добавляем два первых символа в конец массива

harvest = 0
for i in range(bushes):
    harvest = max(harvest, blueberryBushes[i] + blueberryBushes[i+1] + blueberryBushes[i+2]) # функцией max сравниваем максимальное значение первого аргумента с результатом вычисления
print(f'собран урожай: {harvest}')






# Домашнее задание Семинар 5* (сдавать только к семинару 5!)

# Задача 26:  
# Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.

# Задача 28:
# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. Из всех арифметических операций допускаются только +1 и -1. 
# Также нельзя использовать циклы.


# Задачи на повторение по материалам предыдущих семинаров (по желанию)
# Задача 101 Вычислить число π c заданной точностью d

# Пример: 
# при d = 0.001, π = 3.141    0.1 ≤ d ≤ 0.00000000001

# Задача 102 Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

# Задача 103 Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл file1.txt многочлен степени k.

# Пример:  k=2 

# Возможные варианты многочленов:
# 2*x*x + 4*x + 5 = 0 
# x*x + 5 = 0 
# 10*x*x = 0

# Задача 104. Даны два файла file1.txt и file2.txt, в каждом из которых находится запись многочлена (полученные в результате работы программы из задачи 103). 
# Необходимо сформировать файл file_sum.txt, содержащий сумму многочленов.

# Задача 105 Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

# Задача 106 Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента? (Добавьте игру против бота)

# Задача 107 Создайте программу для игры в ""Крестики-нолики"" (Добавьте игру против бота)

# Задача 108 Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных (модуль в отдельном файле, импортируется как библиотека)
# метод Упаковка: на вход подается текстовый файл, на выходе текстовый файл со сжатием.
# метод Распаковка: на вход подается сжатый текстовый файл, на выходе текстовый файл восстановленный.
# Прикинуть достигаемую степень сжатия (отношение количества байт сжатого к исходному).