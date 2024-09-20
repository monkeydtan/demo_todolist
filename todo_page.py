import tkinter as tk
from tkinter import messagebox
from PIL import Image,ImageTk
from tkinter import messagebox

app = tk.Tk()
app.title("To Do List")
app.geometry("500x500")
app.configure(background="light steel blue")

#list_count = 1 #ตัวแปรเริ่มต้นที่ 1
text_placeholder = "เพิ่มรายการของคุณ" # ข้อความเริ่มต้นที่จะแสดงที่ช่องกรอกข้อความ (message_box)

# ฟังก์ชันการกด Add แล้วมีการบันทึกลงใน Listbox
def msg_todolist():
    #global list_count
    global selected_list
    msg = message_box.get("1.0", tk.END).strip() #ดึงข้อความจากช่องกรอกข้อความ และ เก็บไว้ในตัวแปร msg
    if msg and msg != text_placeholder:
        #list_box.insert(tk.END,f"{list_count}. {msg}")
        #list_count += 1
        list_box.insert(tk.END,msg)
        message_box.delete("1.0",tk.END) # ก่อนหน้าใช้ message_box.delete(0,tk.END) มันเลยไม่กลับไปเป็นค่าเริ่มต้น
        add_placeholder()
        
# ฟังก์ชัน add placeholder ==> กล่องข้อความแสดงข้อความเริ่มต้น หรือ placeholder
def add_placeholder(event=None):
    text_typesomething = message_box.get("1.0",tk.END).strip() # ข้อความที่พิมพ์ลงไป --> เก็บไว้ในตัวแปร text_typesomething
    if not text_typesomething: # ถ้ากล่องข้อความ message_box เป็นค่าว่าง --> not text_typesomething คือ ไม่ใช่หรือไม่มีข้อความที่พิมพ์ลงไป
        message_box.insert("1.0",text_placeholder)
        message_box.config(fg="grey")

# ฟังก์ชัน clear placeholder ==> ข้อความ placeholder หายไปจากกล่องข้อความ 
def clear_placeholder(event=None):
    global text_placeholder
    text_typesomething = message_box.get("1.0",tk.END).strip()
    if text_typesomething == text_placeholder: #ถ้าช่องกรอกข้อความ มีค่าเท่ากับ คำว่า เพิ่มรายการของคุณ
        message_box.delete("1.0",tk.END) # ลบ
        message_box.config(fg="black")
        
# ฟังก์ชันการลบ List ที่เคยบันทึกไว้
def delete_list(event):
    deleted_list = list_box.curselection() #.curselection()การเลือก เท่ากับว่า เลือก list box และเก็บค่าไว้ในตัวแปร deleted_list 
    if deleted_list:
        item_list = list_box.get(deleted_list)
        confirm = messagebox.askyesno("ลบรายการ","คุณต้องการลบรายการนี้ใช่หรือไม่")
        if confirm:
            list_box.delete(deleted_list)

    
# กรอบหัวข้อ
frame_header = tk.Frame(app,background='light steel blue')
frame_header.pack(expand=False)

# หัวข้อ
header = tk.Label(frame_header,text="To Do List",font=('Arial',20,"bold"),background='light steel blue',fg='black')
header.grid(pady=(20,10),row=0,column=0)

# กล่องข้อความ และ ปุ่ม Add
message_box = tk.Text(frame_header,width=50,height=5,)
message_box.grid(row=1,column=0)
message_box.insert("1.0", text_placeholder)
message_box.config(fg='grey')

# เชื่อมเหตุการณ์(event) กับ ฟังก์ชัน 
# *** .bind ใช้สำหรับผูกเหตุการณ์ (event) กับฟังก์ชัน
message_box.bind("<FocusIn>",clear_placeholder)
message_box.bind("<FocusOut>",add_placeholder)
message_box.bind("<Key>",clear_placeholder)


add_btn = tk.Button(frame_header,width=5,text="Add",command=msg_todolist)
add_btn.grid(row=2,column=0,pady=(10,0),sticky="e")

# หัวข้อ to do list
header_listbok = tk.Label(frame_header,text="My to-do list",background='light steel blue',font=('Arial',12,"bold"),)
header_listbok.grid(row=3,column=0,pady=(10,0),sticky="w")
# list bok
list_box = tk.Listbox(frame_header)
list_box.grid(row=4,column=0,pady=(5,0),sticky="nsew")

# เชื่อมเหตุการณ์(event) กับ ฟังก์ชัน การลบ List
list_box.bind("<Double-1>",delete_list)



app.mainloop()