from functools import reduce
my_list=[1,2,3,4,5,6,7,8,9,10]
# map
result_map = list(map(lambda x: x * 2, my_list))
print(result_map)

# filter
result_filter = list(filter(lambda x: x % 2 == 0, my_list))
print(result_filter)

# reduce
result_reduce = reduce(lambda x, y: x + y, my_list)
print(result_reduce)