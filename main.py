import tkinter as tk
from pages.example import mi_funcion

root = tk.Tk()

text = "\n".join(str(i) for i in range(1, 11))
text2 = "\n"+str(mi_funcion())+" Funcion"
label = tk.Label(root, text=text+text2, font=("Helvetica", 16))

label.pack()
root.mainloop()