from tkinter import *
from PIL import Image, ImageTk
import time
import random
#///////////////////////////////////////////// Running Functions ///////////////////////////////////////////////////////////////////

def Show_running_bg():
    slot_pil2 = Image.open(
    r"C:\Users\prithvi\OneDrive\Coding\COLLEGE\python-question-solving\Tkinter Projects\00_Project_images\Slot_bg2.png"
    ).convert("RGBA")

    slot_machine_img2 = ImageTk.PhotoImage(slot_pil2)
    slot_label.config(image=slot_machine_img2)
    slot_label.image = slot_machine_img2

    window.update()
    time.sleep(2)

    slot_label.config(image=slot_machine_img)
    slot_label.image = slot_machine_img

def Show_Bet_Btns():
    global betbtn
    betbtn = Image.open(
        r'C:\Users\prithvi\OneDrive\Coding\COLLEGE\python-question-solving\Tkinter Projects\00_Project_images\Btn_Pngs\Bet_Un-Clicked.png'
    ).convert('RGBA')
    betbtn = betbtn.resize((150,70))

    bx, by = 100, 350
    btn_width, btn_heigth = betbtn.size
    
    background_crop = slot_pil.crop((bx, by, bx + btn_width, by + btn_heigth))
    comp = Image.alpha_composite(background_crop, betbtn)

    betbtn_tk = ImageTk.PhotoImage(comp)
    betbtn_lab = Label(window, image=betbtn_tk, bd=0, highlightthickness=0)
    betbtn_lab.place(x=bx, y=by)
    betbtn_lab.bind("<Button-1>", Bet_clicked)
    
    # Keep reference to prevent garbage collection
    betbtn_lab.image = betbtn_tk
def Bet_clicked(event=None):
    betbtn = Image.open(
    r'C:\Users\prithvi\OneDrive\Coding\COLLEGE\python-question-solving\Tkinter Projects\00_Project_images\Btn_Pngs\Bet_Clicked.png'
    ).convert('RGBA')

    betbtn = betbtn.resize((150,70))

    bx, by = 100, 350
    btn_width, btn_heigth = betbtn.size
    
    background_crop = slot_pil.crop((bx, by, bx + btn_width, by + btn_heigth))
    comp = Image.alpha_composite(background_crop, betbtn)

    betbtn_tk = ImageTk.PhotoImage(comp)
    betbtn_lab = Label(window, image=betbtn_tk, bd=0, highlightthickness=0)
    betbtn_lab.place(x=bx, y=by)
    
    # Keep reference to prevent garbage collection
    betbtn_lab.image = betbtn_tk

    window.update()
    time.sleep(0.2)
    Show_Bet_Btns()

    global bet_num
    bet_num += 1

    if bet_num > 3:
        bet_num -= 1

    if bet_num == 2:
        count_text.config(text=str(bet_num))
    elif bet_num == 3:
        count_text.config(text=str(bet_num))

def Show_MaxBet_Btns():
    global Maxbetbtn
    Maxbetbtn = Image.open(
        r'C:\Users\prithvi\OneDrive\Coding\COLLEGE\python-question-solving\Tkinter Projects\00_Project_images\Btn_Pngs\Bet_Max_Un-Clicked.png'
    ).convert('RGBA')
    Maxbetbtn = Maxbetbtn.resize((150,70))

    bx, by = 250, 350
    btn_width, btn_heigth = Maxbetbtn.size
    
    background_crop = slot_pil.crop((bx, by, bx + btn_width, by + btn_heigth))
    comp = Image.alpha_composite(background_crop, Maxbetbtn)

    Maxbetbtn_tk = ImageTk.PhotoImage(comp)
    Maxbetbtn_lab = Label(window, image=Maxbetbtn_tk, bd=0, highlightthickness=0)
    Maxbetbtn_lab.place(x=bx, y=by)
    Maxbetbtn_lab.bind("<Button-1>", MaxBet_clicked)
    
    # Keep reference to prevent garbage collection
    Maxbetbtn_lab.image = Maxbetbtn_tk
def MaxBet_clicked(event=None):
    Maxbetbtn = Image.open(
        r'C:\Users\prithvi\OneDrive\Coding\COLLEGE\python-question-solving\Tkinter Projects\00_Project_images\Btn_Pngs\Bet_Max_Clicked.png'
    ).convert('RGBA')
    Maxbetbtn = Maxbetbtn.resize((150,70))

    bx, by = 250, 350
    btn_width, btn_heigth = Maxbetbtn.size
    
    background_crop = slot_pil.crop((bx, by, bx + btn_width, by + btn_heigth))
    comp = Image.alpha_composite(background_crop, Maxbetbtn)

    Maxbetbtn_tk = ImageTk.PhotoImage(comp)
    Maxbetbtn_lab = Label(window, image=Maxbetbtn_tk, bd=0, highlightthickness=0)
    Maxbetbtn_lab.place(x=bx, y=by)
    Maxbetbtn_lab.bind("<Button-1>", MaxBet_clicked)
    
    # Keep reference to prevent garbage collection
    Maxbetbtn_lab.image = Maxbetbtn_tk

    window.update()
    time.sleep(0.2)
    Show_MaxBet_Btns()

    global bet_num
    bet_num += 2
    if bet_num == 4:
        bet_num -= 2
        bet_num += 1
    elif bet_num > 3:
        bet_num -= 2
    count_text.config(text=str(bet_num))

    Show_running_bg()
    spin_reel()

def Show_Spin_Btns():
    global spinbtn
    spinbtn = Image.open(
        r'C:\Users\prithvi\OneDrive\Coding\COLLEGE\python-question-solving\Tkinter Projects\00_Project_images\Btn_Pngs\Spin_Un-Clicked.png'
    ).convert('RGBA')
    spinbtn = spinbtn.resize((150,70))

    bx, by = 500, 350
    btn_width, btn_heigth = spinbtn.size
    
    background_crop = slot_pil.crop((bx, by, bx + btn_width, by + btn_heigth))
    comp = Image.alpha_composite(background_crop, spinbtn)

    spinbtn_tk = ImageTk.PhotoImage(comp)
    spinbtn_lab = Label(window, image=spinbtn_tk, bd=0, highlightthickness=0)
    spinbtn_lab.place(x=bx, y=by)
    spinbtn_lab.bind("<Button-1>", Spin_clicked)
    
    # Keep reference to prevent garbage collection
    spinbtn_lab.image = spinbtn_tk
def Spin_clicked(event=None):

    spinbtn = Image.open(
    r'C:\Users\prithvi\OneDrive\Coding\COLLEGE\python-question-solving\Tkinter Projects\00_Project_images\Btn_Pngs\Spin_Clicked.png'
    ).convert('RGBA')

    spinbtn = spinbtn.resize((150,70))

    bx, by = 500, 350
    btn_width, btn_heigth = spinbtn.size
    
    background_crop = slot_pil.crop((bx, by, bx + btn_width, by + btn_heigth))
    comp = Image.alpha_composite(background_crop, spinbtn)

    spinbtn_tk = ImageTk.PhotoImage(comp)
    spinbtn_lab = Label(window, image=spinbtn_tk, bd=0, highlightthickness=0)
    spinbtn_lab.place(x=bx, y=by)
    
    # Keep reference to prevent garbage collection
    spinbtn_lab.image = spinbtn_tk

    window.update()
    time.sleep(0.2)
    Show_Spin_Btns()
    Show_running_bg()

    global fruits_list 
    spin_reel()

def Show_btn(btn_img_location,btn_size,pos_x,pos_y,btn_click_func):
    global Your_button
    Your_button = Image.open(
        r'C:\Users\prithvi\OneDrive\Coding\COLLEGE\python-question-solving\Tkinter Projects\00_Project_images\Btn_Pngs\Spin_Un-Clicked.png'
    ).convert('RGBA')
    Your_button = Your_button.resize((150,70))

    bx, by = 500, 350
    btn_width, btn_heigth = Your_button.size
    
    background_crop = slot_pil.crop((bx, by, bx + btn_width, by + btn_heigth))
    comp = Image.alpha_composite(background_crop, Your_button)

    Your_button_tk = ImageTk.PhotoImage(comp)
    Your_button_lab = Label(window, image=Your_button_tk, bd=0, highlightthickness=0)
    Your_button_lab.place(x=bx, y=by)
    Your_button_lab.bind("<Button-1>", Spin_clicked)
    
    # Keep reference to prevent garbage collection
    Your_button_lab.image = Your_button_tk
    

#///////////////////////////////////////////// Buttons Clicked Functions ///////////////////////////////////////////////////////////////////

bet_num = 1
fruits_list = ['🍇','🍊','🍎','🍌','🍉','🥥']
current_balance = 100
def spin_effect(px,py):
    new_reel = Label(text='',font=('Impact',50,'bold'),bg="#FFFFFF")
    new_reel.place(x=px,y=py)
    new_reel.config(text=fruits_list[0])
    window.update()
    time.sleep(0.1)
    new_reel.config(text=fruits_list[1])
    window.update()
    time.sleep(0.1)
    new_reel.config(text=fruits_list[2])
    window.update()
    time.sleep(0.1)
    new_reel.config(text=fruits_list[3])
    window.update()
    time.sleep(0.1)
    new_reel.config(text=fruits_list[4])
    window.update()
    time.sleep(0.1)
    new_reel.config(text=fruits_list[5])
    window.update()
    time.sleep(0.1)
    new_reel.config(text='')

def spin_reel():
    global current_balance
    reel1num = random.randint(0,3)
    reel1emoji = fruits_list[reel1num]

    reel2num = random.randint(0,5)
    reel2emoji = fruits_list[reel2num]

    reel3num = random.randint(0,4)
    reel3emoji = fruits_list[reel3num]

    
    spin_effect(220,130)
    reel1 = Label(text=reel1emoji,font=('Impact',50,'bold'),bg="#FFFFFF")
    reel1.place(x=220,y=130)

    spin_effect(340,130)
    reel2 = Label(text=reel2emoji,font=('Impact',50,'bold'),bg="#FFFFFF")
    reel2.place(x=330,y=130)

    spin_effect(460,130)
    reel3 = Label(text=reel3emoji,font=('Impact',50,'bold'),bg="#FFFFFF")
    reel3.place(x=450,y=130)

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
Show_Spin_Btns()
Show_Bet_Btns()
Show_MaxBet_Btns()

count_text = Label(text='1',font=('Impact',20,'bold'),fg='red',bg='#210808')
count_text.place(x=570,y=493)

current_balance_lab = Label(text=str(current_balance),font=('Impact',20,'bold'),fg='red',bg='#210808')
current_balance_lab.place(x=350,y=493)

win_amount = Label(text='000',font=('Impact',20,'bold'),fg="green",bg='#210808')
win_amount.place(x=170,y=493)

window.mainloop()