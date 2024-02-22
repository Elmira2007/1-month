#1
# a= int(input("Введите номер месяца: "))
# def  season(a):
#     if a == 12 or a == 1 or a == 2:
#         print("Зима")
#     elif a == 3 or a == 4 or a == 5:
#         print("Весна")
#     elif a == 6 or a == 7 or a == 8:
#         print("Лето")
#     elif a == 9 or a == 10 or a == 11:
#         print("Осень")
#     else:
#         print("Ошибка!!!!!!!")

# season(a)


# #2
# a = int(input("Сколько рублей вы хотите вкласть? : "))
# years = int(input("На сколько лет? : "))

# def bank(a,years):
#     count = 0
#     final_num = a
#     while count < years:
#         num = a / 100 
#         num1 = num * 10
#         final_num += num1
#         count += 1


    
#3
# list1 = [1,2,3,4,5]
# list2 = [6,7,8,9,10]
# list_sum = sum(list1) + sum(list2)
# devision = list_sum / 10
# print(devision)


#4
# def zero(number):
#     for i in range(1,11):
#         print(i,"0")

# zero(0)


#5
# def lists(list1):
#     list2 = []
    # for i in list1:
    #     if "A" not in i and "a" not in i and "I" not in i and "i":
#             list2.append(i)
#     return list2
# list3 = ["apple", "banana", "ice", "brown", "cherry"]

# list4 = lists(list3)
# print(list4)


#ДОП
# def usogram(word):
#     letters = set()
#     for i in word:
#         if i in letters:
#             return False
#         letters.add(i)
#     return True
# a = "hello"
# b = "go"
# print(usogram(a))
# print(usogram(b)) 


#2
# def num(num1):
#     num2 = int(str(num1)[::-1])
#     print(num2)
# num(34567)


#3
# def chatbot():
    # while True:
    #     urers = input("задайте мне вопрос: ")
    #     print(urers)
    #     if urers.find("?") >0:
        #     print("Конечно")
        # elif urers.find("!") >0:
        #     print("Успокойся")
        # elif urers == "":
#             print("Как классно,ты молчишь.Продолжай в том же духе")
#         else:
#             print("Ну и что")
# chatbot()