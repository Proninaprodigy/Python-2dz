# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

num = float(input("Введите число: "))
sum = sum(map(int,str(abs(num)).replace(".","")))
print(sum)

#Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

n = int(input("Введите число: "))
i = 1
fact = 1
while i <= n:
    fact *= i 
    print(fact)
    i += 1

# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных пользователем через пробел позициях.

n = int(input("Введите число: "))
from random import randint
arr = []
for i in range (n):
    arr.append(randint(-n, n))
print(arr) 

s = input("Введите через пробел позиции элементов, произведение которых вы хотите посчитать: ")
import math  
arr2 = [int(x) for x in s.split()]
arr3 = []
for k in range (len(arr2)):
    arr3.append(arr[arr2[k]])
print(math.prod(arr3))

# Реализуйте алгоритм перемешивания списка

import random
list = [1, 2, 3, 4, 5]
random.shuffle(list)
print(list)

# Задайте список из k чисел последовательности (1 + 1\k)^k и выведите на экран их сумму.

s = int(input('Введите число k для (1+1/k)^k : '))
result = list((1+1/i)**i for i in range(1, s + 1))
print(f'Сумма чисел = {round(sum(result), 3)}')