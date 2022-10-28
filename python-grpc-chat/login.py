import os
from tkinter import *
from functools import partial
from dbFiles.database import validate,signup
# def validateLogin(self,username, password):
# 	print("username entered :", username.get())
# 	print("password entered :", password.get())

#window
tkWindow = Tk()  
tkWindow.geometry('400x150')  
tkWindow.title('Tkinter Login Form - pythonexamples.org')

#username label and text entry box
usernameLabel = Label(tkWindow, text="User Name").grid(row=0, column=0)
username = StringVar()
usernameEntry = Entry(tkWindow, textvariable=username).grid(row=0, column=1)  

#password label and password entry box
passwordLabel = Label(tkWindow,text="Password").grid(row=1, column=0)  
password = StringVar()
passwordEntry = Entry(tkWindow, textvariable=password, show='*').grid(row=1, column=1)  



def validateLogin():
    global username,password
    result = validate(username.get(),password.get())
    if(result == 1):
        tkWindow.destroy()
        os.system('python client.py')

def goToSignUp():
    tkWindow.destroy()
    os.system('python signup.py')

#login button
loginButton = Button(tkWindow, text="Login", command=validateLogin).grid(row=4, column=0)  
signupButton = Button(tkWindow, text="GO TO SIGNUP", command=goToSignUp).grid(row=5, column=0)  

tkWindow.mainloop()