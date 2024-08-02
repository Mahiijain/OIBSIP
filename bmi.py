import tkinter as tk
from tkinter import *

root = tk.Tk()
canvas1 = tk.Canvas(root, width=600, height=500, bg='teal', relief='raised')
canvas1.pack()

label1 = tk.Label(root, text="BMI CALCULATOR", bg='hotpink')
label1.config(font=('helvetica' ,20))
canvas1.create_window(300, 60, window=label1)

#input
kg = float(input('Enter your weight in kg:'))
m = float(input('Enter your height in m:'))

BMI = float(kg/m**2)

print("BMI calculated is: ",BMI)

if(BMI>0):
    if(BMI<=16):
        print("You are very underweight")
    elif(BMI<=18.5):
        print("you are underweight")
    elif(BMI<=25):
        print("healthy")
    elif(BMI<=30):
        print("you are overweight")
    else:
        print("you are very overweight")
else:
    print("Enter valid details")

root.mainloop()