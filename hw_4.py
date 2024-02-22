# #1
# it_company = ('Google', 'Amazon', 'Microsoft')
# list = list(it_company)
# list.append('Tesla')
# print(list)

# 2
# it_company_index = it_company.index('Amazon')
# print(it_company_index)

# 3
# it_company1 = tuple('Apple' if x == 'Google' else x for x in it_company)

# print(it_company1)

#4
# it_company1 = it_company.index('Apple')
# it_company2 = it_company.index('Microsoft') + 1
# it_company3 = tuple(it_company[it_company1:it_company2])

# print(it_company3)

#5
# text_tuple = ('Experienced', 'programmers', 'in', 'any', 'other', 'language', 'can', 'pick', 'up', 'Python', 'very', 'quickly,', 'and', 'beginners', 'find', 'the', 'clean', 'syntax', 'and', 'indentation', 'structure', 'easy', 'to', 'learn.', 'Whet', 'your', 'appetite', 'with', 'our', 'Python', '3', 'overview')
# print(text_tuple.count('Python'))

#6
# tuple = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)
# tuple1 = tuple[:3] + tuple[10:]

# new_element = (21, 22, 23, 24, 25)
# tuple1 += new_element

# print(tuple1)

# print("Кортеж с циклом:")
# for i in tuple1:
#     print(i)


#7
# list = []

# for i in range(1, 101):
#     list.append(i)

# print(list)

#8
# list = list(range(1, 1001))

# min = min(list)
# max = max(list)

# print("Минимальное значение:", min)
# print("Максимальное значение:", max)
# sum = sum(list)
# print(sum)

#9
# for i in range(1, 498):
#     if i % 2 == 0:
#         print(i)

#10
# while True:
#         num1 = float(input("Введите первое число: "))
#         num2 = float(input("Введите второе число: "))
#         a = input("Выберите операцию (+, -, *, /) или введите 'e' для выхода: ")

#         if a == 'e':
#             break
#         elif a not in ('+', '-', '*', '/'):
#             print("Неверно")
#         else:
#             if a == '+':
#                 result = num1 + num2
#             elif a == '-':
#                 result = num1 - num2
#             elif a == '*':
#                 result = num1 * num2
#             elif a == '/':
#                 if num2 == 0:
#                     print("На ноль делить нельзя")
#                     continue
#                 result = num1 / num2
# #             else:
# #                 print("Неверно")

# #             print("Результат:", result)

# #dop 1
# import random 

# popytki = 5
# while popytki > 0:
#     user_choice = input("Выберите: Камень, Ножницы, Бумага: ").lower()
#     computer_choice = random.choice(["камень", "ножницы", "бумага"])

#     if user_choice in ["камень", "ножницы", "бумага"]:
#         print(f"Вы выбрали: {user_choice}")
#         print(f"Компьютер выбрал: {computer_choice}")

#         if user_choice == computer_choice:
#             print("Ничья!")
#         elif (user_choice == "камень" and computer_choice == "ножницы") or \
#              (user_choice == "ножницы" and computer_choice == "бумага") or \
#              (user_choice == "бумага" and computer_choice == "камень"):
#             print("Вы выиграли!")
#         else:
#             print("Компьютер выиграл!")

#         popytki -= 1
#         print(f"У вас осталось {popytki} попыток.\n")
#     else:
#         print("Пожалуйста, выберите из предложенных вариантов: Камень, Ножницы, Бумага.\n")


#dop2
# while True:
#     age = int(input("Введите ваш возсраст: "))
#     if age > 18:
#         print("Доступ разрешен")
#         break
#     else:
#         print("Извините, пользование данным ресурсом только с 18 лет")