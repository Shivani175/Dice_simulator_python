import tkinter as tk
import random as r

class Rolling():
    def __init__(self,root):  
        self.root =root
        l1 = tk.Label(self.root, text="Rolling Dice", font="arial 10 bold", bg="grey").pack()
        self.b1 =  tk.Button(self.root, text="Let's start it",font="arial 15 bold",command=self.roll)
        self.b1.pack(pady=50)
    def roll(self):
        self.num = r.randrange(0,6)  
        self.b1.forget()
        self.image()
        self.b1 = tk.Button(self.root,image=self.p1,command=self.roll)
        self.b1.pack(pady=50)
    def image(self):
        img = ['dice1.png','dice2.png','dice3.png','dice4.png','dice5.png','dice6.png']   
        self.p1 = tk.PhotoImage(file=img[self.num])
        


root=tk.Tk() #to create a gui window
root.title("Rolling Dice")
root.geometry('250x250')
run = Rolling(root)
root.mainloop()
