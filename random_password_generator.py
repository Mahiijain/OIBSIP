# import tkinter as tk
# from tkinter import *
# import random
# import string

# root = tk.Tk()
# root.title("Random Password Generator")

# canvas1 = tk.Canvas(root, width=600, height=650, bg='orange', relief='raised')
# canvas1.pack()

# label1 = tk.Label(root, text="RANDOM PASSWORD GENERATOR", bg='lightgreen')
# label1.config(font=('helvetica', 20))
# canvas1.create_window(300, 60, window=label1)

# def rpg():
#     length = int(entry1.get())
#     count = int(entry2.get())
#     characters = ''
#     if var_uppercase.get():
#         characters += string.ascii_uppercase
#     if var_lowercase.get():
#         characters += string.ascii_lowercase
#     if var_digits.get():
#         characters += string.digits
#     if var_special.get():
#         characters += string.punctuation
    
#     if not characters:
#         text.delete(1.0, END)
#         text.insert(END, "Please select at least one character type.\n")
#         return

#     passwords = [''.join(random.choice(characters) for i in range(length)) for _ in range(count)]
#     display_passwords(passwords)

# def display_passwords(passwords):
#     text.delete(1.0, END)
#     for password in passwords:
#         text.insert(END, password + '\n')

# label_length = tk.Label(root, text="Enter password length:", bg='orange')
# label_length.config(font=('helvetica', 12))
# canvas1.create_window(300, 150, window=label_length)

# entry1 = tk.Entry(root)
# canvas1.create_window(300, 180, window=entry1)

# label_count = tk.Label(root, text="Enter number of passwords to generate:", bg='orange')
# label_count.config(font=('helvetica', 12))
# canvas1.create_window(300, 220, window=label_count)

# entry2 = tk.Entry(root)
# canvas1.create_window(300, 250, window=entry2)

# var_uppercase = BooleanVar()
# var_lowercase = BooleanVar()
# var_digits = BooleanVar()
# var_special = BooleanVar()

# checkbox_uppercase = tk.Checkbutton(root, text="Include Uppercase Letters", variable=var_uppercase, bg='orange')
# canvas1.create_window(300, 290, window=checkbox_uppercase)

# checkbox_lowercase = tk.Checkbutton(root, text="Include Lowercase Letters", variable=var_lowercase, bg='orange')
# canvas1.create_window(300, 320, window=checkbox_lowercase)

# checkbox_digits = tk.Checkbutton(root, text="Include Digits", variable=var_digits, bg='orange')
# canvas1.create_window(268, 350, window=checkbox_digits)

# checkbox_special = tk.Checkbutton(root, text="Include Special Characters", variable=var_special, bg='orange')
# canvas1.create_window(300, 380, window=checkbox_special)

# button1 = tk.Button(root, text="Generate Passwords", command=rpg, bg='lightgreen', font=('helvetica', 12))
# canvas1.create_window(300, 420, window=button1)

# text = tk.Text(root, height=10, width=50)
# canvas1.create_window(300, 550, window=text)

# root.mainloop()

import tkinter as tk
from tkinter import *
import random
import string

root = tk.Tk()
root.title("Random Password Generator")

canvas1 = tk.Canvas(root, width=600, height=700, bg='orange', relief='raised')
canvas1.pack()

label1 = tk.Label(root, text="RANDOM PASSWORD GENERATOR", bg='lightgreen')
label1.config(font=('helvetica', 20))
canvas1.create_window(300, 60, window=label1)

def rpg():
    length = int(entry1.get())
    count = int(entry2.get())
    custom_symbols = entry_symbols.get()
    characters = ''
    
    if var_uppercase.get():
        characters += string.ascii_uppercase
    if var_lowercase.get():
        characters += string.ascii_lowercase
    if var_digits.get():
        characters += string.digits
    if var_special.get():
        characters += string.punctuation
    if custom_symbols:
        characters += custom_symbols
    
    if not characters:
        text.delete(1.0, END)
        text.insert(END, "Please select at least one character type.\n")
        return

    passwords = [''.join(random.choice(characters) for i in range(length)) for _ in range(count)]
    display_passwords(passwords)

def display_passwords(passwords):
    text.delete(1.0, END)
    for password in passwords:
        text.insert(END, password + '\n')

label_length = tk.Label(root, text="Enter password length:", bg='orange')
label_length.config(font=('helvetica', 12))
canvas1.create_window(300, 150, window=label_length)

entry1 = tk.Entry(root)
canvas1.create_window(300, 180, window=entry1)

label_count = tk.Label(root, text="Enter number of passwords to generate:", bg='orange')
label_count.config(font=('helvetica', 12))
canvas1.create_window(300, 220, window=label_count)

entry2 = tk.Entry(root)
canvas1.create_window(300, 250, window=entry2)

var_uppercase = BooleanVar()
var_lowercase = BooleanVar()
var_digits = BooleanVar()
var_special = BooleanVar()

checkbox_uppercase = tk.Checkbutton(root, text="Include Uppercase Letters", variable=var_uppercase, bg='orange')
canvas1.create_window(300, 290, window=checkbox_uppercase)

checkbox_lowercase = tk.Checkbutton(root, text="Include Lowercase Letters", variable=var_lowercase, bg='orange')
canvas1.create_window(300, 320, window=checkbox_lowercase)

checkbox_digits = tk.Checkbutton(root, text="Include Digits", variable=var_digits, bg='orange')
canvas1.create_window(268, 350, window=checkbox_digits)

checkbox_special = tk.Checkbutton(root, text="Include Special Characters", variable=var_special, bg='orange')
canvas1.create_window(300, 380, window=checkbox_special)

label_symbols = tk.Label(root, text="Enter specific symbols to include:", bg='orange')
label_symbols.config(font=('helvetica', 12))
canvas1.create_window(300, 420, window=label_symbols)

entry_symbols = tk.Entry(root)
canvas1.create_window(300, 450, window=entry_symbols)

button1 = tk.Button(root, text="Generate Passwords", command=rpg, bg='lightgreen', font=('helvetica', 12))
canvas1.create_window(300, 490, window=button1)

text = tk.Text(root, height=10, width=50)
canvas1.create_window(300, 600, window=text)

root.mainloop()

