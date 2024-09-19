import tkinter as tk
from tkinter import messagebox
from PIL import Image,ImageTk

app = tk.Tk()
app.title("To Do List")
app.geometry("500x500")
app.configure(background="light steel blue")


def msg_todolist():
    msg = message_box.get("1.0", tk.END).strip() #ดึงข้อความจากช่องกรอกข้อความ และ เก็บไว้ในตัวแปร msg
    if msg:
        list_box.insert(tk.END,msg)
        message_box.delete(0,tk.END)
        
    
# ฟังก์ชันเมื่อกด add
# def func_add():

# กรอบหัวข้อ
frame_header = tk.Frame(app,background='light steel blue')
frame_header.pack(expand=False)

# หัวข้อ
header = tk.Label(frame_header,text="To Do List",font=('Arial',20,"bold"),background='light steel blue',fg='black')
header.grid(pady=(20,10),row=0,column=0)

# กล่องข้อความ และ ปุ่ม Add
message_box = tk.Text(frame_header,width=50,height=5)
message_box.grid(row=1,column=0)

add_btn = tk.Button(frame_header,width=5,text="Add",command=msg_todolist)
add_btn.grid(row=2,column=0,pady=(10,0),sticky="e")

# หัวข้อ to do list
header_listbok = tk.Label(frame_header,text="My to-do list",background='light steel blue',font=('Arial',12,"bold"),)
header_listbok.grid(row=3,column=0,pady=(10,0),sticky="w")
# list bok
list_box = tk.Listbox(frame_header)
list_box.grid(row=4,column=0,pady=(5,0),sticky="nsew")



app.mainloop()