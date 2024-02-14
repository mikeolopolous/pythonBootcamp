from tkinter import *


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_password():
    value_website = website.get()
    value_username = username.get()
    value_password = password.get()

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

generate_button = Button(text="Generate Password", width=11, highlightbackground="white")
generate_button.grid(row=3, column=2)

add_button = Button(text="Add", width=32, highlightbackground="white", command=add_password)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
