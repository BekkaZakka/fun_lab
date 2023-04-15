from functools import reduce
my_list=[1,2,3,4,5,6,7,8,9,10]
# Мысал map: әр элементті 2-ге көбейту
result_map = list(map(lambda x: x * 2, my_list))
print(result_map)

# filter мысалы: тек жұп сандарды сақтау
result_filter = list(filter(lambda x: x % 2 == 0, my_list))
print(result_filter)

# reduce мысал: барлық элементтерді қорытындылау
result_reduce = reduce(lambda x, y: x + y, my_list)
print(result_reduce)