#In this part we are creating installation of app with some interfaces

def addstudent():
    def submitadd():
        id = idval.get()
        name = nameval.get() 
        mobile = mobileval.get()
        email = emailval.get() 
        address = addressval.get() 
        gender = Genderval.get() 
        dob = DOBval.get() 
        addedtime = time.strftime("%H:%M:%S")
        addeddate = time.strftime("%d/%m/%Y")
        try:
            strr = 'insert into bitstudentmanagementsystem3 values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            mycursor.execute(strr,(id,name,mobile,email,address,gender,dob,addedtime,addeddate))
            connect.commit()
            result = messagebox.askyesnocancel('Notification','Id {} Name {} Added Successfully... and want to clean the form'.format(id,name),parent = addroot)
            if(result==True):
                idval.set('')
                nameval.set('')
                mobileval.set('')
                emailval.set('')
                addressval.set('')
                Genderval.set('')
                DOBval.set('')

        except:
            messagebox.showerror('Notifications','Id already exists try another Id....',parent = addroot)
        strr = 'select * from bitstudentmanagementsystem3'
        mycursor.execute(strr)
        datas = mycursor.fetchall()

        studenttable.delete(*studenttable.get_children())
        for i in datas:                                     # To store data in showdata frame
            vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
            studenttable.insert('', END, values = vv)


    addroot = Toplevel(master = DataEntryFrame)
    addroot.grab_set()
    addroot.geometry('470x470+220+220')
    addroot.title(' BIT Student Management System')
    addroot.config(bg='#FFFFFF') 
    addroot.iconphoto(True, PhotoImage(file = "Bit.png"))
    addroot.resizable(False,False)

    #---------------------------------------------------- Add Student labels

    idlabel = Label(addroot, text = 'Enter ID : ', bg = '#BBDEFB', font = ('custom_font',18,'bold'),fg='#1E88E5', borderwidth=3, width = 12, anchor='w')
    idlabel.place(x=10, y=10)

    
    namelabel = Label(addroot, text = 'Enter Name : ', bg = '#BBDEFB', font = ('custom_font',18,'bold'), fg='#1E88E5', borderwidth=3, width = 12, anchor='w')
    namelabel.place(x=10, y=70)

    
    mobilelabel = Label(addroot, text = 'Enter Mobile : ', bg = '#BBDEFB', font = ('custom_font',18,'bold'), fg='#1E88E5', borderwidth=3, width = 12, anchor='w')
    mobilelabel.place(x=10, y=130)

    
    Emaillabel = Label(addroot, text = 'Enter Email : ', bg = '#BBDEFB', font = ('custom_font',18,'bold'), fg='#1E88E5', borderwidth=3, width = 12, anchor='w')
    Emaillabel.place(x=10, y=190)

    
    addresslabel = Label(addroot, text = 'Enter Address : ', bg = '#BBDEFB', font = ('custom_font',18,'bold'), fg='#1E88E5', borderwidth=3, width = 12, anchor='w')
    addresslabel.place(x=10, y=250)

    
    Genderlabel = Label(addroot, text = 'Enter Gender : ', bg = '#BBDEFB', font = ('custom_font',18,'bold'), fg='#1E88E5', borderwidth=3, width = 12, anchor='w')
    Genderlabel.place(x=10, y=310)

    
    DOBlabel = Label(addroot, text = 'Enter D.O.B : ', bg = '#BBDEFB', font = ('custom_font',18,'bold'), fg='#1E88E5', borderwidth=3, width = 12, anchor='w')
    DOBlabel.place(x=10, y=370)

    #--------------------------------------------------------- Add Student Entry
    
    idval = StringVar()
    nameval = StringVar()
    mobileval = StringVar()
    emailval = StringVar()
    addressval = StringVar()
    Genderval = StringVar()
    DOBval = StringVar()

    identry = Entry(addroot,font=('roman',15,'bold'),bd=5, textvariable=idval)
    identry.place(x=250, y=10)

    nameentry = Entry(addroot,font=('roman',15,'bold'),bd=5, textvariable=nameval)
    nameentry.place(x=250, y=70)
                    
    mobileentry = Entry(addroot,font=('roman',15,'bold'),bd=5, textvariable=mobileval)
    mobileentry.place(x=250, y=130)

    emailentry = Entry(addroot,font=('roman',15,'bold'),bd=5, textvariable=emailval)
    emailentry.place(x=250, y=190)

    addressentry = Entry(addroot,font=('roman',15,'bold'),bd=5, textvariable=addressval)
    addressentry.place(x=250, y=250)

    Genderentry = Entry(addroot,font=('roman',15,'bold'),bd=5, textvariable=Genderval)
    Genderentry.place(x=250, y=310)

    DOBentry = Entry(addroot,font=('roman',15,'bold'),bd=5, textvariable=DOBval)
    DOBentry.place(x=250, y=370)

    #--------------------------------------------------------- Add button

    submitbutton = Button(addroot,text='Submit',font = ('roman',15, 'bold'), width = 20, bd = 5, activebackground='#BBDEFB', activeforeground='white', bg = '#1E88E5',
                          command=submitadd)
    submitbutton.place(x=150, y=420)

    addroot.mainloop()


def searchstudent():
    def search():
        id = idval.get()
        name = nameval.get() 
        mobile = mobileval.get()
        email = emailval.get() 
        address = addressval.get() 
        gender = Genderval.get() 
        dob = DOBval.get() 
        addeddate = time.strftime("%d/%m/%Y")
        if(id != ''):   # To search the id 
            strr = 'select * from bitstudentmanagementsystem3 where id = %s'
            mycursor.execute(strr,(id))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:                                   
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenttable.insert('', END, values = vv)
        elif(name != ''):   # To search the id 
            strr = 'select * from bitstudentmanagementsystem3 where name = %s'
            mycursor.execute(strr,(name))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:                                   
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenttable.insert('', END, values = vv)
        elif(mobile != ''):   # To search the id 
            strr = 'select * from bitstudentmanagementsystem3 where mobile = %s'
            mycursor.execute(strr,(mobile))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:                                   
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenttable.insert('', END, values = vv)
        elif(email != ''):   # To search the id 
            strr = 'select * from bitstudentmanagementsystem3 where email = %s'
            mycursor.execute(strr,(email))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:                                   
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenttable.insert('', END, values = vv)
        elif(address != ''):   # To search the id 
            strr = 'select * from bitstudentmanagementsystem3 where address = %s'
            mycursor.execute(strr,(address))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:                                   
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenttable.insert('', END, values = vv)
        elif(gender != ''):   # To search the id 
            strr = 'select * from bitstudentmanagementsystem3 where gender = %s'
            mycursor.execute(strr,(gender))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:                                   
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenttable.insert('', END, values = vv)
        elif(dob != ''):   # To search the id 
            strr = 'select * from bitstudentmanagementsystem3 where dob = %s'
            mycursor.execute(strr,(dob))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:                                   
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenttable.insert('', END, values = vv)
        elif(addeddate != ''):   # To search the id 
            strr = 'select * from bitstudentmanagementsystem3 where addeddate = %s'
            mycursor.execute(strr,(addeddate))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:                                   
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenttable.insert('', END, values = vv)



    searchroot = Toplevel(master = DataEntryFrame)
    searchroot.grab_set()
    searchroot.geometry('470x540+220+220')
    searchroot.title('BIT Student Management System')
    searchroot.config(bg='#FFFFFF') 
    searchroot.iconphoto(True, PhotoImage(file = "Bit.png"))
    searchroot.resizable(False,False)

    #---------------------------------------------------- Add Student labels

    idlabel = Label(searchroot, text = 'Enter ID : ', bg = '#BBDEFB', font = ('custom_font',18,'bold'),fg = '#1E88E5' , borderwidth=3, width = 12, anchor='w')
    idlabel.place(x=10, y=10)

    
    namelabel = Label(searchroot, text = 'Enter Name : ', bg = '#BBDEFB', font = ('custom_font',18,'bold'),fg= '#1E88E5', borderwidth=3, width = 12, anchor='w')
    namelabel.place(x=10, y=70)

    
    mobilelabel = Label(searchroot, text = 'Enter Mobile : ', bg = '#BBDEFB', font = ('custom_font',18,'bold'),fg= '#1E88E5', borderwidth=3, width = 12, anchor='w')
    mobilelabel.place(x=10, y=130)

    
    Emaillabel = Label(searchroot, text = 'Enter Email : ', bg = '#BBDEFB', font = ('custom_font',18,'bold'),fg= '#1E88E5', borderwidth=3, width = 12, anchor='w')
    Emaillabel.place(x=10, y=190)

    
    addresslabel = Label(searchroot, text = 'Enter Address : ', bg = '#BBDEFB', font = ('custom_font',18,'bold'),fg= '#1E88E5', borderwidth=3, width = 12, anchor='w')
    addresslabel.place(x=10, y=250)

    
    Genderlabel = Label(searchroot, text = 'Enter Gender : ', bg = '#BBDEFB', font = ('custom_font',18,'bold'),fg= '#1E88E5', borderwidth=3, width = 12, anchor='w')
    Genderlabel.place(x=10, y=310)

    DOBlabel = Label(searchroot, text = 'Enter D.O.B : ', bg = '#BBDEFB', font = ('custom_font',18,'bold'),fg= '#1E88E5', borderwidth=3, width = 12, anchor='w')
    DOBlabel.place(x=10, y=370)

    Datelabel = Label(searchroot, text = 'Enter Date : ', bg = '#BBDEFB', font = ('custom_font',18,'bold'),fg= '#1E88E5', borderwidth=3, width = 12, anchor='w')
    Datelabel.place(x=10, y=430)


    #--------------------------------------------------------- Add Student Entry
    
    idval = StringVar()
    nameval = StringVar()
    mobileval = StringVar()
    emailval = StringVar()
    addressval = StringVar()
    Genderval = StringVar()
    DOBval = StringVar()
    dateval = StringVar()

    identry = Entry(searchroot,font=('roman',15,'bold'),bd=5, textvariable=idval)
    identry.place(x=250, y=10)

    nameentry = Entry(searchroot,font=('roman',15,'bold'),bd=5, textvariable=nameval)
    nameentry.place(x=250, y=70)
                    
    mobileentry = Entry(searchroot,font=('roman',15,'bold'),bd=5, textvariable=mobileval)
    mobileentry.place(x=250, y=130)

    emailentry = Entry(searchroot,font=('roman',15,'bold'),bd=5, textvariable=emailval)
    emailentry.place(x=250, y=190)

    addressentry = Entry(searchroot,font=('roman',15,'bold'),bd=5, textvariable=addressval)
    addressentry.place(x=250, y=250)

    Genderentry = Entry(searchroot,font=('roman',15,'bold'),bd=5, textvariable=Genderval)
    Genderentry.place(x=250, y=310)

    DOBentry = Entry(searchroot,font=('roman',15,'bold'),bd=5, textvariable=DOBval)
    DOBentry.place(x=250, y=370)

    Dateentry = Entry(searchroot,font=('roman',15,'bold'),bd=5, textvariable=dateval)
    Dateentry.place(x=250, y=430)


    #--------------------------------------------------------- Add button

    submitbutton = Button(searchroot,text='Submit',font = ('bold_font',15, 'bold'), width = 20, bd = 5, activebackground='#BBDEFB', activeforeground='white', bg = '#1E88E5',
                          command=search)
    submitbutton.place(x=150, y=480)

    searchroot.mainloop()
    


def deletestudent():
    cc = studenttable.focus()
    content = studenttable.item(cc)
    pp = content['values'][0]
    strr = 'delete from bitstudentmanagementsystem3 where id = %s'
    mycursor.execute(strr,(pp))
    connect.commit()
    messagebox.showinfo('Notifications','Id {} deleted successfully...'.format(pp))

    strr = 'select * from bitstudentmanagementsystem3 '
    mycursor.execute(strr)
    datas = mycursor.fetchall()
    studenttable.delete(*studenttable.get_children())
    for i in datas:                                   
        vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
        studenttable.insert('', END, values = vv)




   

def updatestudent():
    def update():
        id = idval.get()
        name = nameval.get() 
        mobile = mobileval.get()
        email = emailval.get() 
        address = addressval.get() 
        gender = Genderval.get() 
        dob = DOBval.get() 
        date = dateval.get()
        time = timeval.get()

        strr = 'update bitstudentmanagementsystem3 set name = %s,mobile= %s, email = %s, address= %s,gender = %s, dob= %s, date = %s, time = %s where id = %s'
        mycursor.execute(strr,(name , mobile, email, address, gender, dob, date, time, id))
        connect.commit()
        messagebox.showinfo('Notifications','Id {} Modified successfully...'.format(id),parent = updateroot)
        strr = 'select * from bitstudentmanagementsystem3 '
        mycursor.execute(strr)
        datas = mycursor.fetchall()
        studenttable.delete(*studenttable.get_children())
        for i in datas:                                   
            vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
            studenttable.insert('', END, values = vv)



    updateroot = Toplevel(master = DataEntryFrame)
    updateroot.grab_set()
    updateroot.geometry('470x585+220+160')
    updateroot.title('BIT Student Management System')
    updateroot.config(bg='#FFFFFF') 
    updateroot.iconphoto(True, PhotoImage(file = "Bit.png"))
    updateroot.resizable(False,False)

    #---------------------------------------------------- Add Student labels

    idlabel = Label(updateroot, text = 'Enter ID : ', bg = "#BBDEFB", font = ('custom_font',18,'bold'),fg='#1E88E5', borderwidth=3, width = 12, anchor='w')
    idlabel.place(x=10, y=10)

    
    namelabel = Label(updateroot, text = 'Enter Name : ', bg = '#BBDEFB', font = ('custom_font',18,'bold'),fg = '#1E88E5', borderwidth=3, width = 12, anchor='w')
    namelabel.place(x=10, y=70)

    
    mobilelabel = Label(updateroot, text = 'Enter Mobile : ', bg = '#BBDEFB', font = ('custom_font',18,'bold'),fg = '#1E88E5', borderwidth=3, width = 12, anchor='w')
    mobilelabel.place(x=10, y=130)

    
    Emaillabel = Label(updateroot, text = 'Enter Email : ', bg = '#BBDEFB', font = ('custom_font',18,'bold'),fg = '#1E88E5', borderwidth=3, width = 12, anchor='w')
    Emaillabel.place(x=10, y=190)

    
    addresslabel = Label(updateroot, text = 'Enter Address : ', bg = '#BBDEFB', font = ('custom_font',18,'bold'),fg = '#1E88E5', borderwidth=3, width = 12, anchor='w')
    addresslabel.place(x=10, y=250)

    
    Genderlabel = Label(updateroot, text = 'Enter Gender : ', bg = '#BBDEFB', font = ('custom_font',18,'bold'),fg = '#1E88E5', borderwidth=3, width = 12, anchor='w')
    Genderlabel.place(x=10, y=310)

    DOBlabel = Label(updateroot, text = 'Enter D.O.B : ', bg = '#BBDEFB', font = ('custom_font',18,'bold'),fg = '#1E88E5', borderwidth=3, width = 12, anchor='w')
    DOBlabel.place(x=10, y=370)

    Datelabel = Label(updateroot, text = 'Enter Date : ', bg = '#BBDEFB', font = ('custom_font',18,'bold'),fg = '#1E88E5', borderwidth=3, width = 12, anchor='w')
    Datelabel.place(x=10, y=430)

    Timelabel = Label(updateroot, text = 'Enter Time : ', bg = '#BBDEFB', font = ('custom_font',18,'bold'),fg = '#1E88E5', borderwidth=3, width = 12, anchor='w')
    Timelabel.place(x=10, y=490)



    #--------------------------------------------------------- Add Student Entry
    
    idval = StringVar()
    nameval = StringVar()
    mobileval = StringVar()
    emailval = StringVar()
    addressval = StringVar()
    Genderval = StringVar()
    DOBval = StringVar()
    dateval = StringVar()
    timeval = StringVar()

    identry = Entry(updateroot,font=('roman',15,'bold'),bd=5, textvariable=idval)
    identry.place(x=250, y=10)

    nameentry = Entry(updateroot,font=('roman',15,'bold'),bd=5, textvariable=nameval)
    nameentry.place(x=250, y=70)
                    
    mobileentry = Entry(updateroot,font=('roman',15,'bold'),bd=5, textvariable=mobileval)
    mobileentry.place(x=250, y=130)

    emailentry = Entry(updateroot,font=('roman',15,'bold'),bd=5, textvariable=emailval)
    emailentry.place(x=250, y=190)

    addressentry = Entry(updateroot,font=('roman',15,'bold'),bd=5, textvariable=addressval)
    addressentry.place(x=250, y=250)

    Genderentry = Entry(updateroot,font=('roman',15,'bold'),bd=5, textvariable=Genderval)
    Genderentry.place(x=250, y=310)

    DOBentry = Entry(updateroot,font=('roman',15,'bold'),bd=5, textvariable=DOBval)
    DOBentry.place(x=250, y=370)

    Dateentry = Entry(updateroot,font=('roman',15,'bold'),bd=5, textvariable=dateval)
    Dateentry.place(x=250, y=430)

    Timeentry = Entry(updateroot,font=('roman',15,'bold'),bd=5, textvariable=timeval)
    Timeentry.place(x=250, y=490)



    #--------------------------------------------------------- Add button

    submitbutton = Button(updateroot,text='Submit',font = ('custom_font',15, 'bold'), width = 20, bd = 5, activebackground='#BBDEFB', activeforeground='white', bg = '#1E88E5',
                          command=update)
    submitbutton.place(x=150, y=540)

    cc = studenttable.focus()
    content = studenttable.item(cc)
    pp = content['values']
    if(len(pp) != 0):
        idval.set(pp[0])
        nameval.set(pp[1]) 
        mobileval.set(pp[2])
        emailval.set(pp[3])
        addressval.set(pp[4])
        Genderval.set(pp[5])
        DOBval.set(pp[6])
        dateval.set(pp[7]) 
        timeval.set(pp[8])

    updateroot.mainloop()

def showallstudent():
    strr = 'select * from bitstudentmanagementsystem3 '
    mycursor.execute(strr)
    datas = mycursor.fetchall()
    studenttable.delete(*studenttable.get_children())
    for i in datas:                                   
        vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
        studenttable.insert('', END, values = vv)


def Exportstudent():
    ff = filedialog.asksaveasfilename()
    gg = studenttable.get_children()
    id,name,mobile,email,address,gender,dob,addeddate,addedtime = [],[],[],[],[],[],[],[],[]
    for i in gg:
        content = studenttable.item(i)
        pp = content['values']
        id.append(pp[0]),name.append(pp[1]), mobile.append(pp[2]), email.append(pp[3]), address.append(pp[4]),
        gender.append(pp[5]),dob.append(pp[6]),addeddate.append(pp[7]),addedtime.append(pp[8])
    dd = ['Id', 'Name', 'Mobile', 'Email', 'Address', 'Gender', 'dob', 'Added Date', 'Added Time']
    df = pandas.DataFrame(list(zip(id,name,mobile,email,address,gender,dob,addeddate,addedtime)),columns=dd)
    paths = r'{}.csv'.format(ff)
    df.to_csv(paths,index = False)

    messagebox.showinfo('Notifications','Student data is saved {}'.format(paths))
        

def exitstudent():
    result = messagebox.askyesnocancel('Notification', 'Do you want to exit?')
    if(result == True):
        root.destroy()
          
          
######################################### ################################ Connection of database to mysql 

def Connectdb():
    def submitdb():
        global connect,mycursor
        host = "localhost"
        user = "root"
        password = "sona17@8#02NAN"
        # host = hostval.get()
        # user = userval.get()
        # password = passwordval.get()
        
        try: 
            connect = pymysql.connect(host=host,user=user,password=password)
            mycursor= connect.cursor()
        except:
            messagebox.showerror('Notifications','Data is inncorrect please try again',parent=dbroot)
            return
        try:
            strr = 'create database bitstudentmanagementsystem0'
            mycursor.execute(strr)
            strr = 'use bitstudentmanagementsystem0' 
            mycursor.execute(strr)
            strr= 'create table bitstudentmanagementsystem3(Id int(11),Name varchar(20),mobile varchar(12),email varchar(30),address varchar(100),gender varchar(100),dob varchar(50),date varchar(50),time varchar(50))'  
            mycursor.execute(strr) 

            strr = 'alter table bitstudentmanagementsystem3 modify column id int not null'
            mycursor.execute(strr)
            strr = 'alter table bitstudentmanagementsystem3 modify column id int primary key'
            mycursor.execute (strr)
            
            
            messagebox.showinfo('Notification','Database created and now you are connected to the databases .....',parent=dbroot)

        except:
            strr = 'use bitstudentmanagementsystem0'
            mycursor.execute(strr)

           
            messagebox.showinfo('Notification','Now you are connected to the databases .....',parent=dbroot)
        dbroot.destroy()

    dbroot = Toplevel()
    dbroot.grab_set()
    dbroot.geometry('470x250+800+230')
    dbroot.iconphoto(True, PhotoImage(file = "Bit.png"))
    dbroot.resizable(False,False)
    dbroot.config(bg='#FFFFFF')
    #-----------------------------------------Connect dblabels
    hostlabel = Label(dbroot,text="Enter Host : ",bg='#BBDEFB',font=('custom_font',18,'bold'),fg='#1E88E5',borderwidth=3,width=13,anchor='w')
    hostlabel.place(x=10,y=10)

    userlabel = Label(dbroot,text="Enter User : ",bg='#BBDEFB',font=('custom_font',18,'bold'),fg='#1E88E5',borderwidth=3,width=13,anchor='w')
    userlabel.place(x=10,y=70)

    passwordlabel = Label(dbroot,text="Enter Password : ",bg='#BBDEFB',font=('custom_font',18,'bold'),fg='#1E88E5',borderwidth=3,width=13,anchor='w')
    passwordlabel.place(x=10,y=130)

    #-------------------------------------------Connectdb Entry

    hostval = StringVar()
    userval = StringVar()
    passwordval = StringVar()
    
    hostentry = Entry(dbroot,font=('custom_font',15,'bold'),bd=5,textvariable=hostval)
    hostentry.place(x=250,y=10)

    userentry = Entry(dbroot,font=('custom_font',15,'bold'),bd=5,textvariable=userval)
    userentry.place(x=250,y=70)

    passwordentry = Entry(dbroot,font=('custom_font',15,'bold'),bd=5,textvariable=passwordval)
    passwordentry.place(x=250,y=130)

    #------------------------------------Connectdb button
    submitbutton = Button(dbroot,text='Submit',font=('bold_font',15,'bold'),bg='#1E88E5',fg='white',bd=5,width=20,activebackground='#BBDEFB',activeforeground='white',
                          command=submitdb)
    submitbutton.place(x=150,y=190)

    dbroot.mainloop()

#######################################################################

def tick():
    time_string = time.strftime("%H:%M:%S")
    date_string = time.strftime("%d/%m/%Y")
    clock.config(text='Date :'+date_string+"\n"+"Time :"+time_string)
    clock.after(200,tick)

#########################################################################Intro slider

import random
colors= ['red', 'green', 'blue', 'yellow', 'pink', 'red2','gold2']

def IntroLabelColorTick():
    fg=random.choice(colors)
    print(fg)
    #SliderLabel.config(fg=fg)     {it gives different colors at every microseconds}
    #SliderLabel.after(2,IntroLabelColorTick)    {not needed in our project :: disco wala}

def IntroLabelTick():
    global count,text
    if(count>=len(ss)):
        count= 0
        text= ''
        SliderLabel.config(text=text)
    else:
        text=text+ss[count]
        SliderLabel.config(text=text)
        count+=1
    SliderLabel.after(200,IntroLabelTick)

##############################################################################
import tkinter as tk
from tkinter import *
from tkinter import Toplevel, messagebox, filedialog
from tkinter.ttk import Treeview
from tkinter import ttk
import pandas
import pymysql
from tkinter import PhotoImage
import time 
root = Tk()
root.title('BIT Student Management System')
root.config(bg='#E3F2FD')
root.geometry('1174x700+200+50')
root.iconphoto(True, PhotoImage(file = "Bit.png"))
root.resizable(False,False)

##########################################################Frames
##---------------------------------------------------------dataentry frame 

DataEntryFrame = Frame(root,bg='#FFFFFF',borderwidth=5)
DataEntryFrame.place(x=20,y=100,width=300,height=560)

frontlabel = Label(DataEntryFrame, text = ' Menu ', font = ('bold_font',20,' bold'),bg = '#FFFFFF', fg = '#1E88E5')
frontlabel.pack(side = TOP, expand = True)

addbutton = Button(DataEntryFrame, text = '1. Add Student ',width= 20 ,relief= 'flat', font=('custom_font', 15),bd = 6,bg = '#BBDEFB',fg = '#1E88E5', activebackground='white',
                    activeforeground='white', command = addstudent)
addbutton.pack(side = TOP, expand = True)

searchbutton = Button(DataEntryFrame, text = '2. Search Student ', width = 20 , font=('custom_font', 15), bd =6,bg = '#BBDEFB',fg='#1E88E5', activebackground='white',
                   relief='flat', activeforeground='white', command = searchstudent)
searchbutton.pack(side = TOP, expand = True)

deletebutton = Button(DataEntryFrame, text = '3. Delete Student ', width = 20 , font=('custom_font', 15), bd =6,bg = '#BBDEFB',fg='#1E88E5', activebackground='white',
                   relief='flat', activeforeground='white', command = deletestudent)
deletebutton.pack(side = TOP, expand = True)

updatebutton = Button(DataEntryFrame, text = '4. Update Student ', width = 20 , font=('custom_font', 15), bd =6,bg = '#BBDEFB',fg='#1E88E5', activebackground='white',
                   relief='flat', activeforeground='white', command = updatestudent)
updatebutton.pack(side = TOP, expand = True)

showallbutton = Button(DataEntryFrame, text = '5. Show all  ', width = 20 , font=('custom_font', 15), bd =6,bg = '#BBDEFB',fg='#1E88E5', activebackground='white',
                   relief=R'flat', activeforeground='white', command = showallstudent)
showallbutton.pack(side = TOP, expand = True)

Exportbutton = Button(DataEntryFrame, text = '6. Export Data ', width = 20 , font=('custom_font', 15), bd =6,bg = '#BBDEFB',fg='#1E88E5', activebackground='white',
                   relief='flat', activeforeground='white', command = Exportstudent)
Exportbutton.pack(side = TOP, expand = True)

Exitbutton = Button(DataEntryFrame, text = '7. Exit ', width = 20 , font=('custom_font', 15), bd =6,bg = '#BBDEFB',fg='#1E88E5', activebackground='white',
                   relief='flat', activeforeground='white', command = exitstudent)
Exitbutton.pack(side = TOP, expand = True)


#------------------------------------------------------------Showdata frame

ShowDataFrame = Frame(root,bg='#FFFFFF',relief='flat',bd= 2)
ShowDataFrame.place(x=350,y=100,width=810,height=570)

#-------------------------------------------------------------Showdata frame

style = ttk.Style()
style.configure('Treeview.Heading',font=('bold_font',14,'bold'),foreground='white',bg='#1E88E5')
style.configure('Treeview',font=('bold_font',15,'bold'),foreground='white',background='#1E88E5')


scroll_x = Scrollbar(ShowDataFrame,orient=HORIZONTAL)
scroll_y = Scrollbar(ShowDataFrame,orient=VERTICAL)

#----------------------------------table in mysql

studenttable = Treeview(ShowDataFrame,columns= ('ID','Name','Mobile No.','E-mail','Address','Gender','D.O.B','Added Date','Added Time'),
                        yscrollcommand=scroll_y.set,xscrollcommand=scroll_x.set)

columns= ('ID','Name','Mobile No.','E-mail','Address','Gender','D.O.B','Added Date','Added Time')
studenttable = ttk.Treeview(ShowDataFrame, columns=columns, show='headings')

style = ttk.Style()
style.theme_use("default")
style.configure("Treeview.Heading", font='bold_font', background="#1E88E5", foreground="white", padding=5)
style.configure("Treeview", font='custom_font', background="#FFFFFF", fieldbackground="#FFFFFF", rowheight=30)
style.map("Treeview", background=[('selected', '#1E88E5')], foreground=[('selected', 'white')])


scroll_x.pack(side=BOTTOM,fill=X)
scroll_y.pack(side=RIGHT,fill=Y)

scroll_x.config(command=studenttable.xview)
scroll_y.config(command=studenttable.yview)

#--------------Headings of Database Table(Left Side of scroll bar)-------------------------#

studenttable.heading('ID',text='ID')     
studenttable.heading('Name',text='Name')
studenttable.heading('Mobile No.',text='Mobile No.')
studenttable.heading('E-mail',text='E-mail')
studenttable.heading('Address',text='Address')
studenttable.heading('Gender',text='Gender')
studenttable.heading('D.O.B',text='D.O.B')
studenttable.heading('Added Date',text='Added Date')
studenttable.heading('Added Time',text='Added Time')
studenttable['show']='headings'     #removes the extra(first) space of headings

studenttable.column('ID',width=100)
studenttable.column('Name',width=200)
studenttable.column('Mobile No.',width=200)
studenttable.column('E-mail',width=300)
studenttable.column('Address',width=200)
studenttable.column('Gender',width=100)
studenttable.column('D.O.B',width=150)
studenttable.column('Added Date',width=150)
studenttable.column('Added Time',width=150)

studenttable.pack(fill=BOTH,expand=1)

########################################################## Header frame----------
header_frame = tk.Frame(root, bg="#1E88E5", height=80)  # Vibrant blue header
header_frame.pack(fill='x')

############################################################Slider

ss = 'Welcome to BIT Student Management System'
count = 0
text = ''
#################################################################Calling functions

SliderLabel = Label(header_frame,text=ss,font=('bold_font',20,'bold'),bg='#1E88E5',fg='white')
SliderLabel.pack(pady=20)

IntroLabelColorTick()

################################################################ clock

clock = Label(root,font=('times', 14),bg='#1E88E5', fg='white')
clock.place(x=20,y=20)
tick()

################################################################# connect database button

connectbutton = Button(header_frame, text= 'Connect To Database',font=('bold_font',10),bg='#1E88E5',fg='white',
                       activebackground='white',activeforeground='white',command=Connectdb)
connectbutton.place(x=1030,y=30)


root.mainloop()
