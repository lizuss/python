# #Задание 1 (дз-3)
#
# def div(*args):
#
#     number1 = int(input('Напишите первое число: '))
#     number2 = int(input('Напишите второе число: '))
#
#     if number2 == 0 :
#         res = "На о делить нельзя"
#     else:
#         res = number1 // number2
# #     return res
# # print(div())
#
# # Задание 2
#

# def pinfo():
#     name = input('Enter name')
#     surname = input('Enter surname')
#     year = int(input('Enter year'))
#     city = input('Enter city')
#     email = input('Enter email')
#     mobile = input()
#
#     return name, surname, year, city, email, mobile
# print(pinfo())


# #Задание 3
#
# def my_func():
#     arg1 = int(input('Напишите аргумент 1 : '))
#     arg2 = int(input('Напишите аргумент 2 : '))
#     arg3 = int(input('Напишите аргумент 3 : '))
#     if arg1 >= arg3 and arg2 >= arg3:
#         return arg1 + arg2
#     elif arg1 > arg2 and arg1 < arg3:
#         return arg1 + arg3
#     else:
#         return arg2 + arg3
# print(my_func())


# Задание 4
# Первый вариант решения
# def degree(x,y):
#     # x= int( input( 'Напишите число:' ))
#     # y=int(input('Напишите степень по модулю:'))
#     if y==0:
#         return 1
#     else:
#         return pow(x,y)
# print(degree(5,3))

# # Второй вариант решения через цикл
# def degree(x,y):
#     if y == 0:
#         return 1
#     else:
#         return 1/ x* degree(x,y-1 )
#
# x = float(input('Напишите число: '))
# y = int(input('Напишите степень: '))
# print(degree(x, y))

# Третий вариант решения

# def degree (x,y):
#     if y == 0:
#         return 1
#     else:
#         return x**y
# x = float(input('Напишите число: '))
# y = int(input('Напишите степень: '))
# print(degree(x, y))

# Задание 5
#
# def s_num():
#     sum=0
#     while True:
#         li = input('Введите числа: ').split()
#         for el in li:
#
#             if  el== 'stop':
#                 print(sum)
#                 return
#             else:
#                 sum = int(sum) + int(el)
#         print (sum)
#
# s_num()
#
#Задание 6
#
def int_func(user_text):
    return user_text.capitalize()

# print(int_func('text'))

# Задание 7

def int_func2(user_text):
    z=''
    user_text= user_text.split()
    for i in user_text:
        i = int_func(i)
        z=z+i+( " ")
    return z

print(int_func2('text  fbrb frvr'))


