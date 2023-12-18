from tkinter import *
from tkinter import messagebox
from PIL import ImageTk

def login():
    if usernameEntry.get()=='' or passwordEntry.get()=='':
        messagebox.showerror('Error','Fields cannot be EMPTY')
    elif usernameEntry.get()=='your_username' and passwordEntry.get()=='your_password':
        window.destroy()
        import sms

    else:
        messagebox.showerror('Error','Please enter the correct credentials.')

window = Tk()

window.geometry('1530x750+0+0')
window.title('Login of Student Management System')

window.resizable(False,False)

background = ImageTk.PhotoImage(file='back1.png')

bgLabel= Label(window,image=background)
bgLabel.place(x=0, y=0)

loginframe = Frame(window)
loginframe.place(x=630,y=150)

logoimage = ImageTk.PhotoImage(file='logo.png')

logoLabel = Label(loginframe,image=logoimage)
logoLabel.grid(row=0,column=0,columnspan=2,pady=20)

usernameLabel = Label(loginframe,text= 'Username: '
                      ,font=('times new roman',20,'bold'))
usernameLabel.grid(row=1,column=0)

usernameEntry=Entry(loginframe,font=('times new roman',15),bd=5,fg='red')
usernameEntry.grid(row=1,column=1)

passwordLabel = Label(loginframe,text= 'Password: '
                      ,font=('times new roman',20,'bold'))
passwordLabel.grid(row=2,column=0,pady=20)

passwordEntry=Entry(loginframe,font=('times new roman',15),bd=5,fg='red')
passwordEntry.grid(row=2,column=1,pady=20)

loginButton = Button(loginframe,text='LOGIN',font=('times new roman',15,'bold'),width=10
                     ,fg='white',bg='cornflowerblue',activebackground='cornflowerblue',activeforeground='white'
                     ,cursor='hand2',command=login)
loginButton.grid(row=3,column=1)

window.mainloop()
