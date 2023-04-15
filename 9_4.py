def dostavka(street, price):
    if street == "Аль-Фараби -Саина-Ташентского-Достык":
        if price < 10000:
            return 500
        else:
            return 0
    else:
        if price < 10000:
            return 1000
        else:
            return 1000

# вызов функции и вывод результата
total = dostavka("Аль-Фараби -Саина-Ташентского-Достык", 11500)
print("Общ стоимость доставки: ", total)