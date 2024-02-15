import pyperclip
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
           'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
           'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    new_password = "".join(password_list)
    pyperclip.copy(new_password)
    password.set(new_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    value_website = website.get()
    value_username = username.get()
    value_password = password.get()

    if value_website == "" or value_username == "":
        messagebox.showwarning(title="Oops", message="Please do not leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(
            title=value_website,
            message=f"Please confirm\nUsername: {value_username}\nPassword: {value_password}"
        )

        if is_ok:
            with open("data.txt", "a") as file:
                file.write(f"{value_website} | {value_username} | {value_password}\n")

            website.set("")
            username.set("email@email.com")
            password.set("")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password manager")
window.config(padx=50, pady=50, background="white")

canvas = Canvas(width=200, height=200, background="white", highlightthickness=0)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(row=0, column=1)

website_label = Label(text="Website: ", bg="white", fg="black")
website_label.grid(row=1, column=0)

website = StringVar(value="")
website_entry = Entry(width=35, bg="white", fg="black", highlightthickness=0, textvariable=website)
website_entry.focus()
website_entry.grid(row=1, column=1, columnspan=2)

username_label = Label(text="Email/Username: ", bg="white", fg="black")
username_label.grid(row=2, column=0)

username = StringVar(value="email@email.com")
username_entry = Entry(width=35, bg="white", fg="black", highlightthickness=0, textvariable=username)
username_entry.grid(row=2, column=1, columnspan=2)

password_label = Label(text="Password: ", bg="white", fg="black")
password_label.grid(row=3, column=0)

password = StringVar(value="")
password_entry = Entry(width=19, bg="white", fg="black", highlightthickness=0, textvariable=password)
password_entry.grid(row=3, column=1)

generate_button = Button(text="Generate Password", width=11, highlightbackground="white", command=generate_password)
generate_button.grid(row=3, column=2)

add_button = Button(text="Add", width=32, highlightbackground="white", command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
