import tkinter


def on_click_button():
    miles = float(miles_entry.get())
    kms = miles * 1.609
    km_result_label.config(text=f"{kms}")


window = tkinter.Tk()
window.title("Mile to Km Converter")
window.minsize(width=200, height=100)
window.config(padx=25, pady=25)

simple_label = tkinter.Label(text="is equal to")
simple_label.grid(column=0, row=1)

miles_entry = tkinter.Entry(width=8)
miles_entry.focus()
miles_entry.grid(column=1, row=0)

miles_label = tkinter.Label(text="Miles")
miles_label.grid(column=2, row=0)

km_result_label = tkinter.Label(text="0")
km_result_label.grid(column=1, row=1)

km_label = tkinter.Label(text="Km")
km_label.grid(column=2, row=1)

calculate_button = tkinter.Button(text="Calculate", command=on_click_button)
calculate_button.grid(column=1, row=2)

window.mainloop()
