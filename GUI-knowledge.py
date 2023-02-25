from tkinter import *
from tkinter import ttk #ttk คือ subsetของ tkinter
from tkinter import messagebox

GUI = Tk() #นี้คือหน้าจอของโปรแกรม
GUI.title('โปรแกรมบันทึกข้อมูล') #นี้คือชื่อโปรแกรม
GUI.geometry('1000x400') #นี้คือขนาดของโปรแกรม

B1 = ttk.Button(GUI,text='เงินมีอยู่กี่่บาท') 
B1.pack(ipadx=30,ipady=30) 
##
def Button2():
    text = 'ตอนนี้มีเงินในบัญชีอยู่ 300 บาท'
    messagebox.showinfo('เงินในบัญชี',text)

FB1 = Frame(GUI)  #frame=ไม้กระดาน
FB1.place(x=300,y=300)
B2 = ttk.Button(FB1,text='เงินมีอยู่กี่่บาท',command=Button2) #FB1 
B2.pack(ipadx=20,ipady=20)
##
GUI.mainloop()
