from tkinter import *
import tkinter.messagebox
from random import randint

root = Tk()
root.title('Guess The Number!')
root.geometry("550x500")
root.resizable(width=False,height=False)

RETRY=0

num_label = Label(root, text="Pick A Number\nBetween 1 and 100!", font=("Arial", 22),borderwidth=5,relief="ridge")
num_label.pack(pady=20)

def guesser():
    global RETRY
    
    if ((int(guess_box.get()))>100 or (int(guess_box.get()))<1):
        num_label.config(text="Out of bounds please input valid number")
        guess_box.delete(0, END)
    elif guess_box.get().isdigit():
       
        num_label.config(text="Pick A Number\nBetween 1 and 100!")

        
        dif = abs(num - int(guess_box.get()))
        
       

        if int(guess_box.get()) == num:
            bc = "SystemButtonFace"
            num_label.config(text="Congratulations Correct Guess!!")
            end()
        elif dif == 10:
           
            RETRY=RETRY+1
            num_label.config(text="Hint: only binary number difference!!")
            bc = "purple"
            guess_box.delete(0, END)

        elif dif < 10:
            RETRY=RETRY+1
            num_label.config(text="Hint :The required number lies between\n 0 and {}".format(num+2))
            bc = "red"
            guess_box.delete(0, END)

            
        else:
            num_label.config(text="Hint :The required number lies between\n {} and 100".format(num-2))
            RETRY=RETRY+1
            bc = "light sky blue"
            guess_box.delete(0, END)

        
        root.config(bg=bc)
       
       
    else:
        RETRY=RETRY+1
        # Delete entry and throw error message
        guess_box.delete(0, END)
        num_label.config(text="Hey! That's Not A Number!")

def end():
    global RETRY
    tkinter.messagebox.showinfo("Hello Player","You have won the game after {} retries\nThanks for playing".format(RETRY))
        
def rando():
    
    global num,RETRY
    num = randint(1,101)
   
    guess_box.delete(0, END)
   
    RETRY=0
    
    num_label.config(bg="orange", text="Enter A Number\nBetween 1 and 100\n to start!")
    root.config(bg="slateblue1")




guess_box = Entry(root, font=("Helvetica", 75), width=2,relief="raised",borderwidth=5)
guess_box.pack(pady=20)

guess_button = Button(root, text="Submit", command=guesser,font=("Arial", 14, "bold"),borderwidth=5,relief="raised",bg="yellow",width=6,height=1)
guess_button.place(x=75,y=400)
rand_button = Button(root, text="Reset Game", command=rando,font=("Arial", 14, "bold"),borderwidth=5,relief="raised",bg="yellow",width=10,height=1)
rand_button.place(x=375,y=400)


rando()

root.mainloop()
