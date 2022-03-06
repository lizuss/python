#ДЗ-2
#Задание 1
# #
# li = [12,13,"hello","hey"]
# print(li)
# for n in li:
#     print(type(n))

#
# # print(type (li[0]))
# # print( type(li[-1]))

#Задание 2
# С заданием 2 не справилась, оставляю примеры попыток

# li = input ("Напишите список: ").split()
# il1= []

# # for n in range(0,len(il1)//2):
# #     il1.append(il[2*n+1])
# #     il1.append(il[2*n])
#
# li[::2],li[1::2] = il1 [1::2], il1 [::2]
# print(il1)

#Задание 3

# mounth = { 'winter':[1, 2, 12], 'Spring': [3, 4, 5],'summer': [6, 7, 8] , 'autumn': [9, 10, 11]}
# num = int(input('Напишите номер месяца: '))
# for n in mounth:
#     if num in mounth[n]:
#         print(n)

#Задание 4

# li = input ("Напишите несколько слов: ").split()
# for n,  word in enumerate (li, 1) :
#     if len(word) >= 10:
#         print(n, word [:10])
#     else :
#         print(n, word)

#задание 5
my_list = [7, 5, 3, 3, 2]
my_list.append(int(input("Введите натуральное число: ")))
print(sorted(my_list)[::-1])



