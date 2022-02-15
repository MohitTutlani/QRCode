#mixture of encoding and decoding
from tkinter import *
from tkinter import messagebox
import qrcode
from pyzbar.pyzbar import decode
from PIL import Image

#tkinter window
window = Tk()
window.title("QR code Encoder & Decoder")
window.resizable(0,0)
window.geometry("400x200")

#------------------Encoder & Decoder---------------------#
def de_code():
    name = file_name.get()
    
    if name:
         img = Image.open('E:/Study Material/LAB/Python/QRcode/'+name+'.png')
         result = decode(img)
         new_window = Tk()
         new_window.title("Decode ANS")
         new_label= Label(new_window,text=result)
         new_label.grid(row=0,column=0)
    else:
        messagebox.showerror("Error in new Window","Please insert name of file to Decode QR code")

def en_code():
    
    data = url_entry.get()
    name = file_name.get()

    if data and name:
     qr = qrcode.QRCode(version = 3, box_size=10, border = 5)
     qr.add_data(data)
     qr.make(fit=True)
     img = qr.make_image(fill_color='black',back_color = 'white')
     
     img.save('E:/Study Material/LAB/Python/QRcode/'+name+'.png')
     messagebox.showinfo("ENCODED","QR code created, Please check your folder...!")
    else:
        messagebox.showerror("Error", "Please insert text into the textbox...!")



#--------------------GUI layout---------------------------#
url_label = Label(window,text="QR code Link", padx = 20).grid(row=0,column=0)
file_name = Label(window,text="File Name", padx = 20).grid(row=1,column=0)

url_entry = Entry(width=30)
url_entry.insert(END, string="")
url_entry.grid(row=0,column=1)

file_name = Entry(width=30)
file_name.insert(END,string="")
file_name.grid(row=1,column=1)

en_code_btn = Button(window, text="Encode QR code", command = en_code).grid(row=2,column=0)
de_code_btn = Button(window, text="Decode QR code", command = de_code).grid(row=2,column=1)


window.mainloop()

