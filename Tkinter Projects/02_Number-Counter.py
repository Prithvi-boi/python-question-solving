from tkinter import * 

num = 1

def count():
    global num
    num += 1
    count_text.config(text=num)
    if num == 3:
        max_btn.config(state=DISABLED)
        count_btn.config(state=DISABLED)
        reduce_btn.config(state=NORMAL)

def max_count():
    global num

    if num == 2:
        num +=1
    else:
        num += 2
    count_text.config(text=num)
    if num == 3:
        max_btn.config(state=DISABLED)
        count_btn.config(state=DISABLED)
        reduce_btn.config(state=NORMAL)

def reduce():
    global num
    num -= 1
    count_text.config(text=num)
    if num < 3:
        max_btn.config(state=NORMAL)
        count_btn.config(state=NORMAL)
    if num == 1:
        reduce_btn.config(state=DISABLED)


mywindow = Tk()
mywindow.geometry('1000x600')
mywindow.title('Click count')

background_img = PhotoImage(file='python-question-solving\\Tkinter Projects\\Project images\\02_Number-counter-Background.png')
background_label = Label(mywindow,image=background_img)
background_label.pack()

count_btn = Button(text='Count',font=('Arial',20,'bold'),command=count)
count_btn.place(x=600,y=350)

max_btn = Button(text='Max',font=('Arial',20,'bold'),command=max_count)
max_btn.place(x=490,y=350)

reduce_btn = Button(text='Reduce',font=('Arial',20,'bold'),command=reduce)
reduce_btn.place(x=390,y=460)

count_text = Label(text='1',font=('Arial',20,'bold'))
count_text.place(x=600,y=170)

mywindow.mainloop()