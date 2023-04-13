# def calculate_years_of_experience(resume):
  
#     total_experience = 0
#     for experience in resume['work_history']:
#         start_date = experience['start_date']
#         end_date = experience['end_date']
#         start_year, start_month, start_day = map(int, start_date.split('-'))
#         end_year, end_month, end_day = map(int, end_date.split('-'))
#         total_experience += (end_year - start_year) + (end_month - start_month) / 12 + (end_day - start_day) / 365
#     return round(total_experience, 2)


# my_resume = {
#     'name': 'Bekzat Zakarin',
#     'email': 'bekzat@gmail.com',
#     'education': 'Computer Science',
#     'skills': ['Python', 'Java', 'C++', 'SQL', 'HTML/CSS'],
#     'work_history': [
#         {'position': 'Student', 'company': 'Satbayev', 'start_date': '2020-09-01', 'end_date': '2024-05-31'},
#         {'position': 'IT person', 'company': 'Qazaqmys Inc', 'start_date': '2025-07-21', 'end_date': '2026-07-31'},
#         {'position': 'Teacher', 'company': 'Kulsary', 'start_date': '2026-09-01', 'end_date': '2030-01-01'}
#     ]
# }

# years_of_experience = calculate_years_of_experience(my_resume)
# print("Опыт работы: " + str(years_of_experience))




# def print_resume(resume):
#     """
#     This function prints out the resume information in a readable format.
#     """
#     print("Name: " + resume['name'])
#     print("Email: " + resume['email'])
#     print("Education: " + resume['education'])
#     print("Skills: " + ", ".join(resume['skills']))
#     print("Work History: ")
#     for experience in resume['work_history']:
#         print("- " + experience['position'] + " at " + experience['company'])

# my_resume = {
#     'name': 'Bekzat Zakarin',
#     'email': 'bekzat@gmail.com',
#     'education': 'Computer Science',
#     'skills': ['Python', 'Java', 'C++', 'SQL', 'HTML/CSS'],
#     'work_history': [
#         {'position': 'Student', 'company': 'Satbayev', 'year': '2020-2024'},
#         {'position': 'It person', 'company': 'Qazaqmys Inc', 'year': '2025'},
#         {'position': 'Teacher', 'company': 'Kulsary', 'year': '2026-r.n'}
#     ]
# }

# print_resume(my_resume)


# 2

# def generate_data(num):

#     data_list = [i for i in range(1, num+1)]
#     data_tuple = tuple(data_list)
#     data_dict = {i: i**2 for i in data_list}
    
#     return data_list, data_tuple, data_dict

# my_list, my_tuple, my_dict = generate_data(10)
# print("List: ", my_list)
# print("Tuple: ", my_tuple)
# print("Dictionary: ", my_dict)


# 3

# from functools import reduce

# # Map example: multiplying each element by 2
# result_map = list(map(lambda x: x * 2, my_list))
# print(result_map)   

# # Filter example: keeping only even numbers
# result_filter = list(filter(lambda x: x % 2 == 0, my_list))
# print(result_filter)   

# # Reduce example: summing up all the elements
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
#     return x ** 2

# def g(x):
#     return x + 1

# h = func(f, g)

# result = h(2)
# print(result)   # f(g(2)) = f(3) = 3**2 = 9 