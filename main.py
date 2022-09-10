from tkinter import *
from tkinter import messagebox
import random
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)



    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers 
    random.shuffle(password_list)



    password = "".join(password_list)
    password_entry.insert(0,password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    
    
    
    website =website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    
    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Error",message="These are can not be empty")
    else:
    
    
        is_it_ok = messagebox.askokcancel(title="Website",message=f"These are the details: \n {email}"
                            f"\n Password : {password} \n is this ok to save?")
        if is_it_ok:
            with open("password-manager\DAta.txt","a") as f:
                f.write(f"{website} | {email} | {password} \n")
                website_entry.delete(0,END)
                password_entry.delete(0,END)
# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=20,pady=20)
canvas = Canvas(width=200,height=200)
canvas_image = PhotoImage(file="password-manager\logo.png")
canvas.create_image(100,100,image=canvas_image)
canvas.grid(row=1,column=2)



#Labels

website_label = Label(text="Website:")
website_label.grid(row=2,column=1)

email_label = Label(text="E-mail/Username:")
email_label.grid(row=3,column=1)

password_label = Label(text="Password:")
password_label.grid(row=4,column=1)

#Entries

website_entry = Entry()
website_entry.grid(row=2,column=2,columnspan=2,sticky="EW")
website_entry.focus()

email_entry = Entry()
email_entry.grid(row=3,column=2,columnspan=2,sticky="EW")
email_entry.insert(0,"someone@example.com")

password_entry = Entry()
password_entry.grid(row=4,column=2,sticky="EW")


#Buttons

add_button = Button(text="Add",command=save)
add_button.grid(row=5,column=2,columnspan=2,sticky="EW")

generate_button = Button(text="Generate",command=generate_password)
generate_button.grid(row=4,column=3,columnspan=1,sticky="EW")

window.mainloop()

