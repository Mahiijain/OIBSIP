import tkinter as tk
from tkinter import *
import random
import string

root = tk.Tk()
root.title("Random Password Generator")

def create_gradient(canvas, color1, color2, height):
    for i in range(height):
        color = "#%02x%02x%02x" % (
            int(color1[1:3], 16) + int((int(color2[1:3], 16) - int(color1[1:3], 16)) * i / height),
            int(color1[3:5], 16) + int((int(color2[3:5], 16) - int(color1[3:5], 16)) * i / height),
            int(color1[5:7], 16) + int((int(color2[5:7], 16) - int(color1[5:7], 16)) * i / height)
        )
        canvas.create_line(0, i, 600, i, fill=color, width=1)

canvas1 = tk.Canvas(root, width=600, height=730, relief='raised')
canvas1.pack()

create_gradient(canvas1, '#add8e6', '#87ceeb', 730)

label1 = tk.Label(root, text="RANDOM PASSWORD GENERATOR", bg='#87ceeb')
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

    if not characters and not custom_symbols:
        text.delete(1.0, END)
        text.insert(END, "Please select at least one character type or enter custom symbols.\n")
        return

    passwords = []
    for _ in range(count):
        password_chars = [random.choice(characters) for _ in range(length - len(custom_symbols))]
        password_chars.extend(custom_symbols)  
        random.shuffle(password_chars) 
        passwords.append(''.join(password_chars))

    display_passwords(passwords)

def display_passwords(passwords):
    text.delete(1.0, END)
    for password in passwords:
        text.insert(END, password + '\n')

def copy_to_clipboard():
    root.clipboard_clear()  
    root.clipboard_append(text.get(1.0, END))  
    root.update() 
    text.insert(END, "Passwords copied to clipboard!")

label_length = tk.Label(root, text="Enter password length:", bg='#87ceeb')
label_length.config(font=('helvetica', 12))
canvas1.create_window(300, 120, window=label_length)

entry1 = tk.Entry(root)
canvas1.create_window(300, 150, window=entry1)

label_count = tk.Label(root, text="Enter number of passwords to generate:", bg='#87ceeb')
label_count.config(font=('helvetica', 12))
canvas1.create_window(300, 190, window=label_count)

entry2 = tk.Entry(root)
canvas1.create_window(300, 220, window=entry2)

var_uppercase = BooleanVar()
var_lowercase = BooleanVar()
var_digits = BooleanVar()
var_special = BooleanVar()

checkbox_uppercase = tk.Checkbutton(root, text="Include Uppercase Letters", variable=var_uppercase, bg='#87ceeb')
canvas1.create_window(300, 260, window=checkbox_uppercase)

checkbox_lowercase = tk.Checkbutton(root, text="Include Lowercase Letters", variable=var_lowercase, bg='#87ceeb')
canvas1.create_window(300, 290, window=checkbox_lowercase)

checkbox_digits = tk.Checkbutton(root, text="Include Digits", variable=var_digits, bg='#87ceeb')
canvas1.create_window(268, 320, window=checkbox_digits)

checkbox_special = tk.Checkbutton(root, text="Include Special Characters", variable=var_special, bg='#87ceeb')
canvas1.create_window(300, 350, window=checkbox_special)

label_symbols = tk.Label(root, text="Enter specific symbols to include:", bg='#87ceeb')
label_symbols.config(font=('helvetica', 12))
canvas1.create_window(300, 400, window=label_symbols)

entry_symbols = tk.Entry(root)
canvas1.create_window(300, 430, window=entry_symbols)

button1 = tk.Button(root, text="Generate Passwords", command=rpg, bg='#aaffaa', font=('helvetica', 12))
canvas1.create_window(300, 470, window=button1)

button_copy = tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard, bg='#aaffaa', font=('helvetica', 12))
canvas1.create_window(300, 520, window=button_copy)

text = tk.Text(root, height=8, width=50)
canvas1.create_window(300, 640, window=text)

root.mainloop()
