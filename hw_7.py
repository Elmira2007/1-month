1
# list1 = [1,2,3,4,5,6,7,8,9,10]
# print(list1*2)


#2
# name = ["Elmira","Mergul","Nurai","Bersultan"]
# result = list(map(lambda x:x.upper(),name))
# print(result)


#3
# name = ["Elmira","Mergul","Nurai","Bersultan"]
# print(list(map(lambda i:i[0],name)))


#4
# name = ["Elmira","Mergul","Nurai","Bersultan"]
# print(list(map(lambda num: f"{num} - {len(num)} букв",name)))


#5
# list1 = [1,2,3,4,5,6,7,8,9,10]
# str_list = str(list1)
# print(type(str_list))


#6
# num_list = [1.2,33.2,11.3,44.5,22.6,56.4]
# print(list(map(lambda x: int(x),num_list)))


#7
# num_list = [12,34,56,87,54,21,23,11,33,66,99]
# for i in num_list:
#     if i % 2 ==0 :
#             print(f" четные {i}")
#     elif i % 2 !=0:
#             print(f" нечетные {i}")


#8
# list1 = ["banana","apple","cherry","peach"]
# str_words = str(list1)
# a = list(str_words)
# print(a)


#9
# num_list = [12,34,56,87,54,21,23,11,33,66,99]
# num = list(map(lambda x:x **2,num_list))
# print(num)


#10
# list1 = ["banana","apple","cherry","peach"]
# num = list(map(lambda x:x.upper(), list1))
# for i in num:
#     print(f"{i}!")