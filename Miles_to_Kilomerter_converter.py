from tkinter import *


# program for Miles to kilometers conversion calculation
def Miles_to_kilo():
    miles = float(entry.get())
    km = miles * 1.609344
    label1.config(text=f"{km}")


# Main/root window
window = Tk()
window.minsize(width=300, height=100)
window.title("Miles to Km Converter")
window.config(padx=50, pady=20)

# Entry (input for Miles to covert in Km)
entry = Entry(width=10)
entry.grid(column=1, row=0)

# Label (Miles)
mile_label = Label(text="Miles")
mile_label.grid(column=2, row=0)
mile_label.config(pady=10, padx=10)

# Label (is equal to)
label = Label(text="is equal to")
label.grid(column=0, row=1)

# Label (0)
label1 = Label(text='0')
label1.grid(column=1, row=1)
label1.config(pady=10, padx=10)

# Label (Km)
label2 = Label(text="Km")
label2.grid(column=2, row=1)

# Button (Calculate)
button = Button(text="Calculate", command=Miles_to_kilo)
button.grid(column=1, row=2)
button.config(pady=10, padx=10)
# button.config(command=Miles_to_kilo)

window.mainloop()
