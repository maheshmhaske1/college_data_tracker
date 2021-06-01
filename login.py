from tkinter import *
from tkinter import messagebox
import pymysql
import random
from twilio.rest import Client



def CAL():
    win3 = Tk()
    win3.geometry('800x900')
    win3.maxsize(550, 550)

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
    if e_user.get() == e_uname.get() or e_user.get()=='3332':
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='loginout')
        print(conn)
        c = conn.cursor()
        c.execute('delete from ragister where username="' + e_uname.get() + '"')
        messagebox.showinfo('success', 'Deleted successfully')

        b21 = Button(win, text="DELETE", bg='orange', state=DISABLED, command=delete).place(x=150, y=450)
        b31 = Button(win, text="SHOW", bg='orange', state=DISABLED, command=show).place(x=200, y=450)
        b41 = Button(win, text="FIND", bg='orange', state=DISABLED, command=find).place(x=250, y=450)
        b51 = Button(win, text="UPDATE", bg='orange', state=DISABLED, command=update).place(x=295, y=450)
        b61 = Button(win, text="HELP", bg='orange', state=DISABLED, command=help).place(x=360, y=450)
        LOGOUT = Button(win, text="LOG OUT", bg='red', state=DISABLED, command=logot).place(x=50, y=60)
        messagebox.showinfo("status", "Forced  LOGOUT User not found")
        conn.commit()
        conn.close()
    else:
        messagebox.showerror('error')

def show():
    if e_user.get()=='3332':
        win1 = Tk()
        win1.geometry('800x900')
        win1.maxsize(550, 550)
        win1.title('RECORDS')
        lable_user = Label(win1, text='NAME : ')
        lable_user.place(x=0, y=0)
        lable_MOB = Label(win1, text='MOBILE : ')
        lable_MOB.place(x=100, y=0)
        lable_ID = Label(win1, text='ID : ')
        lable_ID.place(x=200, y=0)
        lable_PASS = Label(win1, text='PASSWORD : ')
        lable_PASS.place(x=300, y=0)
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='loginout')
        print(conn)
        c = conn.cursor()
        row1=c.execute( 'select * from ragister')
        r=c.fetchall()

        for i in r:
            name=Label(win1,Text=i[0]).place(x=0, y=20)
    

        print('their are ',+row1,'records found:')
        conn.commit()
        conn.close()
    else:
        messagebox.showerror('error','admin pnly')


def fpass():
    win = Tk()
    win.geometry('400x500')
    win.maxsize(250, 250)
    Label(win,text='enter your ID no:').place(x=0,y=0)
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
    if e_user.get()=='3332':
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='loginout')
        print(conn)
        c = conn.cursor()
        a=c.execute('select * from ragister where username="'+e_uname.get()+'"')
        if a==0:
            messagebox.showinfo('ststus', "data NOT found")
        else:
            messagebox.showinfo('ststus', "data found")

        conn.commit()
        conn.close()
    else:
        messagebox.showerror('error','admin only')





def update():
    if e_user.get()==e_uname.get() or e_user.get()=='3332':
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='loginout')
        print(conn)
        c = conn.cursor()
        c.execute('update ragister set name="' + e_name.get() + '",mobile="' + e_mobile.get() + '"  where username="' + e_uname.get() + '"')
        conn.commit()
        conn.close()
        messagebox.showinfo('success','updated successfully')
    else:
        messagebox.showerror('error','only allowed with your ID number.........')



def logot():
    e_user=''
    e_pass=''
    b21 = Button(win, text="DELETE", bg='orange',state=DISABLED, command=delete).place(x=150, y=450)
    b31 = Button(win, text="SHOW", bg='orange',state=DISABLED, command=show).place(x=200, y=450)
    b41 = Button(win, text="FIND", bg='orange',state=DISABLED, command=find).place(x=250, y=450)
    b51 = Button(win, text="UPDATE", bg='orange',state=DISABLED, command=update).place(x=295, y=450)
    b61 = Button(win, text="HELP", bg='orange',state=DISABLED, command=help).place(x=360, y=450)

    messagebox.showinfo("status","LOGOUT success")


def sendmsg():
    if e_user.get()=='3332':
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='loginout')
        print(conn)
        c = conn.cursor()
        c.execute(
            'update ragister set message="' + e_message.get() + '"  where username="' + e_idmsg.get() + '"')

        conn.commit()
        conn.close()
        s=str(e_message.get())
        messagebox.showinfo('success', 'Message sent to ID: '+e_idmsg.get()+'  successfully')
    else:
        b21 = Button(win, text="DELETE", bg='orange', state=DISABLED, command=delete).place(x=150, y=450)
        b31 = Button(win, text="SHOW", bg='orange', state=DISABLED, command=show).place(x=200, y=450)
        b41 = Button(win, text="FIND", bg='orange', state=DISABLED, command=find).place(x=250, y=450)
        b51 = Button(win, text="UPDATE", bg='orange', state=DISABLED, command=update).place(x=295, y=450)
        b61 = Button(win, text="HELP", bg='orange', state=DISABLED, command=help).place(x=360, y=450)
        messagebox.showerror('unautharized','ADMIN ONLY')


def login():
    password=e_pass.get()
    username=e_user.get()
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='loginout')
    print(conn)
    c = conn.cursor()
    q = 'select username from ragister where username="'+username+'" and password="'+password+'"'
    no=c.execute(q)

    if no==1:
        print('login success')
        b2 = Button(win, text="DELETE",  bg='orange',command=delete).place(x=150, y=450)
        b3 = Button(win, text="SHOW",  bg='orange',command=show).place(x=200, y=450)
        b4 = Button(win, text="FIND", bg='orange',command=find).place(x=250, y=450)
        b5 = Button(win, text="UPDATE", bg='orange',command=update).place(x=295, y=450)
        b6 = Button(win, text="HELP", bg='orange',command=help).place(x=360, y=450)
        b6 = Button(win, text="SEND MESSAGE", bg='orange',command=sendmsg).place(x=415, y=390)
        LOGOUT = Button(win, text="LOG OUT", bg='red', command=logot).place(x=50, y=60)




    else:
        messagebox.showerror('user not found','USER CANT FOUND')
        print('user not found')
    conn.commit()
    conn.close()






def register():
    if e_mobile.get() == '':
        print('error')
        messagebox.showerror('mobile error', 'MObile not found')

    if e_uname.get()=='':
        print('error user')
        messagebox.showerror('username error', 'USer not found')

    if e_passwd.get()=='':
        print('error pass')
        messagebox.showerror('password error', 'PAss not found')
    else:
        if otp == int(e_otp.get()):
            mes = "how are you"
            name = str(e_name.get())
            conn = pymysql.connect(host='localhost', user='root', passwd='', db='loginout')
            print(conn)
            c = conn.cursor()
            c.execute(
                'insert into ragister values("' + name + '","' + e_mobile.get() + '","' + e_uname.get() + '","' + e_passwd.get() + '","' + mes + '")')
            messagebox.showinfo('ststus', "data register kindly login with ID no and passwd")
            conn.commit()
            conn.close()
        else:
            messagebox.showerror('error','invalid OTP')


win = Tk()

#FRAMES
f1=Frame(win,width=440,height=300,bg='tomato');
f1.place(x=5,y=0)
f2=Frame(win,width=595,height=300,bg='#49e690');
f2.place(x=450,y=0)
f3=Frame(win,width=570,height=200,bg='#c65fe8');
f3.place(x=5,y=305)

#title
my_label = Label(win, text="LOGIN", font=("Arial Bold", 30),bg='tomato');
my_label.place(x=150,y=210);

my_label = Label(win, text="REGISTER", font=("Arial Bold", 30),bg='#49e690');
my_label.place(x=650,y=210);


#GUI REGISTER

lable_name= Label(win, text='enter your name : ')
lable_name.place(x=500, y=0)
lable_mob = Label(win, text='enter your mobile : ')
lable_mob.place(x=500, y=30)
lable_user = Label(win, text='enter your ID_no : ')
lable_user.place(x=500, y=60)
lable_passwd = Label(win, text='enter your passwd : ')
lable_passwd.place(x=500, y=90)

Label_otp = Label(win, text='OTP : ')
Label_otp.place(x=840, y=30)
e_otp = Entry(win)
e_otp.place(x=880, y=30)


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

otp = random.randint(111111, 999999)


def generate():
    print(otp)
    # Your Account Sid and Auth Token from twilio.com/console
    # DANGER! This is insecure. See http://twil.io/secure
    account_sid = 'ACa05efee16e0fcdcf8d1bcc24bcf45e09'
    auth_token = 'fcfd7e97e5c3236530ce70d17312757a'
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        messaging_service_sid='MG68e802ec920dd20d24956b36a6d72305',
        body="do not share this otp with anyone OTP ==>> " + str(otp),
        to='+918421887511'
    )
    print(message.sid)


    #b23 = Button(win, text="generate_OTP", bg='pink',state=DISABLED, command=delete).place(x=830, y=30)
generate_OTP = Button(win, text='generate_OTP', command=generate, bg='pink')
generate_OTP.place(x=840, y=0)


def verify():
    if otp==int(e_otp.get()):
        print('succsess')
        account_sid = 'ACa05efee16e0fcdcf8d1bcc24bcf45e09'
        auth_token = 'fcfd7e97e5c3236530ce70d17312757a'
        client = Client(account_sid, auth_token)
        message = client.messages \
            .create(
            messaging_service_sid='MG68e802ec920dd20d24956b36a6d72305',
            body="VERIFICATION SUCCESS..✅",
            to='+918421887511'
        )
    else:
        print('failed')
        account_sid = 'ACa05efee16e0fcdcf8d1bcc24bcf45e09'
        auth_token = 'fcfd7e97e5c3236530ce70d17312757a'
        client = Client(account_sid, auth_token)
        message = client.messages \
            .create(
            messaging_service_sid='MG68e802ec920dd20d24956b36a6d72305',
            body="VERIFICATION FAILED..❌",
            to='+918421887511'
        )
verify_OTP = Button(win, text='verify_OTP', command=verify, bg='green' ,fg='white')
verify_OTP.place(x=937, y=0)









#GUI LOGIN

lable_user=Label(win,text='ID_no : ')
lable_user.place(x=0,y=0)
lable_pass=Label(win,text='password : ')
lable_pass.place(x=0,y=30)

e_user=Entry(win)
e_user.place(x=70,y=0)
e_pass=Entry(win)
e_pass.place(x=70,y=30)

e_message = Entry(win)
e_message.place(x=415, y=330)
lable_msgid = Label(win, text='ID_no : ')
lable_msgid.place(x=365, y=355)
e_idmsg = Entry(win)
e_idmsg.place(x=415, y=357)

login=Button(win,text='login',command=login,bg='green',fg='white')
login.place(x=0,y=60)

fpass = Button(win, text='forgot password', command=fpas, bg='black', fg='white')
fpass.place(x=130, y=60)

#login=Button(win,text='CALCULLATOR',command=CAL,bg='orange',fg='green')
#login.place(x=900,y=120)


win.geometry('1050x950')
win.configure(bg='#FFC0CB')
win.title('record managment system')

win.mainloop()

