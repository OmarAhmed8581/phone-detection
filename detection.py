import tkinter as tk
from PIL import ImageTk,Image
import tkinter.font as font
from tkinter import messagebox
import cv2
import os
class Phonedetection1:
    def __init__(self):
        self.phonedectionroot=tk.Tk()
        width = 1000 
        height = 700 
        
        screen_width = self.phonedectionroot.winfo_screenwidth()  
        screen_height = self.phonedectionroot.winfo_screenheight()

        self.Fontlabel = font.Font(family="Times", size=27,)

        self.Fontlabel1 = font.Font(family="Times", size=20,)

        self.Fontlabel2 = font.Font(family="Times", size=13,)
        self.Fontlabel3 = font.Font(family="Times", size=10,)

        
      
        x = (screen_width/2) - (width/2)
        y = (screen_height/2) - (height/2)
        self.phonedectionroot.geometry('%dx%d+%d+%d' % (width, height, x, y))
        self.phonedectionroot.configure(bg="#004b84")
       

        file_name = "images/L1.jpg"
        stdfilee = Image.open(file_name)
        stdshow = ImageTk.PhotoImage(stdfilee)
        self.imageshow = tk.Label(self.phonedectionroot, image=stdshow, border=0)
        self.imageshow.image = stdshow
        self.imageshow.place(relx=0.02, rely=0.4)

        file_name = "images/L2.png"
        stdfilee = Image.open(file_name)
        stdshow = ImageTk.PhotoImage(stdfilee)
        self.imageshow = tk.Label(self.phonedectionroot, image=stdshow, border=0)
        self.imageshow.image = stdshow
        self.imageshow.place(relx=0.71, rely=0.00)


        self.frame=tk.Frame(self.phonedectionroot,bg="#ffffff")
        self.frame.place(relx=0.25,rely=0.2,relwidth=0.55,relheight=0.65)

        self.label1=tk.Label(self.frame,text="Phone Detection",bg="white",fg="#154360")
        self.label1['font']=self.Fontlabel1
        self.label1.place(relx=0.045,rely=0.03)

        self.screen=tk.Label(self.phonedectionroot,bg="#000000",border=0)
        self.screen.place(relx=0.275,rely=0.27,relwidth=0.493,relheight=0.5)


        # self.label2=tk.Label(self.screen,text="")
        # self.label2.place(relx=0,rely=0,relwidth=1,relheight=1)



      
        self.login_box=tk.Frame(self.frame,bg="#fff",border=5)
        self.login_box.place(relx=0,rely=0.15,relwidth=1,relheight=1)
        self.login_button=tk.Button(self.frame,text="Open Video Screen",bg="#154360",fg="white")
        self.login_button['font']=self.Fontlabel2 
        self.login_button.place(relx=0.045,rely=0.88,relwidth=0.9,relheight=0.1)
        self.login_button.bind("<Button-1>", self.camera_open)

        self.phonedectionroot.mainloop()

   


    def camera_open(self,*args):
        os.system("python .//yolov5//detect.py --source 0")
