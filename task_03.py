# Задайте список из n чисел последовательности
# (1 + 1/n)^n и выведите на экран их сумму.

# Пример:

# - Для n=4 {1: 2, 2: 2.25, 3: 2.37, 4: 2.44}
#   Сумма 9.06


n = int(input('Введите число '))
nums = {}
for i in range(1,n+1):
    nums[i] = round((1+1/i)**i,2)
print(nums)
print('Cумма = ', sum(nums.values()))



# n = int(input('Введите число '))
# print('для','n','=',n,'{ ', end=(' '))
# sum=0
# for i in range(1, n+1):
#     num = (1+1/i)**i
#     sum = sum+num
#     print(i, ':', round(num, 2), '', end=(' '))
# print('}')
# print('Cумма = ',round(sum, 2))
