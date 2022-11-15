# tkinter is a python library that enables a window with widgets or also called GUI(graphical user interface)


from tkinter import *
window_object= Tk()

def cm_to_m():

  cm= float(entry_value.get())
  calculation= str(cm/100)
  output= f'{calculation} metres'

  text.insert(END,output)




btn= Button(window_object,background='red',text='Execute',font='Tahoma',borderwidth= 2,command=cm_to_m)

btn.grid(row=0,column=0)

entry_value= StringVar()
entry= Entry(window_object,textvariable=entry_value)
entry.grid(row=0,column=1)

text= Text(window_object,height=1,width=15)
text.grid(row=0,column=2)


window_object.mainloop()