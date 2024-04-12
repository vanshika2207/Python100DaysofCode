from tkinter import *

window=Tk()
window.title("Understanding grid system")
window.minsize(width=500,height=500)

label=Label(text="Hello Vanshika",font=("Arial",12,"bold"))
label.grid(column=0,row=0)

#Buttons
def action():
    print("Do something")

#calls action() when pressed
button = Button(text="Click Me", command=action)
button.grid(row=1,column=1)

new_button=Button(text="Click Me", command=action)
new_button.grid(row=0,column=2)

#Entries
entry = Entry(width=30)
#Add some text to begin with
entry.insert(END, string="Some text to begin with.")
#Gets text in entry
print(entry.get())
entry.grid(row=2,column=3)











window.mainloop()