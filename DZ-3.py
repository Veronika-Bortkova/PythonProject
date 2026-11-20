# Створити клас Rectangle:
#
# -він має приймати дві сторони x,y
#
# Описати поведінку арифметичним методом:
#
#   + сума площин двох екземплярів класу
#
#   – різниця площин двох екземплярів класу
#
#   == площин на рівність
#
#   != площин на нерівність
#
#   >, < менше більше
#
#   при виклику метода len() підраховувати суму сторін
import numbers




# from typing import Self
# class Rectangle:
#     def __init__(self, x,y):
#         self.x = x
#         self.y = y
#
#     def __add__(self, other:Self):
#         return self.x * self.y + other.x * other.y
#
#     def __sub__(self, other:Self):
#         return self.x * self.y - other.x * other.y
#
#     def __eq__(self, other:object) -> bool:
#         return self.x * self.y == other.x * other.y
#
#     def __ne__(self, other:object) -> bool:
#         return self.x * self.y != other.x * other.y
#
#     def __lt__ (self, other:Self):
#         return  self.x * self.y < other.x * other.y
#
#     def __gt__ (self, other:Self):
#         return  self.x * self.y > other.x * other.y
#
#     def __len__(self):
#         return (self.x + self.y)*2
#
#
# rectangle1 = Rectangle(10,2)
# rectangle2 = Rectangle(3,40)
# print(rectangle1 + rectangle2)#140
# print(rectangle1 - rectangle2)#-100
# print(rectangle2 == rectangle1)#False
# print(rectangle1 != rectangle2)#True
# print(rectangle1 < rectangle2)#True
# print(rectangle1 > rectangle2)#False
# print(len(rectangle1))#24


###########################################################################################################################
# створити клас Human(name, age)
#
# створити два класи Prince и Cinderella, які наслідуються від Human:
#
# у попелюшки має бути ім’я, вік, розмір ноги

# у принца має бути ім’я, вік, та розмір знайденого черевичка, а також метод, котрий буде приймати список попелюшок, та шукати ту саму
#
# в класі попелюшки має бути count, який буде зберігати кількість створених екземплярів класу
# також має бути метод класу, який буде виводити це значення

# class Human:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __str__ (self):
#         return f"{self.name} {self.age} лет"
#
# class Cinderella(Human):
#     __count_cind = 0
#     def __init__(self, name, age, size_foot):
#         super().__init__(name, age)
#         self.sizeFoot = size_foot
#         Cinderella.__count_cind +=1
#
#     @classmethod
#     def get_count_cind (cls):
#         return cls.__count_cind
#
# class Prince(Human):
#     def __init__(self, name, age, size_boot):
#         super().__init__(name, age)
#         self.sizeBoot = size_boot
#
#
#     def found (self, arr_cinderels: list[Cinderella]):
#         for item in arr_cinderels:
#             if item.sizeFoot == self.sizeBoot:
#                 return item
#         return "Нет золушки с таким ращмером ноги"
#
#
# cind1 = Cinderella("Nic", 17, 36)
# cind2 = Cinderella("Vik", 18, 37)
# cind3 = Cinderella("Moon", 20, 38)
#
# arr_cind = [cind1, cind2, cind3]
#
# print(Cinderella.get_count_cind())
#
# prince = Prince("Jey", 22, 37)
# cind_found = prince.found(arr_cind)
# print(cind_found)

#########################################################################################################################
# 1) Створити абстрактний клас Printable, який буде описувати абстрактний метод print()
# 2) Створити класи Book та Magazine, в кожного в конструкторі змінна name, та який наслідується від класу Printable
# 3) Створити клас Main, в якому буде:
# – змінна класу printable_list, яка буде зберігати книжки та журнали
#
# – метод add, за допомогою якого можна додавати екземпляри класів в список і робити перевірку, чи то, що передають, є класом Book або Magazine інакше ігнорувати додавання
#
# – метод show_all_magazines, який буде виводити всі журнали, викликаючи метод print абстрактного класу
#
# – метод show_all_books, який буде виводити всі книги, викликаючи метод print абстрактного класу

from abc import ABC, abstractmethod
from string import printable


class Printable(ABC):
    @abstractmethod
    def print(self):
        pass

class Book(Printable):

    def __init__(self, name):
        self.name = name

    def print(self):
        print(f"{self.name }")


class Magazine(Printable):
    def __init__(self, name):
        self.name = name

    def print(self):
        print(f"{self.name}")


class Main:
    printable_list:list[Printable] = []

    @classmethod
    def add (cls, item):
        if isinstance(item, Magazine|Book):
            Main.printable_list.append(item)

    @classmethod
    def show_all_magazines (cls):
        for item in cls.printable_list:
            if isinstance(item, Magazine):
                item.print()

    @classmethod
    def show_all_books (cls):
        for item in cls.printable_list:
            if isinstance(item, Book):
                item.print()


mag1= Magazine("mag1")
mag2 = Magazine("mag2")
mag3 = Magazine("mag3")
book1 = Book("book1")
book2 = Book("book2")
book3 = Book("book3")

libr = [mag1, mag2, book1, mag3, book2, book3]

for item in libr:
    Main.add(item)

Main.show_all_books()
Main.show_all_magazines()

