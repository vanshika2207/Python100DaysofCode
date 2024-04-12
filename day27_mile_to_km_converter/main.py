#Mile to Kilometer Converter
from tkinter import *

window=Tk()
window.title("Mile to Km Converter")
window.minsize(width=300,height=100)
window.config(padx=7,pady=7)

#Entries
entry = Entry(width=10)
#Add some text to begin with
entry.insert(END, string="0")
#Gets text in entry

entry.grid(row=0,column=1)

mile_label= Label(text="Miles",font=("Arial",11,"bold"))
mile_label.grid(row=0,column=2)

label=Label(text="is equal to",font=("Arial",11,"bold"))
label.grid(row=1,column=0)

km_label= Label(text="Km",font=("Arial",11,"bold"))
km_label.grid(row=1,column=2)

answ_label= Label(text="0",font=("Arial",11,"bold"))
answ_label.grid(row=1,column=1)

#Buttons
def action():
    miles=entry.get()
    km=int(miles)*1.60934
    answ_label.config(text=km)


#calls action() when pressed
button = Button(text="Calculate", command=action)
button.grid(row=2,column=1)






window.mainloop()