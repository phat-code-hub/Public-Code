#This a simple program for study desktop App 
#create by Ueda
#-------------------------
import tkinter as tk
#BMI calculate Function
def calc(weight,height):
    return weight/(height**2)

#Fatness judge function
def check(bmi):
    color_index=0
    if bmi < 18.5:
        result ="UnderWeight"
    elif bmi <25.0:
        result ="NormalWeight"
    elif bmi<30.0:
        result="OverWeight"
        color_index=1
    elif bmi<35.0:
        result ="Obesity I"
        color_index=2
    elif bmi<40.0:
        result="Obesity II"
        color_index=3
    else:
        result ="Obesity III"
        color_index=4
    return result,color_index

#Window Initialize
root = tk.Tk()
root.title("Check Your BMI")
root.geometry("250x150")

#Create Label controls
label_1 = tk.Label(root,text="Weight")
label_2 = tk.Label(root,text="(Kg)")
label_3 = tk.Label(root,text="Height")
label_4 = tk.Label(root,text="(cm)")
label_5 = tk.Label(root,text="Input your weight and height please")

#Create Entry widget 
weight = tk.Entry(width=5)
height = tk.Entry(width=5)

#Button Event Handle
def judgment():
    w = float(weight.get())
    h = float(height.get()) /100
    s ,i= check(calc(w,h))
    label_5['text'] = "Your BMI: "+ str(s)
    if i == 1: #Overweight
        _color="blue"
    elif i== 2:
        _color="pink"
    elif i==3:
        _color="beige"
    elif i==4:
        _color="red"
    else:
        _color="black"
    label_5['fg'] =_color

#Create Button
button = tk.Button(root,text="BMI Calculate", command=judgment)

#Position controls
root.columnconfigure(0,weight=1)
root.columnconfigure(1,weight=1)
root.columnconfigure(2,weight=1)

root.rowconfigure(0,weight=1)
root.rowconfigure(1,weight=1)
root.rowconfigure(2,weight=1)
root.rowconfigure(3,weight=1)

#Fisrt Row
label_1.grid(column=0,row=0,sticky=tk.E)
weight.grid(column=1,row=0)
label_2.grid(column=2,row=0,sticky=tk.W)

#Second Row
label_3.grid(column=0,row=1,sticky=tk.E)
height.grid(column=1,row=1)
label_4.grid(column=2,row=1,sticky=tk.W)

#Third Row
button.grid (column=0,row=2,columnspan=3)

#Last Row
label_5.grid(column=0,row=3,columnspan=3)

root.mainloop()