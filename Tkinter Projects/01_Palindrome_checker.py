
from tkinter import *

mywindow = Tk()
mywindow.geometry('500x200')
mywindow.config(background='black')

def palindrome_check():
    my_text = text_input.get().lower()
    reversed_text = my_text[::-1]
    if my_text == reversed_text:
        display_text = Label(text=f'{my_text.capitalize()} is a PALINDROME!!',fg='green',bg='black',font=('Arial',25))
        display_text.pack()
        text_input.delete(0, END)
    else:
        display_text = Label(text=f'{my_text.capitalize()} is Not a PALINDROME!!',fg='red',bg='black',font=('Arial',25))
        display_text.pack()
        text_input.delete(0, END)

def remove_text():
    text_input.delete(0, END)


my_lable = Label(text='Palindrome Checker',fg='yellow',bg='black',font=('Arial',25,'bold'))
my_lable.pack()

text_input = Entry()
text_input.config(font=('Arial',20))
text_input.pack(pady=20)

submit_btn = Button()
submit_btn.config(text='Submit',command=palindrome_check)
submit_btn.pack()

remove_btn = Button()
remove_btn.config(text='remove text',command=remove_text)
remove_btn.pack(pady=10)

mywindow.mainloop()