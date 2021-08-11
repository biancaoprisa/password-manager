from tkinter import *
from tkinter import messagebox
import random

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    chars = [random.choice(letters) for char in range(nr_letters)]
    symb = [random.choice(symbols) for char in range(nr_symbols)]
    nums = [random.choice(numbers) for num in range(nr_numbers)]

    password_list = chars + symb + nums

    random.shuffle(password_list)

    password = "".join(password_list)

    password_input.insert(0, password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    details = f"\n{website_input.get()} | {email_input.get()} | {password_input.get()}"
    if len(website_input.get()) > 0 or len(password_input.get()) > 0:
        is_ok = messagebox.askokcancel(title=website_input.get(), message=f"These are the details you have entered:\nEmail: {email_input.get()}\nPassword: {password_input.get()}")

        if is_ok:
            with open("data.txt", mode="a") as data:
                data.write(details)
                website_input.delete(0, "end")
                password_input.delete(0, "end")
    else:
        messagebox.showinfo(title="Empty Fields", message="Please don't leave any fields empty!")




# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("My Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
locker_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=locker_img)
canvas.grid(row=0, column=1)

website_label = Label(text="Website")
website_label.grid(row=1, column=0)

email_label = Label(text="Email/Username")
email_label.grid(row=2, column=0)

password_label = Label(text="Password")
password_label.grid(row=3, column=0)

website_input = Entry(width=35)
website_input.grid(row=1, column=1, columnspan=2 )
website_input.focus()

email_input = Entry(width=35)
email_input.grid(row=2, column=1, columnspan=2)
email_input.insert(0, "bianca@gmail.com")

password_input = Entry(width=20)
password_input.grid(row=3, column=1)

password_button = Button(text="Generate Password", command=generate_password)
password_button.grid(row=3, column=2)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)



window.mainloop()