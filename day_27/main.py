import tkinter


def button_clicked():
    value_entry = my_entry.get()
    my_label.config(text=value_entry)


window = tkinter.Tk()
window.title("titulo ventana")
window.minsize(width=500, height=300)

my_label = tkinter.Label(text="Una etiqueta", font=("Cascadia Code", 24, "bold"))
my_label.grid(column=0, row=0)

my_button = tkinter.Button(text="Click Me", command=button_clicked)
my_button.grid(column=1, row=1)

my_other_button = tkinter.Button(text="Other button", command=button_clicked)
my_other_button.grid(column=2, row=0)

my_entry = tkinter.Entry(width=20, font=("Cascadia Code", 10))
my_entry.insert(tkinter.END, string="Escribe tu nombre")
my_entry.grid(column=3, row=2)

window.mainloop()
