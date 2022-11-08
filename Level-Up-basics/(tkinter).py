# tkinter is a python library that enables a window with widgets or also called GUI(graphical user interface)


from tkinter import *
window_object= Tk()

def m_to_cm():
  text.insert(END,( str((int(entry_value.get()))/ 100)+ 'cm'))



btn= Button(window_object,background='red',text='Execute',font='Tahoma',borderwidth= 2,command=m_to_cm)

btn.grid(row=0,column=0)

entry_value= StringVar()
entry= Entry(window_object,textvariable=entry_value)
entry.grid(row=0,column=1)

text= Text(window_object,height=1,width=4)
text.grid(row=0,column=2)


window_object.mainloop()