from tkinter import *

window = Tk()
window.title("This is main window!")
window.minsize(width=500, height=400)

# Label

my_label = Label(text="This is a label.", font=('arial', 15, "italic"))
my_label.pack()

# my_label['text'] = 'this is text1'


# Button

def click_button():
    print('button clicked!')
    new_text = input.get()
    my_label.config(text=new_text)


# input

input = Entry()
input.pack()
# print(input.get())


button = Button(text='submit!', command=click_button)
button.pack()

window.mainloop()
