#This is simple python desktop code
#to display Calendar 
#Create by Ueda
#-----------------------------
import tkinter as tk
import datetime as da
import calendar as ca
from tkinter import messagebox

WEEK =['Sun','Mon','Tue','Wed','Thu','Fri','Sat']
WEEK_COLOR=['red','black','black','black','black','black','blue']
MONS =['January','February','March','April','May','Jun',
        'July','August','September','October','November','December']
#Calendar Function
def disp(arg):
    global yer
    global mon
    
    mon[0] += arg
    
    #Modify and display when year change
    if  mon[0] <1:
        mon[0],yer[0] = 12,yer[0]-1
    elif mon[0] >12:
        mon[0],yer[0] =1,yer[0]+1
    label['text'] =MONS[mon[0]-1]+", "+str(yer[0])
    #Get Python Calendar
    cal = ca.Calendar(firstweekday=6)
    cal = cal.monthdayscalendar(yer[0],mon[0])
    
    #Delete widget from Frame
    for widget in frame.winfo_children():
        widget.destroy()
    r = 0
    for i,x in enumerate(WEEK):
        label_day = tk.Label(frame,
                            text =x,
                            font =('',10),
                            width=3,
                            fg = WEEK_COLOR[i])
        label_day.grid(row=r,column=i,pady=1)
    r=1
    for week in cal:
        for i,day in enumerate(week):
            day = ' ' if day == 0 else day
            label_day = tk.Label(frame,
                                text = day,
                                font =(' ',10),
                                fg= WEEK_COLOR[i],
                                borderwidth=1)
            if (yer[0], mon[0], today) == (yer[1],mon[1],day):
                label_day['relief'] = 'solid'
            label_day.bind('<Button-1>',click)
            label_day.grid(row =r , column=i,padx=2,pady=1)
        r = r+1

#
def click(event):
    t= event.widget['text']
    event.widget['background'] = 'gray'
    messagebox.showinfo("Info","Selected Day: "+str(t))
    
#Main Window
root = tk.Tk()
root.title("Calendar")
root.geometry("220x200")
root.resizable(0,0)

#Get current Date
yer = [da.date.today().year] *2
mon =[da.date.today().month] *2
today = da.date.today().day

#By window width ,Divide colummns by one third 
for n in range(3):
    root.grid_columnconfigure(n,weight=1)

#Display Button
label = tk.Label(root,font=('',10))
button_1 = tk.Button(root,
                    text="<",
                    font =('',10),
                    command=lambda: disp(-1))
button_1.grid(row=0,column=0,pady=10)
label.grid(row=0,column=1)
button_2 = tk.Button(root,
                    text=">",
                    font =('',10),
                    command=lambda: disp(1))
button_2.grid(row=0,column=2)

#Display date 
frame = tk.Frame(root)
frame.grid(row =1,column=0,columnspan=3)
disp(0)
root.mainloop()
