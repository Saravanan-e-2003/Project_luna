import pyautogui
import random
import tkinter as tk

x = 1000
cycle = 0
check = 1
idle_num =[1,2,3,4]
play_num = [10,11,12,13,15]
walk_left = [6,7]
walk_right = [8,9]
jump_num = [16,17,18]
event_number = random.randrange(1,3,1)
impath = 'Assets/'

#transfer random no. to event
def event(cycle,check,event_number,x):
    if event_number in idle_num:
        check = 0
        window.after(100,update,cycle,check,event_number,x) #no. 1,2,3,4 = idle
    elif event_number == 5:
        check = 1
        window.after(100,update,cycle,check,event_number,x) #no. 5 = idle to sleep
    elif event_number in walk_left:
        check = 4
        window.after(100,update,cycle,check,event_number,x)#no. 6,7 = walk towards left
    elif event_number in walk_right:
        check = 5
        window.after(100,update,cycle,check,event_number,x)#no 8,9 = walk towards right
    elif event_number in jump_num:
        check  = 6
        print("jump")
        window.after(100,update,cycle,check,event_number,x)#no. 16,17 = sleep
    elif event_number in play_num:
        check  = 2
        window.after(100,update,cycle,check,event_number,x)#no. 10,11,12,13,15 = play
    elif event_number == 14:
        check = 3
        window.after(100,update,cycle,check,event_number,x)#no. 15 = sleep to idle

#looping through gif frames
def gif_work(cycle,frames,event_number,first_num,last_num):
    if cycle < len(frames) -1:
        cycle+=1
    else:
        cycle = 0
        event_number = random.randrange(first_num,last_num+1,1)
    return cycle,event_number

def update(cycle,check,event_number,x):

    if check ==0:
        frame = idle[cycle]
        cycle ,event_number = gif_work(cycle,idle,event_number,1,9)
    elif check ==1:
        frame = idle_to_lick[cycle]
        cycle ,event_number = gif_work(cycle,idle_to_lick,event_number,10,10)
    elif check == 2:
        frame = play[cycle]
        cycle ,event_number = gif_work(cycle,play,event_number,10,15)
    elif check ==3:
        frame = play_to_lick[cycle]
        cycle ,event_number = gif_work(cycle,play_to_lick,event_number,1,1)
    elif check == 4:
        frame = walk_positive[cycle]
        cycle , event_number = gif_work(cycle,walk_positive,event_number,1,9)
        x -= 10
    elif check == 5:
        frame = walk_negative[cycle]
        cycle , event_number = gif_work(cycle,walk_negative,event_number,1,9)
        x -= -10
    elif check == 6:
        frame = jump[cycle]
        cycle , event_number = gif_work(cycle,jump,event_number,15,18)
        print("atUpdate")
    window.geometry('100x100+'+str(x)+'-57')
    label.configure(image=frame)
    window.after(1,event,cycle,check,event_number,x)

window = tk.Tk()

#Assets calling
idle = [tk.PhotoImage(file=impath+'idle.gif',format = 'gif -index %i' %(i)) for i in range(8)]#idle gif
idle_to_lick = [tk.PhotoImage(file=impath+'lick.gif',format = 'gif -index %i' %(i)) for i in range(8)]#idle to sleep gif
play = [tk.PhotoImage(file=impath+'play.gif',format = 'gif -index %i' %(i)) for i in range(3)]#sleep gif
play_to_lick = [tk.PhotoImage(file=impath+'lick.gif',format = 'gif -index %i' %(i)) for i in range(8)]#sleep to idle gif
walk_positive = [tk.PhotoImage(file=impath+'run_negative.gif',format = 'gif -index %i' %(i)) for i in range(8)]#walk to left gif
walk_negative = [tk.PhotoImage(file=impath+'run.gif',format = 'gif -index %i' %(i)) for i in range(8)]#walk to right gif
jump = [tk.PhotoImage(file=impath+'jump.gif',format = 'gif -index %i' %(i)) for i in range(6)]

window.config(highlightbackground='black')
label = tk.Label(window,bd=0,bg='black')
window.overrideredirect(True)
window.wm_attributes('-transparentcolor','black')
label.pack()

#main event loop
window.after(1,update,cycle,check,event_number,x)
window.mainloop()