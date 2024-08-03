import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import Image

root = tk.Tk()
canvas1 = tk.Canvas(root, width=600, height=500, bg='teal', relief='raised')
canvas1.pack()

label1 = tk.Label(root, text="BMI CALCULATOR", bg='pink')
label1.config(font=('helvetica' ,20))
canvas1.create_window(300, 60, window=label1)

def BMI():
    m = float(Height.get())
    kg = float(weight.get())

    bmi = float(kg/m**2)
    print(bmi)
    label1.config(text = bmi)
    
   
    if(bmi<=16):
        print("You are very underweight")
    elif(bmi<=18.5):
        print("you are underweight")
    elif(bmi<=25):
        print("healthy")
    elif(bmi<=30):
        print("you are overweight")
    else:
        print("you are very overweight")


    


current_value = tk.DoubleVar()
def get_current_value():
    return '{: .2f}'.format(current_value.get())
def slider_changed(event):
    Height.set(get_current_value())

style = ttk.Style()
style.configure("TScale",bg="teal")
slider = ttk.Scale(root,from_=0,to=220,orient="horizontal",style="TScale",command=slider_changed,variable=current_value)
slider.place(x=80,y=250)



current_value2 = tk.DoubleVar()
def get_current_value2():
    return '{: .2f}'.format(current_value2.get())
def slider_changed2(event):
    Weight.set(get_current_value2())

style2 = ttk.Style()
style2.configure("TScale",bg="teal")
slider2 = ttk.Scale(root,from_=0,to=220,orient="horizontal",style="TScale",command=slider_changed2,variable=current_value2)
slider2.place(x=350,y=250)

#####

Height = StringVar()
Weight = StringVar()

height = Entry(root,textvariable = Height,width = 5, font = 'arial 50',bg= "#fff", fg = "#000",bd=0,justify=CENTER)
height.place(x=35,y=160)
Height.set(get_current_value())

weight = Entry(root,textvariable = Weight,width = 5, font = 'arial 50',bg= "#fff", fg = "#000",bd=0,justify=CENTER)
weight.place(x=325,y=160)
Weight.set(get_current_value2())

Button(root,text = 'Result',width=15,height=3,font = 'arial 10 bold', bg ="lightblue",fg='white',command= BMI).place(x=250,y=400)
label1=Label(root, font = "arial 50 bold", bg = 'lightblue',fg = 'white')
label1.place(x=125,y=305)
label2=Label(root, font = "arial 20 bold", bg = 'lightblue',fg = 'white')
label2.place(x=250,y=400)


root.mainloop()