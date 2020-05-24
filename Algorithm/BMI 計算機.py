
import tkinter
from tkinter import ttk
def bmi_calc():
    weight=float(weight_box.get())
    height=float(height_box.get())/100
    bmi=weight/height**2
    if bmi<18.5:
        msg='低体重'
    elif 18.5<bmi<25.0:
        msg='普通体重'
    else:
        msg='肥満'
    bmi_label.configure(text='BMI:' + str(round(bmi,1))+ ' '+msg)
root=tkinter.Tk()
root.title('BMI計算機')
root.geometry("300x100")
weight_label=ttk.Label(root,text='体重（Kg）')
weight_label.grid(column=0,row=0,padx=10,pady=5)
weight_box=ttk.Entry(root)
weight_box.grid(column=1,row=0,pady=5)
height_label=ttk.Label(root,text='身長(cm)')
height_label.grid(column=0,row=1,pady=5)
height_box=ttk.Entry(root)
height_box.grid(column=1,row=1,pady=5)
calc_btn=ttk.Button(root,text='計算',command=bmi_calc)
calc_btn.grid(column=0,row=2,pady=5)
bmi_label=ttk.Label(root,text='BMI結果')
bmi_label.grid(column=1,row=2,pady=5)
root.mainloop()