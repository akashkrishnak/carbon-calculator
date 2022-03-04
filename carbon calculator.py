import cx_Oracle
import re
from tkinter import * 
from tkinter.ttk import *

cx_Oracle.init_oracle_client(lib_dir= r"D:\instantclient_21_3")
master = Tk()
master.geometry("600x320")
master.resizable(False, False)
master.title("Carbon Emission Calculator of a Car")
try:

	con = cx_Oracle.connect('carb_em/test@localhost:1521/xe')
	print(con.version)

	print("Connected to database successfully")

except cx_Oracle.DatabaseError as e:
	print("There is a problem with Oracle", e)


def pr():
    res=(float(miles.get())/float(fuel.get()))*19.36/2204.6
    value=Label(master,text="                            ",font=50).place(x=350,y=250)
    value=Label(master,text=str(round(res,3))+" tons",font=50).place(x=350,y=250)
    m=miles.get()
    f=fuel.get()
    n=names.get()
    cursor = con.cursor()
    mySql_insert_query = """INSERT INTO carbon_emission VALUES (:1, :2, :3, :4) """
    cursor.execute(mySql_insert_query, (n,m,f,res))
    con.commit()

def gr():
    cursor = con.cursor()
    cursor.execute("SELECT NAME FROM CARBON_EMISSION WHERE CARBON_EMISSION=(SELECT MAX(CARBON_EMISSION) FROM CARBON_EMISSION)")
    nm=cursor.fetchone()
    str = ''
    for item in nm:
        str = str + item
    grname1=Label(master,text="                                          ",font=50).place(x=350,y=275)
    grname1=Label(master,text=str,font=50).place(x=350,y=275)
    con.commit()


miles=StringVar()
fuel=StringVar()
names=StringVar()
name=Label(master,text="Enter you name:",font=50).place(x=60,y=50)
nameentry=Entry(master,width=30,textvariable=names).place(x=300,y=52.5)
milesdriven=Label(master,text="Miles Driven :",font=50).place(x=60,y=85)
milesentry=Entry(master,width=30,textvariable=miles).place(x=300,y=87.5)
fuelefficiency=Label(master,text="Fuel Efficiency :",font=50).place(x=60,y=120)
fuelentry=Entry(master,width=30,textvariable=fuel).place(x=300,y=122.5)
calc=Button(text="Calculate",command=pr).place(x=250,y=175)
large=Button(text="Greatest Emission",command=gr).place(x=250,y=210)
carbonemission=Label(master,text="Carbon Emission:",font=50).place(x=170,y=250)
value=Label(master,text="0",font=50).place(x=350,y=250)
grname=Label(master,text="Greatest Emission:",font=50).place(x=170,y=275)
grname1=Label(master,text="None",font=50).place(x=350,y=275)
mainloop()
