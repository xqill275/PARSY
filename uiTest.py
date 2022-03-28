from tkinter import *


def MakeAccount():
    signUpScreen = Toplevel(root)
    username = Label(signUpScreen, text = "username:")
    password = Label(signUpScreen, text = "password:")
    comfirmPassword = Label(signUpScreen, text = "confirm password")

  
# grid method to arrange labels in respective
# rows and columns as specified
    username.grid(row = 0, column = 0, sticky = W, pady = 2)
    password.grid(row = 1, column = 0, sticky = W, pady = 2)
    comfirmPassword.grid(row=2, column = 0, sticky = W, pady = 2)
    
  
# entry widgets, used to take entry from user
    e1 = Entry(signUpScreen)
    e2 = Entry(signUpScreen)
    e3 = Entry(signUpScreen)
  
# this will arrange entry widgets
    e1.grid(row = 0, column = 1, pady = 2)
    e2.grid(row = 1, column = 1, pady = 2)
    e3.grid(row = 2, column = 1, pady = 2)

    signUpButton = Button(signUpScreen,text = "sign Up!",command = getUserData(e2,e3))
    signUpButton.grid(row=3, column = 0, sticky = W, pady = 2)
    e3.grid(row = 2, column = 1, pady = 2)
    
def getUserData(e2,e3):
    testPass = e2.get()
    testConfirm = e3.get()
    if testPass != testConfirm:
        warning = Label(signUpScreen,text = "passwords do not match!",colour = red)
        warning.pack()
        
    

root = Tk()

width_= 300
height_ = 100

canvas = Canvas(root,height= height_, width = width_)
canvas.pack()

TitleFrame = Frame(root)
TitleFrame.pack(side = TOP)

menuFrame = Frame(root)
menuFrame.pack()

title = Label(TitleFrame, text = "parrsy!", height = 5,width = 5,font = ("Arial",25))
title.pack()

login = Button(menuFrame,text = "log in!")
login.pack()

createAccount = Button(menuFrame,text = "create account!",command = MakeAccount)
createAccount.pack()

exit_ = Button(menuFrame,text = "exit")
exit_.pack()

root.mainloop()
