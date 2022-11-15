import os
from tkinter import *
from datetime import datetime as dt

window_object= Tk()

main_entry_value= StringVar()
main_entry= Entry(window_object,textvariable=main_entry_value)
main_entry.grid(row=1,columns= 1)

main_entry_btn= Button(window_object,text= 'Search Tasks',background= '#fcca33')
main_entry_btn.grid(row=1,column=2)

date_label= Label(window_object,text='Date Added',background='#33ccac')
date_label.grid(row=1,column= 4)

date_label_entry_value= StringVar()
date_label_entry= Entry(window_object,textvariable=date_label_entry_value)
date_label_entry.grid(row=1,column=3)

type_of_task_label= Label(window_object,text='Type of Task',background='#33ccaf')
type_of_task_label.grid(row=1,column=6)

type_of_task_label_entry_value= StringVar()
type_of_task_label_entry= Entry(window_object,textvariable= type_of_task_label_entry_value)
type_of_task_label_entry.grid(row= 1,column=5)

display= Text(window_object,height=15,width=25)
display.grid(row=2)





window_object.mainloop()

