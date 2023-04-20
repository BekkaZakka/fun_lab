import pandas as pd
import random

# Создаем случайную таблицу с помощью pandas
data = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'Dave', 'Eve'],
    'Age': [random.randint(18, 30) for _ in range(5)],
    'Score': [random.uniform(0, 100) for _ in range(5)]
})

# Выводим исходную таблицу
print('Исходная таблица:\n', data)

# Изменяем возраст некоторых студентов
data.loc[data['Name'] == 'Alice', 'Age'] = random.randint(30, 50)
data.loc[data['Name'] == 'Charlie', 'Age'] = random.randint(30, 50)

# Выводим измененную таблицу
print('\nИзмененная таблица:\n', data)

# Считаем средний балл студентов младше 30 лет
mean_score = data.loc[data['Age'] < 30, 'Score'].mean()
print('\nСредний балл студентов младше 30 лет:', mean_score)

# Выбираем случайного студента и выводим его данные
random_student = data.sample()
print('\nСлучайный студент:\n', random_student.to_string(index=False))
