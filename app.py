import tkinter as tk
from PIL import ImageTk,Image
import tkinter.font as font
from tkinter import messagebox
from detection import Phonedetection1


class EntryWithPlaceholder(tk.Entry):
    def __init__(self,master=None, placeholder="PLACEHOLDER", color='grey',):
        super().__init__(master) 

        self.placeholder = placeholder
        self.placeholder_color = color
        self.default_fg_color = self['fg']

        self.bind("<FocusIn>", self.foc_in)
        self.bind("<FocusOut>", self.foc_out)

        self.put_placeholder()
  

    def put_placeholder(self):
        self.insert(0, self.placeholder)
        self['fg'] = self.placeholder_color

    def foc_in(self, *args):
        if self['fg'] == self.placeholder_color:
            self.delete('0', 'end')
            self['fg'] = self.default_fg_color

    def foc_out(self, *args):
        if not self.get():
            self.put_placeholder()


class login:

    def __init__(self):
        self.Login=tk.Tk()
        width = 1000 # Width 
        height = 700 # Height
        
        screen_width = self.Login.winfo_screenwidth()  # Width of the screen
        screen_height = self.Login.winfo_screenheight() # Height of the screen
        
        # Calculate Starting X and Y coordinates for Window
        x = (screen_width/2) - (width/2)
        y = (screen_height/2) - (height/2)
        self.Login.geometry('%dx%d+%d+%d' % (width, height, x, y))
        self.Login.configure(bg="#004b84")
        self.login_as=""
        self.images_path = "E:\\FYP GUI\\images\\"
        self.Login.title("Phone Detection")

        #
        file_name = "images//L1.jpg"
        stdfilee = Image.open(file_name)
        stdshow = ImageTk.PhotoImage(stdfilee)
        self.imageshow = tk.Label(self.Login, image=stdshow, border=0)
        self.imageshow.image = stdshow
        self.imageshow.place(relx=0.02, rely=0.4)

        file_name = "images//L2.png"
        stdfilee = Image.open(file_name)
        stdshow = ImageTk.PhotoImage(stdfilee)
        self.imageshow = tk.Label(self.Login, image=stdshow, border=0)
        self.imageshow.image = stdshow
        self.imageshow.place(relx=0.71, rely=0.00)
        # #


        self.frame=tk.Frame(self.Login,bg="#ffffff")
        self.frame.place(relx=0.25,rely=0.2,relwidth=0.55,relheight=0.65)

        self.Fontlabel = font.Font(family="Times", size=27,)

        self.Fontlabel1 = font.Font(family="Times", size=20,)

        self.Fontlabel2 = font.Font(family="Times", size=13,)
        self.Fontlabel3 = font.Font(family="Times", size=10,)

        
        # self.left_fame=tk.Frame(self.frame,bg="#01375d")
        # self.left_fame.place(relwidth=0.4,relheight=1.00)

        self.login_box=tk.Frame(self.frame,bg="#fff",border=5)
        self.login_box.place(relx=0,rely=0.15,relwidth=1,relheight=1)


        

        file_name="images//149071.jpg"
        stdfilee=Image.open(file_name)
        stdshow=ImageTk.PhotoImage(stdfilee)
        self.imageshow=tk.Label(self.frame,image=stdshow,border=0)
        self.imageshow.image=stdshow
        self.imageshow.place(relx=0.35,rely=0.06)

        # self.label=tk.Label(self.left_fame,text="Welcome Back",bg="#01375d",fg="white")
        # self.label['font']=self.Fontlabel
        # self.label.place(relx=0.13,rely=0.47)

        self.label1=tk.Label(self.login_box,text="Phone Detection",bg="white",fg="#154360")
        self.label1['font']=self.Fontlabel1
        self.label1.place(relx=0.3,rely=0.2)

        


          
        file_name="images//user.jpg"
        stdfilee=Image.open(file_name)
        stdshow=ImageTk.PhotoImage(stdfilee)
        self.imageshow7=tk.Label(self.login_box,image=stdshow,border=0)
        self.imageshow7.image=stdshow
        self.imageshow7.place(relx=0.055,rely=0.25)


        self.imageshow7.place_forget()



        

        
        #---------------------------- textbox frame--------------------------------->
        self.frame_Email_textbox=tk.Frame(self.login_box,bg="#e7e7e7")
        self.frame_Email_textbox.place(relx=0.02,rely=0.3,relwidth=0.9,relheight=0.08)


        self.frame_Pass_textbox=tk.Frame(self.login_box,bg="#e7e7e7")
        self.frame_Pass_textbox.place(relx=0.02,rely=0.5,relwidth=0.9,relheight=0.08)








        # file_name="user_icon.jpg"
        # stdfilee=Image.open(file_name)
        # stdshow=ImageTk.PhotoImage(stdfilee)
        # self.imageshow5=tk.Label(self.frame_Email_textbox,image=stdshow,border=0)
        # self.imageshow5.image=stdshow
        # self.imageshow5.place(relx=0.05,rely=0.12)
       
        


        self.Email_text=EntryWithPlaceholder(self.frame_Email_textbox, "Email",)
        self.Email_text['border']=0
        self.Email_text['bg']="#e7e7e7"
        self.Email_text['fg']="#666666"
        self.Email_text['font']=self.Fontlabel3
        self.Email_text.place(relx=0.04,rely=0.01,relwidth=0.3,relheight=1)
        self.Email_text.bind("<Leave>", self.email_leave)
        self.Email_text.bind("<Button-1>", self.email_click)


       

        self.pass_text=EntryWithPlaceholder(self.frame_Pass_textbox,"Password")
        self.pass_text['border']=0
        self.pass_text['bg']="#e7e7e7"
        self.pass_text['fg'] = "#666666"
        self.pass_text['font']=self.Fontlabel3
        self.pass_text.place(relx=0.04,rely=0.01,relwidth=0.8,relheight=1)
        self.pass_text.bind("<Leave>", self.password_leave)
        self.pass_text.bind("<Button-1>", self.password_click)


        self.login_button=tk.Button(self.login_box,text="Login",bg="#154360",fg="white")
        self.login_button['font']=self.Fontlabel2 
        self.login_button.place(relx=0.045,rely=0.6,relwidth=0.25,relheight=0.1)
        self.login_button.bind("<Button-1>", self.get_login)



     
        
        self.Login.mainloop()
    
    def email_click(self,*args):
        self.Email_text.delete(0, 'end')

    def email_leave(self,*args):
        if self.Email_text.get()=="" :
            self.Email_text.delete(0, 'end')
            self.Email_text.insert(0, 'Email')
            # self.Login.focus()
    
    def password_click(self,*args):
        self.pass_text.delete(0, 'end')

    def password_leave(self,*args):
        if self.pass_text.get()=="" :
            self.pass_text.delete(0, 'end')
            self.pass_text.insert(0, 'Password')
    def get_login(self,*args):
        if self.pass_text.get()=="admin" and self.Email_text.get()=="admin":
            self.Login.destroy()
            Phonedetection1()
        else:
            messagebox.showerror("error","Invalid email and password")   
login()