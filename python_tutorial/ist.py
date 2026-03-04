import tkinter as stk

root = stk.Tk()
root.title("motka")
root.geometry("1200x1200")

label = stk.Label(root, text="Welcome to Python")
label.pack(pady=10+80)

def say_hello():
    label.config(text="gaand mra motka")

button = stk.Button(root, text="Click me", command=say_hello)
button.pack()

root.mainloop()
