# import canvas as canvas
import tkinter as tk

# Создаем окно
window = tk.Tk()

# Устанавливаем заголовок окна
window.title("Логотип")

# Создаем холст
canvas = tk.Canvas(window, width=300, height=300)

# Изменяем цвет заднего фона
canvas.configure(bg="white")

# canvas.create_line(0, 0, 300, 300, width=3, fill="purple")
canvas.create_rectangle(50, 50, 250, 250, fill="white", outline="black", width=2)
canvas.create_oval(100, 100, 200, 200, fill="red")
# Создаем текстовый объект с именем
text = canvas.create_text(150, 150, text="Abylaikhan Kosherbaev",
                          font=("Arial", 20), fill="white")
canvas.create_text(152, 152, text="Abylaikhan Kosherbaev",
                   font=("Arial", 20), fill="black")
# Отображаем холст
canvas.pack()

# Запускаем цикл событий
window.mainloop()