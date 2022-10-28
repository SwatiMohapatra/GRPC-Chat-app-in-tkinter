import os
from tkinter import *
from functools import partial
from dbFiles.database import signup
# def validateLogin(self,username, password):
# 	print("username entered :", username.get())
# 	print("password entered :", password.get())

#window
tkWindow = Tk()  
tkWindow.geometry('400x150')  
tkWindow.title('RPC MECHANISM - SIGNUP')

#username label and text entry box
usernameLabel = Label(tkWindow, text="User Name").grid(row=0, column=0)
username = StringVar()
usernameEntry = Entry(tkWindow, textvariable=username).grid(row=0, column=1)  

#password label and password entry box
passwordLabel = Label(tkWindow,text="Password").grid(row=1, column=0)  
password = StringVar()
passwordEntry = Entry(tkWindow, textvariable=password, show='*').grid(row=1, column=1)  



def validateSignUp():
    global username,password
    signup(username.get(),password.get())

def goToLogin():
    tkWindow.destroy()
    os.system('python login.py')   #its juz like writinhg command in cmd prompt

#login button 
loginButton = Button(tkWindow, text="Signup", command=validateSignUp).grid(row=4, column=0)  
signupButton = Button(tkWindow, text="GO TO LOGIN", command=goToLogin).grid(row=5, column=0)  

tkWindow.mainloop()