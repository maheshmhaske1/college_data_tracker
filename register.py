import pymysql
from tkinter import *
win=Tk()
from tkinter import messagebox
con=pymysql.connect(host='localhost',user='root',passwd='',db='contact')
print(con)
c=con.cursor()
c.execute('insert into a values(5)')
con.commit()
con.close()
def insert():
    messagebox.showinfo('status', 'value inserted')


Button(win,text='add',command=insert).pack()
win.mainloop()
