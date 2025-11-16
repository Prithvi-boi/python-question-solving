from tkinter import *
from PIL import Image, ImageTk
import time
import random
#///////////////////////////////////////////// Button clicked Functions ///////////////////////////////////////////////////////////////////

def Show_running_bg():
    slot_run_pil = Image.open(
    r"C:\Users\prithvi\OneDrive\Coding\COLLEGE\python-question-solving\Tkinter Projects\00_Project_images\Slot_bg2.png"
    ).convert("RGBA")

    slot_machine_running_img = ImageTk.PhotoImage(slot_run_pil)
    slot_label.config(image=slot_machine_running_img)
    slot_label.image = slot_machine_running_img

    window.update()
    time.sleep(2)

    slot_label.config(image=slot_machine_img)
    slot_label.image = slot_machine_img
   
def Show_btn(btn_img_location,pos_x,btn_name):
    global Your_button
    Your_button = Image.open(
        btn_img_location
    ).convert('RGBA')
    Your_button = Your_button.resize((150,70))

    bx, by = pos_x,350
    btn_width, btn_heigth = Your_button.size
    
    background_crop = slot_pil.crop((bx, by, bx + btn_width, by + btn_heigth))
    comp = Image.alpha_composite(background_crop, Your_button)

    Your_button_tk = ImageTk.PhotoImage(comp)
    Your_button_lab = Label(window, image=Your_button_tk, bd=0, highlightthickness=0)
    Your_button_lab.place(x=bx, y=by)
    Your_button_lab.bind("<Button-1>", lambda e: button_click(btn_name))
    
    # Keep reference to prevent garbage collection
    Your_button_lab.image = Your_button_tk

def button_click(btn_function):
    if btn_function == 'spin':
        Show_btn(
            btn_img_location=r'C:\Users\prithvi\OneDrive\Coding\COLLEGE\python-question-solving\Tkinter Projects\00_Project_images\Btn_Pngs\Spin_Clicked.png',
            pos_x=500,
            btn_name='None'
        )
        window.update()
        time.sleep(0.2)
        Show_btn(
            btn_img_location=r'C:\Users\prithvi\OneDrive\Coding\COLLEGE\python-question-solving\Tkinter Projects\00_Project_images\Btn_Pngs\Spin_Un-Clicked.png',
            pos_x=500,
            btn_name='spin'
        )
        Show_running_bg()
        global fruits_list 
        spin_reel()
    
    elif btn_function == 'bet':
        Show_btn(
            btn_img_location=r'C:\Users\prithvi\OneDrive\Coding\COLLEGE\python-question-solving\Tkinter Projects\00_Project_images\Btn_Pngs\Bet_Clicked.png',
            pos_x=100,
            btn_name='None'
        )

        window.update()
        time.sleep(0.2)
        Show_btn(
            btn_img_location=r'C:\Users\prithvi\OneDrive\Coding\COLLEGE\python-question-solving\Tkinter Projects\00_Project_images\Btn_Pngs\Bet_Un-Clicked.png',
            pos_x=100,
            btn_name='bet'
        )

        global bet_num
        bet_num += 1

        if bet_num > 3:
            bet_num -= 1

        if bet_num == 2:
            count_text.config(text=str(bet_num))
        elif bet_num == 3:
            count_text.config(text=str(bet_num))
    
    elif btn_function == 'bet_max':
        Show_btn(
            btn_img_location=r'C:\Users\prithvi\OneDrive\Coding\COLLEGE\python-question-solving\Tkinter Projects\00_Project_images\Btn_Pngs\Bet_Max_Clicked.png',
            pos_x=250,
            btn_name='None'
        )

        window.update()
        time.sleep(0.2)
        Show_btn(
            btn_img_location=r'C:\Users\prithvi\OneDrive\Coding\COLLEGE\python-question-solving\Tkinter Projects\00_Project_images\Btn_Pngs\Bet_Max_Un-Clicked.png',
            pos_x=250,
            btn_name='bet_max'
        )

        # global bet_num
        bet_num += 2
        if bet_num == 4:
            bet_num -= 2
            bet_num += 1
        elif bet_num > 3:
            bet_num -= 2
        count_text.config(text=str(bet_num))

        Show_running_bg()
        spin_reel()

#///////////////////////////////////////////// Reel Logic Functions ///////////////////////////////////////////////////////////////////

bet_num = 1
fruits_list = ['🍇','🍊','🍎','🍌','🍉','🥥']
current_balance = 100

def spin_effect(px,py):
    new_reel = Label(text='',font=('Impact',50,'bold'),bg="#FFFFFF")
    new_reel.place(x=px,y=py)

    for i in range(0,6):
        window.update()
        time.sleep(0.1)
        new_reel.config(text=fruits_list[i])

def spin_reel():
    global current_balance
    reel1num = random.randint(0,5)
    reel1emoji = fruits_list[reel1num]

    reel2num = random.randint(0,5)
    reel2emoji = fruits_list[reel2num]

    reel3num = random.randint(0,5)
    reel3emoji = fruits_list[reel3num]

    def result_emoji(pos_x,emoji):
            reel = Label(text=emoji,font=('Impact',50,'bold'),bg="#FFFFFF")
            reel.place(x=pos_x,y=130)
    
    spin_effect(220,130)
    result_emoji(220,reel1emoji)

    spin_effect(340,130)
    result_emoji(340,reel2emoji)

    spin_effect(460,130)
    result_emoji(460,reel3emoji)

    if reel1num == reel2num == reel3num:
        if bet_num == 1:
            current_balance += 50
            current_balance_lab.config(text=current_balance)
            win_amount.config(text='+50',fg='green')
        elif bet_num == 2:
            current_balance += 50*2
            current_balance_lab.config(text=current_balance)
            win_amount.config(text='+100',fg='green')
        elif bet_num == 3:
            current_balance += 50*3
            current_balance_lab.config(text=current_balance)
            win_amount.config(text='+150',fg='green')
    elif reel1num == reel2num or reel2num == reel3num or reel1num == reel3num:
        if bet_num == 1:
            current_balance += 20
            current_balance_lab.config(text=current_balance)
            win_amount.config(text='+20',fg='green')
        elif bet_num == 2:
            current_balance += 20*2
            current_balance_lab.config(text=current_balance)
            win_amount.config(text='+40',fg='green')
        elif bet_num == 3:
            current_balance += 20*3
            current_balance_lab.config(text=current_balance)
            win_amount.config(text='+60',fg='green')
    else:
        if bet_num == 1:
            current_balance -= 10
            current_balance_lab.config(text=current_balance)
            win_amount.config(text='-10',fg='red')
        elif bet_num == 2:
            current_balance -= 20*2
            current_balance_lab.config(text=current_balance)
            win_amount.config(text='-40',fg='red')
        elif bet_num == 3:
            current_balance -= 30*3
            current_balance_lab.config(text=current_balance)
            win_amount.config(text='-90',fg='red')

def default_emoji():
    reel1 = Label(text=fruits_list[random.randint(0,5)],font=('Impact',50,'bold'),bg="#FFFFFF")
    reel1.place(x=220,y=130)

    reel2 = Label(text=fruits_list[random.randint(0,5)],font=('Impact',50,'bold'),bg="#FFFFFF")
    reel2.place(x=330,y=130)

    reel3 = Label(text=fruits_list[random.randint(0,5)],font=('Impact',50,'bold'),bg="#FFFFFF")
    reel3.place(x=450,y=130)
#///////////////////////////////////////////// Tkinter Window ///////////////////////////////////////////////////////////////////

window = Tk()
window.geometry('800x650')
window.resizable(False,False)

# == Load slot machine background ==
slot_pil = Image.open(
    r"C:\Users\prithvi\OneDrive\Coding\COLLEGE\python-question-solving\Tkinter Projects\00_Project_images\Btn_Pngs\Slot_Bg.png"
).convert("RGBA")

slot_machine_img = ImageTk.PhotoImage(slot_pil)
slot_label = Label(window, image=slot_machine_img)
slot_label.pack()

# == Load Buttons on machine background As a png ==

default_emoji()

Show_btn(
    btn_img_location=r'C:\Users\prithvi\OneDrive\Coding\COLLEGE\python-question-solving\Tkinter Projects\00_Project_images\Btn_Pngs\Spin_Un-Clicked.png',
    pos_x=500,
    btn_name='spin'
)

Show_btn(
    btn_img_location=r'C:\Users\prithvi\OneDrive\Coding\COLLEGE\python-question-solving\Tkinter Projects\00_Project_images\Btn_Pngs\Bet_Un-Clicked.png',
    pos_x=100,
    btn_name='bet'
)

Show_btn(
    btn_img_location=r'C:\Users\prithvi\OneDrive\Coding\COLLEGE\python-question-solving\Tkinter Projects\00_Project_images\Btn_Pngs\Bet_Max_Un-Clicked.png',
    pos_x=250,
    btn_name='bet_max'
)

count_text = Label(text='1',font=('Impact',20,'bold'),fg='red',bg='#210808')
count_text.place(x=570,y=493)

current_balance_lab = Label(text=str(current_balance),font=('Impact',20,'bold'),fg='red',bg='#210808')
current_balance_lab.place(x=350,y=493)

win_amount = Label(text='000',font=('Impact',20,'bold'),fg="green",bg='#210808')
win_amount.place(x=170,y=493)

window.mainloop()