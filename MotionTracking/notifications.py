from tkinter import *


class PopUp():
    
    def __init__(self,type,message):
        
        
        self.window = Toplevel()
        self.type = type
        self.message = message

    def show(self):

        self.window.lift()
        self.window.title(self.type)
        message = Label(self.window,text=self.message).grid(row=0,sticky=W)
        dismiss = Button(self.window,text="OK",command=self.window.destroy).grid(row=1,column=0)
        self.window.mainloop()