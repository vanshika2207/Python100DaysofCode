# ---------------------------- PASSWORD GENERATOR ------------------------------- #
import pyperclip as pyperclip

import pyperclip
def generate_pass():
    import random
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [random.choice(letters) for _ in range(nr_letters)]
    password_list+= [random.choice(symbols) for _ in range(nr_symbols)]
    password_list += [random.choice(numbers) for _ in range(nr_numbers)]

    random.shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(0,password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
from tkinter import messagebox
def save_pass():
    website=website_entry.get()
    email=email_entry.get()
    password=password_entry.get()
    if len(website)==0 or len(password)==0:
        messagebox.showerror(title=website,message="Fields should not be left empty")
    else:

        is_ok=messagebox.askokcancel(title=website,message=f"These are the details entered:\nEmail:{email}"
                                                           f"\nPasword:{password} \n is it ok to save ?")
        if is_ok:

            with open('saved_password.csv',mode="a") as save:
                save.write(website+" | "+email+" | "+password +'\n')
            website_entry.delete(0, 'end')
            password_entry.delete(0, 'end')
            email_entry.delete(0, 'end')

# ---------------------------- UI SETUP ------------------------------- #
from tkinter import *
window=Tk()
window.title("Password Manager")
window.config(padx=50,pady=20,bg="white")
canvas=Canvas(width=200,height=200,bg="white",highlightthickness=0)
logo=PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo)
canvas.grid(row=0,column=1)
website_label=Label(text="Website:",font=("Arial",10,"normal"),bg="white")
website_label.grid(row=1, column=0)
website_entry=Entry(width=35)
website_entry.insert(END, string="")
website_entry.grid(row=1,column=1,columnspan=2)
website_entry.focus()
email_label=Label(text="Email/Username:",font=("Arial",10,"normal"),bg="white")
email_label.grid(row=2, column=0)
email_entry=Entry(width=35)
email_entry.insert(0, string="vanshikasaxena0207@gmail.com")
email_entry.grid(row=2,column=1,columnspan=2)
password_label=Label(text="Password:",font=("Arial",10,"normal"),bg="white")
password_label.grid(row=3, column=0)
password_entry=Entry(width=21)
password_entry.insert(END, string="")
password_entry.grid(row=3,column=1)



generate_password = Button(text="Generate Password", command=generate_pass,width=16)
generate_password.grid(row=3,column=2)




add_password = Button(text="Add", command=save_pass,width=36)
add_password.grid(row=4,column=1,columnspan=2)


window.mainloop()













