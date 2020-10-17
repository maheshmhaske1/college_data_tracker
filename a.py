from tkinter import *
from tkinter import messagebox
import pymysql

def CAL():
    win = Tk()
    win.geometry('400x500')
    win.maxsize(250,250)
    e1 = Entry(win)
    e1.place(x=100, y=0)
    e2 = Entry(win)
    e2.place(x=100, y=30)

    def add():
        no1 = int(e1.get())
        no2 = int(e2.get())
        add = no1 + no2
        print(add)
        Label(win, text=add,fg='red').place(x=0, y=90)

    def sub():
        no1 = int(e1.get())
        no2 = int(e2.get())
        sub = no1 - no2
        print(sub)
        Label(win, text=sub).place(x=50, y=90)

    def mul():
        no1 = int(e1.get())
        no2 = int(e2.get())
        mul = no1 * no2
        print(mul)
        Label(win, text=mul).place(x=100, y=90)

    def div():
        no1 = int(e1.get())
        no2 = int(e2.get())
        div = no1 / no2
        print(div)
        Label(win, text=div).place(x=150, y=90)

    Label(win, text='enter 1st no :').place(x=0, y=0)
    Label(win, text='enter 2st no :').place(x=0, y=30)

    b1 = Button(win, text="add", command=add).place(x=0, y=60)
    b2 = Button(win, text="sub", command=sub).place(x=50, y=60)
    b3 = Button(win, text="mul", command=mul).place(x=100, y=60)
    b4 = Button(win, text="div", command=div).place(x=150, y=60)

def help():
    lable_help = Label(win, text='=====helping you====      1.for delete login >> enter roll number in LOGiN SECTION >> hit DELETE button and data has been deleted       2.for UPDATE data LOGIN << enter ROLL NUMBER in registration section which is going to update also enter updation for NAME & MOBILE NUMBER  ',fg='red')
    lable_help.place(x=0, y=500)
    l=Label(win,'hit UPDATE button and data has updated successfully',fg='red')
    l.place(x=0, y=510)



def delete():
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='loginout')
    print(conn)
    c = conn.cursor()
    messagebox.askokcancel('ststus',"sure about delete")
    c.execute('delete from ragister where uname="'+e_user.get()+'"')
    conn.commit()
    conn.close()


def show():
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='loginout')
    print(conn)
    c = conn.cursor()
    row1=c.execute( 'select * from ragister')
    print('their are ',+row1,'records found:')
    conn.commit()
    conn.close()


def fpass():
    win = Tk()
    win.geometry('400x500')
    win.maxsize(250, 250)
    Label(win,text='enter your roll no:').place(x=0,y=0)
    eus = Entry(win)
    eus.place(x=100, y=0)
    def wp():
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='loginout')
        c = conn.cursor()
        a = c.execute('select * from ragister where uname="' + eus.get() + '"')
        conn.commit()
        conn.close()
    Button(win,text='view pass',command=wp).place(x=90,y=30)


def fpas():
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='loginout')
    c = conn.cursor()
    a = c.execute('select * from ragister where uname="' + e_user.get() + '"')
    print(a)
    conn.commit()
    conn.close()




def find():
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='loginout')
    print(conn)
    c = conn.cursor()
    a=c.execute('select * from ragister where uname="'+e_user.get()+'"')
    if a==0:
        messagebox.showinfo('ststus', "data NOT found")
    else:
        messagebox.showinfo('ststus', "data found")

    conn.commit()
    conn.close()





def update():
    if e_user.get()==e_uname.get():
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='loginout')
        print(conn)
        c = conn.cursor()
        c.execute('update ragister set name="' + e_name.get() + '",mobile="' + e_mobile.get() + '"  where uname="' + e_uname.get() + '"')
        conn.commit()
        conn.close()
        messagebox.showinfo('success','updated successfully')
    else:
        messagebox.showerror('error','only allowed with your roll number.........')



def logot():
    e_user=''
    e_pass=''
    b21 = Button(win, text="DELETE", bg='orange',state=DISABLED, command=delete).place(x=150, y=300)
    b31 = Button(win, text="SHOW", bg='orange',state=DISABLED, command=show).place(x=200, y=300)
    b41 = Button(win, text="FIND", bg='orange',state=DISABLED, command=find).place(x=250, y=300)
    b51 = Button(win, text="UPDATE", bg='orange',state=DISABLED, command=update).place(x=300, y=300)
    b61 = Button(win, text="HELP", bg='orange',state=DISABLED, command=help).place(x=370, y=300)
    LOGOUT = Button(win, text="LOG OUT", bg='red',state=DISABLED, command=logot).place(x=50, y=60)
    messagebox.showinfo("status","LOGOUT success")


def login():
    password=e_pass.get()
    username=e_user.get()
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='loginout')
    print(conn)
    c = conn.cursor()
    q = 'select uname from ragister where uname="'+username+'" and password="'+password+'"'
    no=c.execute(q)
    if no==1:
        print('login success')
        b2 = Button(win, text="DELETE",  bg='orange',command=delete).place(x=150, y=300)
        b3 = Button(win, text="SHOW",  bg='orange',command=show).place(x=200, y=300)
        b4 = Button(win, text="FIND", bg='orange',command=find).place(x=250, y=300)
        b5 = Button(win, text="UPDATE", bg='orange',command=update).place(x=300, y=300)
        b6 = Button(win, text="HELP", bg='orange',command=help).place(x=370, y=300)
        LOGOUT = Button(win, text="LOG OUT", bg='red', command=logot).place(x=50, y=60)
    elif e_user=='' or e_pass=="":
        messagebox.showerror('user and pass not found','username and password cant null')




    else:
        messagebox.showerror('user not found','USER CANT FOUND')
        print('user not found')
    conn.commit()
    conn.close()






def register():
    try:
        name = str(e_name.get())
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='loginout')
        print(conn)
        c = conn.cursor()
        c.execute(
            'insert into ragister values("' + name + '","' + e_mobile.get() + '","' + e_uname.get() + '","' + e_passwd.get() + '")')
        messagebox.showinfo('ststus', "data register kindly login with roll no and passwd")
        conn.commit()
        conn.close()
    except:
        messagebox.showerror('error','check connection')



win=Tk()





#GUI REGISTER

lable_name= Label(win, text='enter your name : ')
lable_name.place(x=500, y=0)
lable_mob = Label(win, text='enter your mobile : ')
lable_mob.place(x=500, y=30)
lable_user = Label(win, text='enter your roll_no : ')
lable_user.place(x=500, y=60)
lable_passwd = Label(win, text='enter your passwd : ')
lable_passwd.place(x=500, y=90)

e_name = Entry(win)
e_name.place(x=700, y=0)
e_mobile = Entry(win)
e_mobile.place(x=700, y=30)
e_uname = Entry(win)
e_uname.place(x=700, y=60)
e_passwd = Entry(win)
e_passwd.place(x=700, y=90)

register1 = Button(win, text='register', command=register, bg='yellow')
register1.place(x=500, y=120)









#GUI LOGIN

lable_user=Label(win,text='roll_no : ')
lable_user.place(x=0,y=0)
lable_pass=Label(win,text='password : ')
lable_pass.place(x=0,y=30)

e_user=Entry(win)
e_user.place(x=70,y=0)
e_pass=Entry(win)
e_pass.place(x=70,y=30)

login=Button(win,text='login',command=login,bg='green',fg='white')
login.place(x=0,y=60)

fpass = Button(win, text='forgot password', command=fpas, bg='black', fg='white')
fpass.place(x=130, y=60)

login=Button(win,text='CALCULLATOR',command=CAL,bg='orange',fg='green')
login.place(x=900,y=120)



win.title('record managment systen')

win.mainloop()
