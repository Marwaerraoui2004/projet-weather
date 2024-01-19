import tkinter
from subprocess import call
from tkinter import messagebox

app=tkinter.Tk()
app.title("login form")
app.geometry('340x440')
app.configure(bg='#000000')
def login(): 
    
    print("hello user ")
    username="mounamarwa"
    password="1234567"
    if password_entry.get()==password and username_entry.get()==username:
        messagebox.showinfo(title='login success',message="you successfuly loged in")
    else:
        messagebox.showerror(title="error",message="invalid login")
    
    app.destroy()
    call(["python",r"C:\Users\HP PRO\Desktop\projet weather tkinter\weather.py"])
    
frame=tkinter.Frame(bg='#000000')

login_label=tkinter. Label (frame, text="Login", bg='#000000',fg='#FFFFFF',font=("arial",30))
username_label=tkinter. Label (frame, text="Username", bg='#CE5A67',fg='#FFFFFF',font=("arial",16))
username_entry = tkinter. Entry (frame,font=("arial",16))
password_entry=tkinter. Entry (frame, show="*",font=("arial",16))
password_label =tkinter. Label (frame, text="Password", bg='#CE5A67',fg='#FFFFFF',font=("arial",16))
login_button=tkinter.Button(frame, text="Login" ,bg='#CE5A67',fg='#FFFFFF',font=("arial",16),command=login)
# Placing widgets on the screen
login_label.grid(row=0, column=0, columnspan=2,sticky='news',pady='40')
username_label.grid(row=1, column=0)
username_entry.grid(row=1, column=1,pady='20')
password_label.grid(row=2, column=0)
password_entry.grid(row=2, column=1,pady='20')
login_button.grid(row=3,column=0, columnspan=2,pady='30')




frame.pack()

app.mainloop()