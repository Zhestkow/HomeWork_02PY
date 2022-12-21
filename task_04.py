# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.

import os
clear = lambda: os.system('cls')
clear()

import random as r

n = int(input('Введите число -> '))
num = [r.randint(-n,n) for i in range(n)]
print (num)
file = open("file.txt","r")
sum = 1
for i in file:
    sum*=num[int(i)]
print(sum)