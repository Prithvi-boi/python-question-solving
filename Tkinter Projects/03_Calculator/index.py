#--------------------------------------------------------------------------------------- Modules --------------------------------

from tkinter import *
from PIL import Image,ImageTk
import math_logic

#--------------------------------------------------------------------------------------- Python Logic ---------------------------

expression_collector = []

def show_button(btn_name,pos_x,pos_y,bg_color,btn_func):
    btn = Button(text=btn_name,font=('Arial',15,'bold'),bg=bg_color,fg='white')
    btn.config(width=4)
    btn.config(command= lambda: btn_func(btn_name))
    btn.place(x=pos_x,y=pos_y)

def display_click(btn_name):
    expression_collector.append(btn_name)
    display_text = ''.join(map(str,expression_collector))
    display.config(text=display_text)

def display_evaluation(btn_name):
    result = eval(''.join(map(str,expression_collector)))
    display.config(text=result)
    expression_collector.clear()
    expression_collector.append(result)

def display_clear(btn_name):
    display.config(text='')
    expression_collector.clear()

#--------------------------------------------------------------------------------------- Tkinter Start here -----------------

window_root = Tk()
window_root.geometry('500x500')
window_root.resizable(False,False)

calsy_bg = Image.open(r'C:\Users\prithvi\OneDrive\Coding\COLLEGE\python-question-solving\Tkinter Projects\00_Project_images\calculator_bg.png')
calsy_bg = calsy_bg.resize((500,500))
calsy_bg_tk = ImageTk.PhotoImage(calsy_bg)

calsy_bg_lab = Label(image=calsy_bg_tk)
calsy_bg_lab.pack()

display = Label(text='',font=('Arial',15,'bold'),bg='#ACDDC6',fg='black')
display.place(x=140,y=107)

show_button('9',130,167         ,'black',display_click)
show_button('8',130+60,167      ,'black',display_click)
show_button('7',130+120,167     ,'black',display_click)
show_button('6',130,167+55      ,'black',display_click)
show_button('5',130+60,167+55   ,'black',display_click)
show_button('4',130+120,167+55  ,'black',display_click)
show_button('3',130,167+110     ,'black',display_click)
show_button('2',130+60,167+110  ,'black',display_click)
show_button('1',130+120,167+110 ,'black',display_click)
show_button('0',130,167+160     ,'red'  ,display_click)
show_button('.',130+60,167+160  ,'red'  ,display_click)
show_button('/',130+120,167+160 ,'red'  ,display_click)
show_button('+',130+185,167     ,'green',display_click)
show_button('-',130+185,167+55  ,'green',display_click)
show_button('x',130+185,167+110 ,'green',display_click)
show_button('=',130+185,167+160 ,'blue' ,display_evaluation)
show_button('AC',130+270,167 ,'grey' ,display_clear)


window_root.mainloop()