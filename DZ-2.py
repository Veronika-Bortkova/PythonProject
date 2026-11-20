

# 1) написати функцію (notebook) на замикання, котра буде в собі зберігати список справ, вам потрібно реалізувати два методи:
#
# – перший записує в список нову справу
#
# – другий повертає всі записи
#
# (приклад сигнатури функції notebook у вкладенні )
#
# from typing import  Callable
# def notebook ()->tuple[Callable[[str], list[str]], Callable[[],list[str]]]:
#     todo_list:list[str] = []
#     def add_todo (to_do:str)->list[str]:
#         nonlocal todo_list
#         if to_do not in todo_list:
#             todo_list.append(to_do)
#         return todo_list.copy()
#     def get_all ()->list[str]:
#         nonlocal todo_list
#         return todo_list.copy()
#
#     return add_todo, get_all
#
# add_todo, get_list_todo = notebook()
# add_todo("do1")
# add_todo("Do2")
# add_todo("do1")
# full_list = get_list_todo()
# get_list_todo()
# print(full_list)


# l1 = notebook()
# concurrent_l = l1("do1")
# print(concurrent_l)
# l1("do2")
# print(concurrent_l)
# l1("do3")
# l1("do1")
# print(concurrent_l)
# l1("do4")
# print(concurrent_l)



################################################################################################
#3) створити функцію, котра буде повертати суму розрядів числа у вигляді строки (також використовуємо типізацію)
#
# def sum_str (x:int)->str:
#     str_N:str = str(x)
#     leng:int = len(str_N)
#     l_str = []
#     for i in str_N:
#         leng -= 1
#         if i != "0":
#             l_str.append(i+"0"*leng)
#         else: continue
#
#     return " + ".join(l_str)
#
#
# print(sum_str(70022))
# print(sum_str(754))


############################################################################################################
# 4) створити декоратор, котрий буде підраховувати, скільки разів була запущена функція, продекорована цим декоратором, та буде виводити це значення після виконання функцій
#
# приклад декоратору у вкладенні

from typing import  Callable
def decor(func):
    count = 0
    def inner(*args, **kwargs):
        nonlocal count
        print("--------------------------------")
        func(*args,**kwargs)
        count +=1
        print(f"count = {count}")
    return inner#возвращаем внутреннюю функцию - ен запуск, а именно функцию

@decor
def func1 ()->None:
    print("func1")

@decor
def func2 ():
    print("func2")


func1()
func2()
func1()
func2()
func1()
func2()
func1()
func2()







