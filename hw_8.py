# 1
# with open("users.txt","w") as file_write:
#     file_write.write("Hello work")
# with open("users.txt","r") as file_read:
#     result = file_read.read()
#     print(result)


#2
# with open("users.txt","r", encoding="UTF-8") as file:
#     res = file.read().split("\n") 
#     print(len(res))


#3
# with open("text.txt","r",encoding="UTF-8") as text_list1:
#     result = text_list1.read()
#     if "Elmira" in result:
#         print("Слова найдено: ")
#     else: 
#         print("Слово не найдено!!!")


#4 
# res = input("Введите текст: ")
# with open("res.txt","a+",encoding="UTF-8") as res_list:
#     res_list.write(f"Текст добавлен: {res}.\n")
#     print(res_list)


#5
# def copy(file1,file2):
#     with open(file1,"r") as file1:
#         with open(file2,"w") as file2:
#             file2.write(file1.read())
#             print("Файл успешно скопирован!")


# copy("users.txt","res.txt")


#6
# with open("text.txt","r", encoding="UTF-8") as text_list2:
#     result = text_list2.read().split()
#     print(len(result))


#7
# user = input("Введите слово: ")
# with open("res1.txt","w", encoding="UTF-8") as res_list:
#     res_list.write(f"Новая версия: {user}.\n")