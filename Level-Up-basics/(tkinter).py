# tkinter is a python library that enables a window with widgets or also called GUI(graphical user interface)


from tkinter import *
window_object= Tk()

def display_text():
  print(entry_value.get)



btn= Button(window_object,background='red',text='A cool button ',font='Tahoma',borderwidth= 2,command=display_text)

btn.grid(row=0,column=0)

entry_value= StringVar()
entry= Entry(window_object,textvariable=entry_value)
entry.grid(row=0,column=1)

text= Text(window_object,height=1,width=4)
text.grid(row=0,column=2)


window_object.mainloop()