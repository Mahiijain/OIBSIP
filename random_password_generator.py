import tkinter as tk
from tkinter import *
from PIL import Image
import random
import string

# background
root = tk.Tk()
canvas1 = tk.Canvas(root, width=600, height=600, bg='orange', relief='raised')
canvas1.pack()

# background label
label1 = tk.Label(root, text="RANDOM PASSWORD GENERATOR", bg='lightgreen')
label1.config(font=('helvetica' ,20))
canvas1.create_window(300, 60, window=label1)

def rpg(length, count):
    passwords = []
    for i in range(count):
        password = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for i in range(length))
        passwords.append(password)
    return passwords

length = int(input("Enter the password length: "))
count = int(input("Enter the number of passwords to generate: "))

generated_passwords = rpg(length, count)

print("\nGenerated Passwords:")
for password in generated_passwords:
    print(password)
    
root.mainloop()