# 1) Створити файл email.txt та наповнити його інформацію наступного формату (використайте для цього ШІ).
#
# 9d3dc7094d3dcb31ffe2960ad891dd04 34hrap@gmail.com
#
# ec4f2883e9eb74770d02b30f06659a5f tele_nat@mail.i
#
# 44ab3c993daee2a9655925d53fbdd7bf telepaev.sn@gmail.com
#
# ….
#
# ваша задача:  записати в новий файл тільки email’ /-ли з доменом gmail.com
from os.path import join


# try:
#     with open("email.txt", "w") as file:
#         file.write("3a8f91c2d4e5b60718293a4b5c6d7e8f liam.turner91@gmail.com\n8c7e6d5b4a3f2e1d0c9b8a7f6e5d4c3b chloe_bennett@yahoo.com\n1f2e3d4c5b6a79887766554433221100 noah.carter84@outlook.com\n9a8b7c6d5e4f3a2b1c0d9e8f7a6b5c4d ava_mitchell@gmail.com\n4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b mason.perez77@proton.me\n7d8e9f0a1b2c3d4e5f6a7b8c9d0e1f2a isabella_roberts@icloud.com\n2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f logan.campbell@ukr.net\n6b7c8d9e0f1a2b3c4d5e6f7a8b9c0d1e mia_phillips95@gmail.com\n0a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d lucas.evans80@yahoo.co.uk\n5e6f7a8b9c0d1e2f3a4b5c6d7e8f9a0b harper_edwards@gmx.com\nb1c2d3e4f5a6b7c8d9e0f1a2b3c4d5e6 elijah.collins@zoho.com\ne4f5a6b7c8d9e0f1a2b3c4d5e6f7a8b9 amelia_stewart88@gmail.com\n9d0e1f2a3b4c5d6e7f8a9b0c1d2e3f4a james.sanchez@i.ua\n3c4d5e6f7a8b9c0d1e2f3a4b5c6d7e80 evelyn_morris@aol.com\n8a9b0c1d2e3f4a5b6c7d8e9f0a1b2c3d benjamin.rogers@meta.ua\nd5e6f7a8b9c0d1e2f3a4b5c6d7e8f9a0 abigail_reed93@gmail.com\n2f3a4b5c6d7e8f9a0b1c2d3e4f5a6b7c henry.cook75@web.de\n7a8b9c0d1e2f3a4b5c6d7e8f9a0b1c2e emily_morgan@outlook.com\n4b5c6d7e8f9a0b1c2d3e4f5a6b7c8d9e alexander.bell@icloud.com\nc0d1e2f3a4b5c6d7e8f9a0b1c2d3e4f5 ella_murphy86@proton.me\n")
#
#
# except Exception as e:
#     print(e)
#
# try:
#     with open("email.txt", "r") as file:
#        arr_email =  file.readlines()
#        email_gmail = [i for i in arr_email if "gmail.com" in i]
#        data = "\n".join(email_gmail)
#
# except Exception as e:
#     print(e)
#
# try:
#     with open("gmail.txt", "w") as file:
#         file.write(data)
# except Exception as e:
#     print(e)



# #Решение от преподавателя (у меня был неправильно формат забит)
# try:
#     with open("text_dz_4_1.txt") as file_source, open("mails_2.txt", "w") as file_result:
#         for line in file_source:
#             email = line.split()[-1]
#             if email.endswith("gmail.com"):
#                 # file_result.write(f"{email}\n")
#                 #можно записывать в файл спомощью принта - он сам добавляет перенос строки
#                 print(email, file=file_result)
#
# except Exception as e:
#     print(e)




# 2) Створити записну книжку покупок:
#
# – у покупки повинна бути id, назва і ціна
#
# – всі покупки зберігаємо в файлі

# з функціоналу:
#
#  * вивід всіх покупок
#
#  * має бути змога додавати покупку в книгу
#
# * має бути змога шукати по будь-якому полю покупку
#
# * має бути змога показати найдорожчу покупку
#
# * має бути можливість видаляти покупку по id
#
# (ну і меню на це все)



class Purchase:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price
        # self.write_notebook()

    def write_notebook (self):
        recording = f"id: {self.id}, name: {self.name}, price: {self.price}\n"
        try:
            with open("notebook.txt", "a", encoding="utf-8") as file:
                file.write(recording)
        except Exception as e:
            print(e)

    @classmethod
    def get_notebook(cls):
        try:
            with open("notebook.txt", encoding="utf-8") as file:
              content = file.read()
              print(content)
              return content
        except Exception as e:
            print(e)

    @classmethod
    def search(cls, key, value):
        found = []
        try:
            with open("notebook.txt", encoding="utf-8") as file:
                for i in file:
                    arr_str = (i.strip()).split(",")
                    for j in arr_str:
                        j = j.strip()
                        if j.startswith(key) and j.split(":")[-1].strip() == str(value):
                            print(i.strip())
                            found.append(i.strip())

        except Exception as e:
            print(e)
        return ("\n").join(found)




pur1 = Purchase(1, "box", 500)
pur2 = Purchase(2, "pen", 70)
pur3 = Purchase(3, "bread", 47)
pur4 = Purchase(4, "bread", 80)
pur5 = Purchase(5, "chees", 70)
pur7 = Purchase(7, "pensil", 500)
pur1.write_notebook()
pur2.write_notebook()
pur3.write_notebook()
pur4.write_notebook()
pur5.write_notebook()
pur7.write_notebook()
# Purchase.search("name", "bread")
# Purchase.search("id", 7)
Purchase.search("price", 500)


