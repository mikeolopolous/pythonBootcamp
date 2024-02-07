import tkinter


window = tkinter.Tk()
window.title("First GUI program")
window.minsize(width=500, height=300)

# Label
my_label = tkinter.Label(text="I am a label", font=("Arial", 24))
my_label.pack()

# my_label["text"] = "Change label text!"
# my_label.config(text="Change label text again!")


# Widget functions
def button_clicked():
    value_input = input_txt.get()
    value_text = text.get("1.0", tkinter.END)

    my_label.config(text=value_input)
    print(value_text)


def spinbox_used():
    print(spinbox.get())


def scale_used(value):
    print(value)


def checkbutton_used():
    print(checked_state.get())


def radio_used():
    print(radio_state.get())


def listbox_used(event):
    print(listbox.get(listbox.curselection()))


# Button
button = tkinter.Button(text="Click me!", command=button_clicked)
button.pack()

# Entries
input_txt = tkinter.Entry(width=10)
input_txt.insert(tkinter.END, string="Insert method")
input_txt.pack()

# Text
text = tkinter.Text(width=30, height=5)
text.focus()
text.insert(tkinter.END, chars="Hello World!")
# print(text.get("1.0", tkinter.END))
text.pack()

# Spinbox
spinbox = tkinter.Spinbox(from_=0, to=100, command=spinbox_used)
spinbox.pack()

# Scale
scale = tkinter.Scale(from_=0, to=100, command=scale_used)
scale.pack()

# Checkbutton
checked_state = tkinter.IntVar()
checkbutton = tkinter.Checkbutton(text="Is on?", variable=checked_state, command=checkbutton_used)
print(checked_state.get())
checkbutton.pack()

# Radiobutton
radio_state = tkinter.IntVar()
radio_button1 = tkinter.Radiobutton(text="Option 1", value=1, variable=radio_state, command=radio_used)
radio_button2 = tkinter.Radiobutton(text="Option 2", value=2, variable=radio_state, command=radio_used)
radio_button1.pack()
radio_button2.pack()

# Listbox
listbox = tkinter.Listbox(height=4)
fruits = ["apple", "banana", "orange", "pear"]

for fruit in fruits:
    listbox.insert(fruits.index(fruit), fruit)

listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()


window.mainloop()
