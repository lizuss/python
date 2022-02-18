# #Задание 1
# a = int(3)
# b = int(2)
# c = a+b
# print (c)
# a=int(input("A = "))
# b=int(2)
# c=a+b
# print (c)
# print(a)
# f = str("hello")
# print (f)

# # Задание 2
#
# time= int (input ("Напишите время в секундах: "))
# hours= time // 3600
# minutes = (time- hours*3600)//60
# seconds = time - (hours * 3600 + minutes * 60)
# print (f"time {hours}:{minutes}:{seconds}")

#
# # Задание 3
# n=(input("n="))
# x1 = int(n)
# x2 = int(n+n)
# print (x2)
# x3 = int(n+n+n)
# print (x3)
# x=x1+x2+x3
# print(x)

# # Задание 4
# a = int(input("Введите целое положительное число"))
# m = a%10
# a = a//10
# while a > 0:
#
#     if a%10 > m:
#         m = a%10
#     a = a//10
# print (m)


# # Задание 5-6
# revenue= float(input("Введите выручку компании "))
# costs = float(input("Введите издержки фирмы "))
# if revenue > costs:
#    print(f"Фирма работает с прибылью. Рентабельность выручки составила {revenue / costs}")
#    workers = int(input("Введите количество сотрудников фирмы "))
#    print(f"прибыль в расчете на одного сотрудника составила {revenue / workers}")
# elif revenue == costs :
#
#     print ("в ноль")
# else:
#     print ("в убыток")