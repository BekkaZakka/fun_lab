# def square(number):
#     return number ** 2
# result = square(5)
# print(result) # Вывод: 25

# my_list = [3, 2, 1]
# my_list.sort()
# print(my_list)


# 2

# def generate_data(num):

#     data_list = [i for i in range(1, num+1)]
#     data_tuple = tuple(data_list)
#     data_dict = {i: i**2 for i in data_list}
    
#     return data_list, data_tuple, data_dict

# my_list, my_tuple, my_dict = generate_data(10)
# print("тізім: ", my_list)
# print("кортеж: ", my_tuple)
# print("сөздік: ", my_dict)


# 3

# from functools import reduce
# my_list=[1,2,3,4,5,6,7,8,9,10]
# # Мысал map: әр элементті 2-ге көбейту
# result_map = list(map(lambda x: x * 2, my_list))
# print(result_map)   

# # filter мысалы: тек жұп сандарды сақтау
# result_filter = list(filter(lambda x: x % 2 == 0, my_list))
# print(result_filter)   

# # reduce мысал: барлық элементтерді қорытындылау
# result_reduce = reduce(lambda x, y: x + y, my_list)
# print(result_reduce)   


# 4

# def dostavka(street, price):
#     if street == "Аль-Фараби -Саина-Ташентского-Достык":
#         if price < 10000:
#             return 500
#         else:
#             return 0
#     else:
#         if price < 10000:
#             return 1000
#         else:
#             return 1000

# # вызов функции и вывод результата
# total = dostavka("Аль-Фараби -Саина-Ташентского-Достык", 11500)
# print("Общ стоимость доставки: ", total)


# 5

# def func(f, g):
#     def h(x):
#         return f(g(x))
#     return h

# def f(x):
#     return x ** 3

# def g(x):
#     return x - 1

# h = func(f, g)

# result = h(4)
# print(result)   