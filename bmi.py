import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import Image

root = tk.Tk()
canvas1 = tk.Canvas(root, width=600, height=600, bg='teal', relief='raised')
canvas1.pack()

label1 = tk.Label(root, text="BMI CALCULATOR", bg='pink')
label1.config(font=('helvetica' ,20))
canvas1.create_window(300, 60, window=label1)

def BMI():
    m = float(Height.get())
    kg = float(weight.get())

    bmi = round(float(kg/m**2),3)
    #print("BMI value is:")
    #print(bmi)
    label1.config(text = bmi)
    
   
    if(bmi<=16):
        label2.config(text="You are very underweight")
    elif(bmi<=18.5):
        label2.config(text = "you are underweight")
    elif(bmi<=25):
        label2.config(text = "healthy")
    elif(bmi<=30):
        label2.config(text = "you are overweight")
    else:
        label2.config(text = "you are very overweight")


    


current_value = tk.DoubleVar()
def get_current_value():
    return '{: .2f}'.format(current_value.get())
def slider_changed(event):
    Height.set(get_current_value())

style = ttk.Style()
style.configure("TScale",bg = "teal")
slider = ttk.Scale(root,from_=0,to=220,orient="horizontal",style="TScale",command=slider_changed,variable=current_value)
slider.place(x=80,y=180)



current_value2 = tk.DoubleVar()
def get_current_value2():
    return '{: .2f}'.format(current_value2.get())
def slider_changed2(event):
    Weight.set(get_current_value2())

style2 = ttk.Style()
style2.configure("TScale",bg="teal")
slider2 = ttk.Scale(root,from_=0,to=220,orient="horizontal",style="TScale",command=slider_changed2,variable=current_value2)
slider2.place(x=400,y=180)

#####

Height = StringVar()
Weight = StringVar()

height = Entry(root,textvariable = Height,width = 5, font = 'arial 50',bg= "#fff", fg = "#000",bd=0,justify=CENTER)
height.place(x=35,y=100)
Height.set(get_current_value())

weight = Entry(root,textvariable = Weight,width = 5, font = 'arial 50',bg= "#fff", fg = "#000",bd=0,justify=CENTER)
weight.place(x=340,y=100)
Weight.set(get_current_value2())

##
label11 = tk.Label(root, text="HEIGHT IN METERS", bg='teal')
label11.config(font=('helvetica' ,20))
canvas1.create_window(150, 230, window=label11)

label21 = tk.Label(root, text="WEIGHT IN KG", bg='teal')
label21.config(font=('helvetica' ,20))
canvas1.create_window(450, 230, window=label21)

Button(root,text = 'Result',width=15,height=3,font = 'arial 10 bold', bg ="lightblue",fg='white',command= BMI).place(x=230,y=300)
label1=Label(root, font = "arial 50 bold", bg = 'teal',fg = 'white')
label1.place(x=225,y=370)
label2=Label(root, font = "arial 20 bold", bg = 'teal',fg = 'white')
label2.place(x=130,y=470)


root.mainloop()