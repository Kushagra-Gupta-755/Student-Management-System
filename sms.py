from tkinter import *
import time
import ttkthemes
from tkinter import ttk,messagebox,filedialog
from PIL import ImageTk
import pymysql
import pandas

#functionality:-

def iexit():
    result=messagebox.askyesno('EXIT','Do you want to exit?')
    if result:
        root.destroy()
    else:
        pass
def export_data():
    url=filedialog.asksaveasfilename(defaultextension='.csv')
    indexing=studentTable.get_children()
    newlist=[]
    for index in indexing:
        content=studentTable.item(index)
        datalist=content['values']
        newlist.append(datalist)

    table=pandas.DataFrame(newlist,columns=['ID','NAME','ENROLLMENT_NO','CONTACT_NUMBER','EMAIL','ADDRESS','GENDER','DOB','DAYSCHOLAR_HOSTELER','DATE_ADDED'])
    table.to_csv(url,index=False)
    messagebox.showinfo('Success','Data is saved Successfully.')
def update_student():

    def update_data():
        query = 'update student set NAME=%s,ENROLLMENT_NO=%s,CONTACT_NUMBER=%s,EMAIL=%s,ADDRESS=%s,GENDER=%s,DOB=%s,DAYSCHOLAR_HOSTELER=%s,DATE_ADDED=%s where ID=%s'
        mycursor.execute(query,(nameEntry.get(),enrollEntry.get(),contactEntry.get(),mailEntry.get(),addressEntry.get(),genderEntry.get(),dobEntry.get(),dayEntry.get(),dateEntry.get(),idEntry.get()))
        con.commit()
        messagebox.showinfo('Success',f'ID {idEntry.get()} is modified Successfully',parent=update_window)
        update_window.destroy()
        show_students()

    update_window = Toplevel()
    update_window.grab_set()
    update_window.geometry('800x750+0+0')
    update_window.title('Update Data')
    update_window.resizable(0, 0)
    idLabel = Label(update_window, text='ID: ', font=('times new roman', 20, 'bold'))
    idLabel.grid(row=0, column=0, padx=30, pady=15, sticky=W)
    idEntry = Entry(update_window, font=('times new roman', 15), width=24)
    idEntry.grid(row=0, column=1, pady=15, padx=10)

    nameLabel = Label(update_window, text='NAME: ', font=('times new roman', 20, 'bold'))
    nameLabel.grid(row=1, column=0, padx=30, pady=15, sticky=W)
    nameEntry = Entry(update_window, font=('times new roman', 15), width=24)
    nameEntry.grid(row=1, column=1, pady=15, padx=10)

    enrollLabel = Label(update_window, text='ENROLLMENT NO: ', font=('times new roman', 20, 'bold'))
    enrollLabel.grid(row=2, column=0, padx=30, pady=15, sticky=W)
    enrollEntry = Entry(update_window, font=('times new roman', 15), width=24)
    enrollEntry.grid(row=2, column=1, pady=15, padx=10)

    contactLabel = Label(update_window, text='CONTACT NUMBER: ', font=('times new roman', 20, 'bold'))
    contactLabel.grid(row=3, column=0, padx=30, pady=15, sticky=W)
    contactEntry = Entry(update_window, font=('times new roman', 15), width=24)
    contactEntry.grid(row=3, column=1, pady=15, padx=10)

    mailLabel = Label(update_window, text='E-MAIL: ', font=('times new roman', 20, 'bold'))
    mailLabel.grid(row=4, column=0, padx=30, pady=15, sticky=W)
    mailEntry = Entry(update_window, font=('times new roman', 15), width=24)
    mailEntry.grid(row=4, column=1, pady=15, padx=10)

    addressLabel = Label(update_window, text='ADDRESS: ', font=('times new roman', 20, 'bold'))
    addressLabel.grid(row=5, column=0, padx=30, pady=15, sticky=W)
    addressEntry = Entry(update_window, font=('times new roman', 15), width=24)
    addressEntry.grid(row=5, column=1, pady=15, padx=10)

    genderLabel = Label(update_window, text='GENDER: ', font=('times new roman', 20, 'bold'))
    genderLabel.grid(row=6, column=0, padx=30, pady=15, sticky=W)
    genderEntry = Entry(update_window, font=('times new roman', 15), width=24)
    genderEntry.grid(row=6, column=1, pady=15, padx=10)

    dobLabel = Label(update_window, text='D.O.B: ', font=('times new roman', 20, 'bold'))
    dobLabel.grid(row=7, column=0, padx=30, pady=15, sticky=W)
    dobEntry = Entry(update_window, font=('times new roman', 15), width=24)
    dobEntry.grid(row=7, column=1, pady=15, padx=10)

    dayLabel = Label(update_window, text='DAY-SCHOLAR/HOSTELLER: ', font=('times new roman', 20, 'bold'))
    dayLabel.grid(row=8, column=0, padx=30, pady=15, sticky=W)
    dayEntry = Entry(update_window, font=('times new roman', 15), width=24)
    dayEntry.grid(row=8, column=1, pady=15, padx=10)

    dateLabel = Label(update_window, text='DATE ADDED: ', font=('times new roman', 20, 'bold'))
    dateLabel.grid(row=9, column=0, padx=30, pady=15, sticky=W)
    dateEntry = Entry(update_window, font=('times new roman', 15), width=24)
    dateEntry.grid(row=9, column=1, pady=15, padx=10)

    update_student_button = ttk.Button(update_window, text='UPDATE', width=20, command=update_data)
    update_student_button.grid(row=10, columnspan=2, pady=15)

    indexing=studentTable.focus()

    content=studentTable.item(indexing)
    listdata=content['values']
    idEntry.insert(0,listdata[0])
    nameEntry.insert(0,listdata[1])
    enrollEntry.insert(0, listdata[2])
    contactEntry.insert(0, listdata[3])
    mailEntry.insert(0, listdata[4])
    addressEntry.insert(0, listdata[5])
    genderEntry.insert(0, listdata[6])
    dobEntry.insert(0, listdata[7])
    dayEntry.insert(0, listdata[8])
    dateEntry.insert(0, listdata[9])


def show_students():
    query = 'select * from student'
    mycursor.execute(query)
    fetched_data = mycursor.fetchall()
    studentTable.delete(*studentTable.get_children())
    for data in fetched_data:
        studentTable.insert('', END, values=data)
def delete_student():
    indexing=studentTable.focus()
    print(indexing)
    content = studentTable.item(indexing)
    content_id = content['values'][0]
    query= 'delete from student where id=%s'
    mycursor.execute(query,content_id)
    con.commit()
    messagebox.showinfo('Deleted!',f'ID {content_id} is deleted Successfully.')
    query='select * from student'
    mycursor.execute(query)
    fetched_data=mycursor.fetchall()
    studentTable.delete(*studentTable.get_children())
    for data in fetched_data:
        studentTable.insert('',END,values=data)
def search_student():
    def search_data():
        query = 'select * from student where id=%s or name=%s or ENROLLMENT_NO=%s or CONTACT_NUMBER=%s or EMAIL=%s or ADDRESS=%s or GENDER=%s or DOB=%s or DAYSCHOLAR_HOSTELER=%s or DATE_ADDED=%s'
        mycursor.execute(query,(idEntry.get(),nameEntry.get(),enrollEntry.get(),contactEntry.get(),mailEntry.get(),addressEntry.get(),genderEntry.get(),dobEntry.get(),dayEntry.get(),dateEntry.get()))
        studentTable.delete(*studentTable.get_children())
        fetched_data=mycursor.fetchall()
        for data in fetched_data:
            studentTable.insert('',END,values=data)

    search_window = Toplevel()
    search_window.grab_set()
    search_window.geometry('800x750+0+0')
    search_window.title('Search Student')
    search_window.resizable(0, 0)
    idLabel = Label(search_window, text='ID: ', font=('times new roman', 20, 'bold'))
    idLabel.grid(row=0, column=0, padx=30, pady=15, sticky=W)
    idEntry = Entry(search_window, font=('times new roman', 15), width=24)
    idEntry.grid(row=0, column=1, pady=15, padx=10)

    nameLabel = Label(search_window, text='NAME: ', font=('times new roman', 20, 'bold'))
    nameLabel.grid(row=1, column=0, padx=30, pady=15, sticky=W)
    nameEntry = Entry(search_window, font=('times new roman', 15), width=24)
    nameEntry.grid(row=1, column=1, pady=15, padx=10)

    enrollLabel = Label(search_window, text='ENROLLMENT NO: ', font=('times new roman', 20, 'bold'))
    enrollLabel.grid(row=2, column=0, padx=30, pady=15, sticky=W)
    enrollEntry = Entry(search_window, font=('times new roman', 15), width=24)
    enrollEntry.grid(row=2, column=1, pady=15, padx=10)

    contactLabel = Label(search_window, text='CONTACT NUMBER: ', font=('times new roman', 20, 'bold'))
    contactLabel.grid(row=3, column=0, padx=30, pady=15, sticky=W)
    contactEntry = Entry(search_window, font=('times new roman', 15), width=24)
    contactEntry.grid(row=3, column=1, pady=15, padx=10)

    mailLabel = Label(search_window, text='E-MAIL: ', font=('times new roman', 20, 'bold'))
    mailLabel.grid(row=4, column=0, padx=30, pady=15, sticky=W)
    mailEntry = Entry(search_window, font=('times new roman', 15), width=24)
    mailEntry.grid(row=4, column=1, pady=15, padx=10)

    addressLabel = Label(search_window, text='ADDRESS: ', font=('times new roman', 20, 'bold'))
    addressLabel.grid(row=5, column=0, padx=30, pady=15, sticky=W)
    addressEntry = Entry(search_window, font=('times new roman', 15), width=24)
    addressEntry.grid(row=5, column=1, pady=15, padx=10)

    genderLabel = Label(search_window, text='GENDER: ', font=('times new roman', 20, 'bold'))
    genderLabel.grid(row=6, column=0, padx=30, pady=15, sticky=W)
    genderEntry = Entry(search_window, font=('times new roman', 15), width=24)
    genderEntry.grid(row=6, column=1, pady=15, padx=10)

    dobLabel = Label(search_window, text='D.O.B: ', font=('times new roman', 20, 'bold'))
    dobLabel.grid(row=7, column=0, padx=30, pady=15, sticky=W)
    dobEntry = Entry(search_window, font=('times new roman', 15), width=24)
    dobEntry.grid(row=7, column=1, pady=15, padx=10)

    dayLabel = Label(search_window, text='DAY-SCHOLAR/HOSTELLER: ', font=('times new roman', 20, 'bold'))
    dayLabel.grid(row=8, column=0, padx=30, pady=15, sticky=W)
    dayEntry = Entry(search_window, font=('times new roman', 15), width=24)
    dayEntry.grid(row=8, column=1, pady=15, padx=10)

    dateLabel = Label(search_window, text='DATE ADDED: ', font=('times new roman', 20, 'bold'))
    dateLabel.grid(row=9, column=0, padx=30, pady=15, sticky=W)
    dateEntry = Entry(search_window, font=('times new roman', 15), width=24)
    dateEntry.grid(row=9, column=1, pady=15, padx=10)

    search_student_button = ttk.Button(search_window, text='SEARCH STUDENT', width=20, command=search_data)
    search_student_button.grid(row=10, columnspan=2, pady=15)


def add_student():
    def add_data():
        if idEntry.get()=='' or nameEntry.get()=='' or enrollEntry.get()=='' or contactEntry.get()=='' or mailEntry.get()=='' or addressEntry.get()=='' or genderEntry.get()=='' or dobEntry.get()=='' or dayEntry.get()==''or dateEntry.get()=='':
            messagebox.showerror('Error!','All fields are required',parent=add_window)
        else:
            try:
                query = 'insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
                mycursor.execute(query, (
                idEntry.get(), nameEntry.get(), enrollEntry.get(), contactEntry.get(), mailEntry.get(),
                addressEntry.get(), genderEntry.get(), dobEntry.get(), dayEntry.get(), dateEntry.get()))
                con.commit()
                result = messagebox.askyesno('Data added successfully', 'Do you want to clean the form?',
                                             parent=add_window)
                if result:
                    idEntry.delete(0, END)
                    nameEntry.delete(0, END)
                    enrollEntry.delete(0, END)
                    contactEntry.delete(0, END)
                    mailEntry.delete(0, END)
                    addressEntry.delete(0, END)
                    genderEntry.delete(0, END)
                    dobEntry.delete(0, END)
                    dayEntry.delete(0, END)
                    dateEntry.delete(0, END)
                else:
                    pass
            except:
                messagebox.showerror('Error','Id cannot be repeated',parent=add_window)
                return

            query='select *from student'
            mycursor.execute(query)
            fetched_data=mycursor.fetchall()
            studentTable.delete(*studentTable.get_children())
            for data in fetched_data:
                studentTable.insert('',END,values=data)

    add_window=Toplevel()
    add_window.grab_set()
    add_window.geometry('800x750+0+0')
    add_window.title('Add Student')
    add_window.resizable(0,0)
    idLabel=Label(add_window,text='ID: ',font=('times new roman',20,'bold'))
    idLabel.grid(row=0,column=0,padx=30,pady=15,sticky=W)
    idEntry=Entry(add_window,font=('times new roman',15),width=24)
    idEntry.grid(row=0,column=1,pady=15,padx=10)

    nameLabel=Label(add_window,text='NAME: ',font=('times new roman',20,'bold'))
    nameLabel.grid(row=1,column=0,padx=30,pady=15,sticky=W)
    nameEntry=Entry(add_window,font=('times new roman',15),width=24)
    nameEntry.grid(row=1,column=1,pady=15,padx=10)

    enrollLabel=Label(add_window,text='ENROLLMENT NO: ',font=('times new roman',20,'bold'))
    enrollLabel.grid(row=2,column=0,padx=30,pady=15,sticky=W)
    enrollEntry=Entry(add_window,font=('times new roman',15),width=24)
    enrollEntry.grid(row=2,column=1,pady=15,padx=10)

    contactLabel=Label(add_window,text='CONTACT NUMBER: ',font=('times new roman',20,'bold'))
    contactLabel.grid(row=3,column=0,padx=30,pady=15,sticky=W)
    contactEntry=Entry(add_window,font=('times new roman',15),width=24)
    contactEntry.grid(row=3,column=1,pady=15,padx=10)

    mailLabel=Label(add_window,text='E-MAIL: ',font=('times new roman',20,'bold'))
    mailLabel.grid(row=4,column=0,padx=30,pady=15,sticky=W)
    mailEntry=Entry(add_window,font=('times new roman',15),width=24)
    mailEntry.grid(row=4,column=1,pady=15,padx=10)

    addressLabel=Label(add_window,text='ADDRESS: ',font=('times new roman',20,'bold'))
    addressLabel.grid(row=5,column=0,padx=30,pady=15,sticky=W)
    addressEntry=Entry(add_window,font=('times new roman',15),width=24)
    addressEntry.grid(row=5,column=1,pady=15,padx=10)

    genderLabel=Label(add_window,text='GENDER: ',font=('times new roman',20,'bold'))
    genderLabel.grid(row=6,column=0,padx=30,pady=15,sticky=W)
    genderEntry=Entry(add_window,font=('times new roman',15),width=24)
    genderEntry.grid(row=6,column=1,pady=15,padx=10)

    dobLabel=Label(add_window,text='D.O.B: ',font=('times new roman',20,'bold'))
    dobLabel.grid(row=7,column=0,padx=30,pady=15,sticky=W)
    dobEntry=Entry(add_window,font=('times new roman',15),width=24)
    dobEntry.grid(row=7,column=1,pady=15,padx=10)

    dayLabel=Label(add_window,text='DAY-SCHOLAR/HOSTELLER: ',font=('times new roman',20,'bold'))
    dayLabel.grid(row=8,column=0,padx=30,pady=15,sticky=W)
    dayEntry=Entry(add_window,font=('times new roman',15),width=24)
    dayEntry.grid(row=8,column=1,pady=15,padx=10)

    dateLabel=Label(add_window,text='DATE ADDED: ',font=('times new roman',20,'bold'))
    dateLabel.grid(row=9,column=0,padx=30,pady=15,sticky=W)
    dateEntry=Entry(add_window,font=('times new roman',15),width=24)
    dateEntry.grid(row=9,column=1,pady=15,padx=10)

    add_student_button=ttk.Button(add_window,text='ADD STUDENT',width=15,command=add_data)
    add_student_button.grid(row=10,columnspan=2,pady=15)
def connect_database():
    def connect():
        global mycursor,con
        try:
            con=pymysql.connect(host=hostEntry.get(),user=userEntry.get(),password=passwordEntry.get())
            mycursor = con.cursor()
        except:
            messagebox.showerror('Error','Invalid Details',parent=connectWindow)
            return
        try:
            query='create database studentmanagementsystem'
            mycursor.execute(query)
            query='use studentmanagementsystem'
            mycursor.execute(query)
            query= 'create table student (ID int not null primary key,NAME varchar(30),ENROLLMENT_NO varchar(11),CONTACT_NUMBER varchar(10),EMAIL varchar(30),ADDRESS varchar(100),GENDER varchar(20),DOB varchar(20),DAYSCHOLAR_HOSTELER varchar(20),DATE_ADDED varchar(20))'
            mycursor.execute(query)
        except:
            query=('use studentmanagementsystem')
            mycursor.execute(query)
        messagebox.showinfo('Success', 'Database Connection Successful', parent=connectWindow)
        connectWindow.destroy()
        addStudent.config(state=NORMAL)
        searchStudent.config(state=NORMAL)
        updateData.config(state=NORMAL)
        exportData.config(state=NORMAL)
        showData.config(state=NORMAL)
        deleteData.config(state=NORMAL)

    connectWindow = Toplevel()
    connectWindow.grab_set()
    connectWindow.geometry('470x250+730+230')
    connectWindow.title('Database Connection')
    connectWindow.resizable(0,0)

    hostnameLabel = Label(connectWindow,text = 'Host Name:',font=('arial',20,'bold'))
    hostnameLabel.grid(row=0,column=0)

    hostEntry = Entry(connectWindow,font=('arial',15),bd=2)
    hostEntry.grid(row=0,column=1,padx=40,pady=20)

    usernameLabel = Label(connectWindow, text='User Name:', font=('arial', 20, 'bold'))
    usernameLabel.grid(row=1, column=0)

    userEntry = Entry(connectWindow, font=('arial', 15), bd=2)
    userEntry.grid(row=1, column=1, padx=40, pady=20)

    passwordLabel = Label(connectWindow, text='Password:', font=('arial', 20, 'bold'))
    passwordLabel.grid(row=2, column=0)

    passwordEntry = Entry(connectWindow, font=('arial', 15), bd=2)
    passwordEntry.grid(row=2, column=1, padx=40, pady=20)

    connectButton = ttk.Button(connectWindow,text='CONNECT',width=15,command=connect)
    connectButton.grid(row=3,columnspan=2)

def clock():
    date = time.strftime('%d-%m-%Y')
    currenttime = time.strftime('%H:%M:%S')
    datetimeLabel.config(text = f'   Date: {date}\nTime: {currenttime}')
    datetimeLabel.after(1000,clock)
#GUI
root = ttkthemes.ThemedTk()
root.get_themes()
root.set_theme('plastik')

background2 = ImageTk.PhotoImage(file='back1.png')

bgLabel2= Label(root,image=background2)
bgLabel2.place(x=0, y=0)

root.geometry('1530x750+0+0')
root.resizable(0,0)
root.title('Student Management System')

datetimeLabel= Label(root,text='H',font= ('times new roman',18,'bold'))
datetimeLabel.place(x=5,y=40)
clock()
s='STUDENT MANAGEMENT SYSTEM'
sliderLabel = Label(root,text=s,font= ('times new roman',28,'bold'))
sliderLabel.place(x=500,y=40)

connectButton = ttk.Button(root,text= 'Database', width=15,command=connect_database)
connectButton.place(x=1400,y=50)

leftFrame = Frame(root)
leftFrame.place(x=70,y=140,width=300,height=550)

logo_image =PhotoImage(file='logo2.png')
logo_Label = Label(leftFrame,image=logo_image)
logo_Label.grid(row=0,column=0)

addStudent = ttk.Button(leftFrame,text='Add Student',width=25,state=DISABLED,command=add_student)
addStudent.grid(row=1,column=0,pady=20)

searchStudent = ttk.Button(leftFrame,text='Search Student',width=25,state=DISABLED,command=search_student)
searchStudent.grid(row=2,column=0,pady=20)

deleteData = ttk.Button(leftFrame,text='Delete Data',width=25,state=DISABLED,command=delete_student)
deleteData.grid(row=5,column=0,pady=20)

updateData = ttk.Button(leftFrame,text='Update Data',width=25,state=DISABLED,command=update_student)
updateData.grid(row=4,column=0,pady=20)

showData = ttk.Button(leftFrame,text='Show Students',width=25,state=DISABLED,command=show_students)
showData.grid(row=3,column=0,pady=20)

exportData = ttk.Button(leftFrame,text='Export Data',width=25,state=DISABLED,command=export_data)
exportData.grid(row=6,column=0,pady=20)

exit = ttk.Button(leftFrame,text='Exit',width=25,command=iexit)
exit.grid(row=7,column=0,pady=20)

rightFrame = Frame(root,bg='lightgray',border=10)
rightFrame.place(x=300,y=140,width=1200,height=550)

scrollBarX = Scrollbar(rightFrame,orient=HORIZONTAL)
scrollBarY = Scrollbar(rightFrame,orient=VERTICAL)

studentTable = ttk.Treeview(rightFrame,column=('ID','NAME','ENROLLMENT NO','CONTACT NUMBER','E-MAIL','ADDRESS','GENDER',
                                'D.O.B','DAY-SCHOLAR/HOSTELER','DATE ADDED'),
                            xscrollcommand=scrollBarX.set,yscrollcommand=scrollBarY.set)
scrollBarX.config(command=studentTable.xview)
scrollBarY.config(command=studentTable.yview)

scrollBarX.pack(side=BOTTOM,fill=X)
scrollBarY.pack(side=RIGHT,fill=Y)

studentTable.pack(fill=BOTH,expand=1)

studentTable.heading('ID',text='ID')
studentTable.heading('NAME',text='NAME')
studentTable.heading('ENROLLMENT NO',text='ENROLLMENT NO')
studentTable.heading('CONTACT NUMBER',text='CONTACT NUMBER')
studentTable.heading('E-MAIL',text='E-MAIL')
studentTable.heading('ADDRESS',text='ADDRESS')
studentTable.heading('GENDER',text='GENDER')
studentTable.heading('D.O.B',text='D.O.B')
studentTable.heading('DAY-SCHOLAR/HOSTELER',text='DAY-SCHOLAR/HOSTELER')
studentTable.heading('DATE ADDED',text='DATE ADDED')

studentTable.column('ID',width=50,anchor=CENTER)
studentTable.column('NAME',width=250,anchor=CENTER)
studentTable.column('ENROLLMENT NO',width=200,anchor=CENTER)
studentTable.column('CONTACT NUMBER',width=200,anchor=CENTER)
studentTable.column('E-MAIL',width=350,anchor=CENTER)
studentTable.column('ADDRESS',width=400,anchor=CENTER)
studentTable.column('GENDER',width=100,anchor=CENTER)
studentTable.column('D.O.B',width=150,anchor=CENTER)
studentTable.column('DAY-SCHOLAR/HOSTELER',width=250,anchor=CENTER)
studentTable.column('DATE ADDED',width=150,anchor=CENTER)

style=ttk.Style()
style.configure('Treeview',rowheight=30,font=('times new roman',15),foreground='navyblue')
style.configure('Treeview.Heading',font=('times new roman',12,'bold'))

studentTable.config(show='headings')

root.mainloop()
