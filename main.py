import googletrans
from googletrans import Translator
from tkinter import *
from PIL import Image,ImageTk
root = Tk()
root.title("Google Translate")
root.geometry("500x630")
root.iconbitmap("IconLion.ico")
#Hiển thị background
bg = Image.open("background.jpg")
render = ImageTk.PhotoImage(bg)
img = Label(root,image = render)
img.place(x=0,y=0)
#Hiển thị tiêu đề
name = Label(root,text="Google dịch của Sử Tử Nhỏ",fg="red",bd = 0, bg = "#EFB784")
name.config(font=("Arial",16))
name.pack(pady=28)
#Hiển thị chatbox
box = Text(root,width=28,height=8,font=("Arial",16),bg = "#FFFFFF")
box.pack(pady=5)

#button
button_frame = Frame(root).pack(side=BOTTOM)

def clear():
    box.delete(1.0,END)
    result.delete(1.0, END)
def trans():
    txt = box.get(1.0,END)
    t = Translator()
    a = t.translate(txt,src="vi",dest="en")
    result_txt = a.text
    result.insert(END,result_txt)


clear_bt=Button(button_frame,text="Xoá",font= ("Arial",10,"bold"),bg="#FFFFFF",fg="#2B2B2B",command=clear)
clear_bt.place(x=310,y=290)
trans_bt=Button(button_frame,text="Dịch",font= ("Arial",10,"bold"),bg="#FFFFFF",fg="#2B2B2B",command=trans)
trans_bt.place(x=150,y=290)
#Hiển thị kết quả
result = Text(root,width=28,height=8,font=("Arial",16),bg = "#FFFFFF")
result.pack(pady=40)



root.resizable(width=False, height=False)
root.mainloop()
#print(googletrans.LANGUAGES)