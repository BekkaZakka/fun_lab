from tkinter import *

root = Tk()
canvas = Canvas(root, width=300, height=300)
canvas.create_text(150, 150, text="Abylai", font=("Arial", 30))
canvas.pack()
root.mainloop()
