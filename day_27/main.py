import tkinter


window = tkinter.Tk()
window.title("First GUI program")
window.minsize(width=500, height=300)

my_label = tkinter.Label(text="I am a label", font=("Arial", 24))
my_label.pack()

window.mainloop()