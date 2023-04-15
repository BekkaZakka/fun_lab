input_string = input("Введите строку: ")

# Преобразуем строку во множество (set), чтобы оставить только уникальные символы
unique_chars = set(input_string)

# Преобразуем множество обратно в список, чтобы отсортировать символы в алфавитном порядке
sorted_unique_chars = sorted(list(unique_chars))

# Выводим на экран уникальные символы в алфавитном порядке
print("Уникальные символы в алфавитном порядке: ", end="")
for char in sorted_unique_chars:
    print(char, end=" ")
print()
