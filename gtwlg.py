from tkinter import *
from tkinter import messagebox
from tkinter import ttk

root=Tk()
root.title('Number convertor')
root.geometry('1280x720')

#====================variable====================
num=IntVar()
s=StringVar()
lblbinary=StringVar()
lbldecimal=StringVar()
lblhexa=StringVar()
lbloctal=StringVar()
lbascii=StringVar()
#===================Notebook=====================
#Create notebook
notebook = ttk.Notebook(root)
notebook.pack(pady=10,expand=True)
#create frames
frame1 = Frame(notebook, width=1280, height=720)

frame2 = Frame(notebook, width=1280, height=720)
#add frames to notebook
notebook.add(frame1, text='Number Converter')
notebook.add(frame2, text='String Converter')

notebook.pack(expand=True, fill='both')

#===================functions=====================
def convertn():
    if num.get()==0:
        messagebox.showerror('Error','You must enter a number to convert')
    else:
        #number to binary,decimal,hexa,octal
        lblbinary.set(str(bin(num.get())))
        lbldecimal.set(str(num.get()))
        lblhexa.set(str(hex(num.get())))
        lbloctal.set(str(oct(num.get())))



def clear():
    num.set(0)
    lblhexa.set('')
    lblbinary.set('')
    lbldecimal.set('')
    lbloctal.set('')





#===================number(frame1)=====================
Label(frame1,text='Number Converter',font=('times new rommon',60,'bold'),bg='Black',fg='crimson',relief=RIDGE).pack(pady=10)

n=Label(frame1,text='Enter Number',font='arial 20 bold')
n.place(x=300,y=150)
n_txt=Entry(frame1,font=('times new rommon',20,'bold'),fg='blue',justify=CENTER,relief=GROOVE,textvariable=num)
n_txt.place(x=650,y=160)

b=Label(frame1,text='Binary',font='arial 20 bold')
b.place(x=300,y=230)
b_txt=Entry(frame1,font=('times new rommon',20,'bold'),fg='blue',justify=CENTER,relief=GROOVE,textvariable=lblbinary)
b_txt.place(x=650,y=230)

d=Label(frame1,text='decimal',font='arial 20 bold')
d.place(x=300,y=310)
d_txt=Entry(frame1,font=('times new rommon',20,'bold'),fg='blue',justify=CENTER,relief=GROOVE,textvariable=lbldecimal)
d_txt.place(x=650,y=300)

h=Label(frame1,text='Hexa Decimal',font='arial 20 bold')
h.place(x=300,y=390)
h_txt=Entry(frame1,font=('times new rommon',20,'bold'),fg='blue',justify=CENTER,relief=GROOVE,textvariable=lblhexa)
h_txt.place(x=650,y=380)


o=Label(frame1,text='Octal',font='arial 20 bold')
o.place(x=300,y=470)
o_txt=Entry(frame1,font=('times new rommon',20,'bold'),fg='blue',justify=CENTER,relief=GROOVE,textvariable=lbloctal)
o_txt.place(x=650,y=460)

btn1=Button(frame1,text='Converter',font='arial 20 bold',fg='white',bg='green',width=10,relief=GROOVE,bd=10,command=convertn)
btn1.place(x=310,y=550)

btn2=Button(frame1,text='Clear',font='arial 20 bold',fg='white',bg='red',width=10,relief=GROOVE,bd=10,command=clear)
btn2.place(x=760,y=550)

#===================String(frame2)=====================
Label(frame2,text='String Converter',font=('times new rommon',60,'bold'),bg='Black',fg='crimson',relief=RIDGE).pack(pady=10)

n=Label(frame2,text='Enter String',font='arial 20 bold')
n.place(x=300,y=150)
n_txt=Entry(frame2,font=('times new rommon',20,'bold'),fg='blue',justify=CENTER,relief=GROOVE,textvariable=s)
n_txt.place(x=650,y=160)

b=Label(frame2,text='Binary',font='arial 20 bold')
b.place(x=300,y=230)
b_txt=Entry(frame2,font=('times new rommon',20,'bold'),fg='blue',justify=CENTER,relief=GROOVE,textvariable=b)
b_txt.place(x=650,y=230)

d=Label(frame2,text='decimal',font='arial 20 bold')
d.place(x=300,y=310)
d_txt=Entry(frame2,font=('times new rommon',20,'bold'),fg='blue',justify=CENTER,relief=GROOVE,textvariable=b)
d_txt.place(x=650,y=300)

h=Label(frame2,text='Hexa Decimal',font='arial 20 bold')
h.place(x=300,y=390)
h_txt=Entry(frame2,font=('times new rommon',20,'bold'),fg='blue',justify=CENTER,relief=GROOVE,textvariable=b)
h_txt.place(x=650,y=380)


o=Label(frame2,text='Octal',font='arial 20 bold')
o.place(x=300,y=470)
o_txt=Entry(frame2,font=('times new rommon',20,'bold'),fg='blue',justify=CENTER,relief=GROOVE,textvariable=b)
o_txt.place(x=650,y=460)

btn1=Button(frame2,text='Converter',font='arial 20 bold',fg='white',bg='green',width=10,relief=GROOVE,bd=10,command=convertn)
btn1.place(x=310,y=550)

btn2=Button(frame2,text='Clear',font='arial 20 bold',fg='white',bg='red',width=10,relief=GROOVE,bd=10,command=clear)
btn2.place(x=760,y=550)

root.mainloop()