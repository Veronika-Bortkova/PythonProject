# 1) написати прогу, яка вибирає зі введеної строки цифри і виводить їх через кому,
#
# наприклад:
#
# st = ‘as 23 fdfdg544’ введена строка
#
# 2,3,5,4,4        #вивело в консолі.

# string1 = input("Enter string ")
# num_list = [i for i in string1 if i.isdigit()]
# result = ", ".join(num_list)
# print(result)


# 2)написати прогу, яка вибирає зі введеної строки числа і виводить їх так, як вони написані
#
# наприклад:
#
#   st = ‘as 23 fdfdg544 34’ #введена строка
#
#   23, 544, 34              #вивело в консолі

# string1 = input("Enter string ")
# l = []
# st = ""
# for i in string1:
#     if i.isdigit():
#         st = st + i
#     else:
#         if st:
#             l.append(st)
#             st=""
# if st:
#     l.append(st)
# resalt = ", ".join(l)
# print(resalt)

# или как у преподавателя
# st = "as 23 fdfdg544 34"
# l_st = [my_num if my_num.isdigit() else " " for my_num in st]
# print(l_st)
# str_1 = "".join(l_st)
# str_2 =str_1.split()
# str_3 = ", ".join(str_2)
# print(str_3)


# 1) є строка:
#
# greeting = ‘Hello, world’
#
# записати кожний символ, як окремий елемент списку, і зробити його заглавним:
#
# [‘H’, ‘E’, ‘L’, ‘L’, ‘O’, ‘,’, ‘ ‘, ‘W’, ‘O’, ‘R’, ‘L’, ‘D’]

# greeting = "Hello, world"
# str = [i.upper() for i in greeting]
# print(str)


# 2) з діапазону від 0-50 записати тільки непарні числа, при цьому піднести їх до квадрату
#
# приклад:
#
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, …]

# res = [i**2 for i in range(51) if i%2 !=0]
# print(res)



# – створити функцію, яка виводить List

# def func1():
#     print("List")
#
# func1()
#
# – створити функцію, яка приймає три числа, та виводить та повертає найбільше.

# def func2(a,b,c):
#     l = [a,b,c]
#     print(max(l))
#
# func2(1,7,2)


# – створити функцію, яка приймає будь-яку кількість чисел, повертає найменше, а виводить найбільше
# def func3(*args):
#     l = list(args)
#     print(max(l))
#     return min(l)
#
# min1 = func3(1,2,3,4)
# print(min1)

# – створити функцію, яка повертає найбільше число з List

# def func4(list1):
#     if isinstance(list1, list):
#         return max(list1)
#     else: print("Enter List")
#
# res = func4([1,2,3,4])
# print(res)
#
# func4(1)


# – створити функцію, яка повертає найменше число з List
# def func5(list1):
#     if isinstance(list1,list):
#         return min(list1)
#     else: print("Enter List")
#
# func5(1)
# res=func5([7, 5,0])
# print(res)

# – створити функцію, яка приймає List чисел та складає значення елементів List та повертає його.

# def func7(number_list):
#     if not isinstance(number_list, list):
#         print("Enter nomber List")
#         return
#     for i in number_list:
#             if not isinstance(i, (int, float)):
#                 print("Enter nomber List")
#                 return
#     return sum(number_list)
#
# res = func7([2,2,4])
# print(res)


# – створити функцію, яка приймає List чисел та повертає середнє арифметичне його значень.
# def func8(list_number):
#     if not isinstance(list_number, list):
#         print("Enter List number")
#         return
#     for i in list_number:
#         if not isinstance(i, (int,float)):
#             print("Enter List number")
#             return
#     return sum(list_number)/ len(list_number)
#
# res = func8([1,2,3,4,5.1])
# print(res)
#
#
# 1 Є list:
#
#   list = [22, 3,5,2,8,2,-23, 8,23,5]
#
#   – знайти  мін. число
#
#   – видалити усі дублікати
#
#   – замінити кожне 4-те значення на ‘X’

# list1 = [22, 3,5,2,8,2,-23, 8,23,5]
# minL = min(list1)
# print(minL)
#
# list2 = list(set(list1))
# print(list2)
#
#
# for i in range(3, len(list1), 4):
#     list1[i] = "X"
#
# print(list1)
#
# # for i, value in enumerate(list1):
# #     print(i)
# #     print(value)
#
# list1 = ["X" if i % 4 == 3 else val for i, val in enumerate(list1)]
# print(list1)
#
# list1 = ["X" if i % 4 == 3 else list1[i] for i in range(len(list1))]

# 2) вивести на екран пустий квадрат з “*”, сторона якого вказана як аргумент функції

# def func_SQ (x):
#     print(f"*{x*" "}* {"\n"*x}*{x*" "}*")
#
# func_SQ(4)

# 3) вивести табличку множення за допомогою циклу while
# i=1
# j=1
# while i<9:
#     print("\n")
#     while j<10:
#         print(f"{i}*{j} = {i*j}")
#         j+=1
#     else: j=1
#     i+=1
#
