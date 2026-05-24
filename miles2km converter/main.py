import tkinter

window = tkinter.Tk()
window.title("Program")
window.minsize(width=100,height=100)

def button_clicked(): 
    miles = input1.get()
    km = int(miles)*1.609344
    new_text = km
    win2.config(text=new_text)

win = tkinter.Label(text="Miles")
win.grid(column=2,row=0)


input1 = tkinter.Entry(width=10)
input1.grid(column=1,row=0)

win1 = tkinter.Label(text="is equal to")
win1.grid(column=0,row=1)


win2 = tkinter.Label(text="0")
win2.grid(column=1,row=1)


win = tkinter.Label(text="Kilometre")
win.grid(column=2,row=1)


enter = tkinter.Button(text="Calculate",command=button_clicked)
enter.grid(column=1,row=2)


window.mainloop()