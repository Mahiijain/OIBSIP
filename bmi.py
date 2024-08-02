import tkinter as tk
from tkinter import *

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