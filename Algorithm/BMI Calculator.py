import tkinter
from tkinter import ttk  
#---------------------------------------------------------------
def bmi_calc():
    weight=float(weight_box.get())
    height=float(height_box.get())/100
    bmi=weight/height**2
    if bmi<18.5:
        msg='Low'
    elif 18.5<bmi<25.0:
        msg='Normal'
    else:
        msg='obese'
    bmi_label.configure(text='BMI:' + str(round(bmi,1))+ ' '+msg)
#---------------------------------------------------------------
#Main 
root=tkinter.Tk()
root.title('BMI Calculate')
root.geometry("300x100")
weight_label=ttk.Label(root,text='Weight（Kg）')
weight_label.grid(column=0,row=0,padx=10,pady=5)
weight_box=ttk.Entry(root)
weight_box.grid(column=1,row=0,pady=5)
height_label=ttk.Label(root,text='Height(cm)')
height_label.grid(column=0,row=1,pady=5)
height_box=ttk.Entry(root)
height_box.grid(column=1,row=1,pady=5)
calc_btn=ttk.Button(root,text='CALC',command=bmi_calc)
calc_btn.grid(column=0,row=2,pady=5)
bmi_label=ttk.Label(root,text='BMI Result')
bmi_label.grid(column=1,row=2,pady=5)
root.mainloop()