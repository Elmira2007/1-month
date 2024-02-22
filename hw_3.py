#1
# age = int(input("Введите ваш возраст: "))
# if age < 18:
#     print("Вы являетесь несовершеннолетним.")
# elif 18 < age < 65:
#     print("Вы являетесь взрослым.")
# else:
#     print("Вы являетесь пожилым.") 

#2
# num1 = int(input("Введите первое число: "))
# num2 = int(input("Введите второе число: "))
# num3 = int(input("Введите третье число: "))

# print(min(num1, num2, num3))


#3
# list = ["Osh", "Talas", "Naryn", "Bishkek", "Batken", "Person", "Seven", "3D", "BMW", "Mersedes", "qwerty", "asdfg", "xcvbn", "nbvc", "lkjhg"]
# print(list[2:7])


#4
# list = ["Osh", "Talas", "Naryn", "Bishkek", "Batken", "Person", "Seven", "3D", "BMW", "Mersedes"]
# list.pop(2)
# list.pop(8)
# list.append("qweimxs")
# list.append("lunalina")
# list.append("banana")
# list.append("lemon")
# list.append("apple")

# print(list)


#5
# numbers = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# numbers.remove(2)
# numbers.remove(16)
# print(numbers)


#6
# numbers = [2,3,1,52,56,8,3,58,0,98,75,3,45,21,44,2,1,4,5,6,8,909,4,24,653,12,43,2,5,8,5,3,6,8,0,2,12,4,32,5,7,43,8,0,8,654,235,65,2,3,6,0,9,8,6,43,2,4,56,2,36,7,954,2,34,6,8,45,2,4,5,73,1,32,5,321,452,3,]
# numbers.sort()
# number = numbers[::-1]
# print(number) 


#8
# numbers = [2,3,1,52,56,8,3,58,0,98,75,3,45,21,44,2,1,4,5,6,8,909,4,24,653,12,43,2,5,8,5,3,6,8,0,2,12,4,32,5,7,43,8,0,8,654,235,65,2,3,6,0,9,8,6,43,2,4,56,2,36,7,954,2,34,6,8,45,2,4,5,73,1,32,5,321,452,3,]
# print(numbers.count(5))
# print(numbers.count(2))
# print(numbers.count(3))


#9
# numbers = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# number = sum(numbers) / len(numbers)

# print("Среднее арифметическое:", number)

#доп
# numbers = [1,2,3,4,5,6,7,8,9,10]
# print(min(numbers))
# print(max(numbers))
# print(sum(numbers))


# list = ["Osh", "Talas", "Naryn", "Bishkek", "Batken", "Person", "Seven", "3D", "BMW", "Mersedes"]
# list[2], list[8] = list[8], list[2]
# print(list)


# list = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# list = [x for x in list if x % 2 != 0]
# print(list)