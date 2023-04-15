def generate_data(num):
    data_list = [i for i in range(1, num + 1)]
    data_tuple = tuple(data_list)
    data_dict = {i: i ** 2 for i in data_list}

    return data_list, data_tuple, data_dict


my_list, my_tuple, my_dict = generate_data(5)
print("тізім: ", my_list)
print("кортеж: ", my_tuple)
print("сөздік: ", my_dict)