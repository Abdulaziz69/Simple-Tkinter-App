from tkinter import ttk
from tkinter.ttk import Progressbar
from tkinter import *
from moviepy.editor import VideoFileClip
import tkinter as tk
from time import sleep
from pathlib import Path
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image
import numpy as np
import cv2
from pdf2image import convert_from_path

LARGE_FONT_STYLE = ("Arial", 40, "bold")
SMALL_FONT_STYLE = ("Arial", 16)
DIGITS_FONT_STYLE = ("Arial", 28, "bold")
DEFAULT_FONT_STYLE = ("Arial", 17)
PASS_FONT = ("Arial", 35, "bold")

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)
def box_image():
    messagebox.showinfo("Result", 'Image Save Successful')
def box_Sound():
    messagebox.showinfo("Result", 'Sound Save Successful')

class GUI:
    def __init__(self):
        self.app = tk.Tk()
        self.app.geometry('1000x700')
        self.app.configure(bg='#121212')
        self.app.title('Delta')
        # self.app.resizable(False, False)
        # self.app.update_idletasks()
        self.app.overrideredirect(True)
        # self.app_offsetx = 0
        # self.app_offsety = 0
        self.app.bind("<ButtonPress-1>", self.StartMove)
        self.app.bind("<ButtonRelease-1>", self.StopMove)
        self.app.bind("<B1-Motion>", self.OnMotion)

        self.window = Canvas(
            self.app,
            bg = '#121212',
            height = 700,
            width = 1000,
            bd = 0,
            highlightthickness = 0,
            relief = 'ridge'
        )
        self.window.place(x = 0, y = 0)
        self.current_value = tk.StringVar()
        self.path_value = tk.StringVar()
        #self.path_save = tk.StringVar()
        self.name_value = tk.StringVar()
        self.name_mp3 = tk.StringVar()
        #self.image_name = tk.StringVar()
        self.Checkbutton1 = IntVar()  
        self.Checkbutton2 = IntVar()  
        self.Checkbutton3 = IntVar()
        self.Checkbutton4 = IntVar()
        self.Checkbutton5 = IntVar()
        self.Checkbutton6 = IntVar()
        self.Checkbutton7 = IntVar()
        self.Checkbutton8 = IntVar()
        self.Checkbutton9 = IntVar()
        self.creat_backround_images = self.creat_backround()
        self.creat_buttons = self.creat_Button()
        self.creat_rectangels = self.creat_rectangel()
        self.creat_text = self.Creat_Text()
        self.creat_labels = self.creat_label()
        self.creat_checkbutton = self.creat_checkButton()
        #self.creat_progressbar = self.Progressbar() #ERROR

    def StartMove(self, event):
        self.x = event.x
        self.y = event.y

    def StopMove(self, event):
        self.x = None
        self.y = None

    def OnMotion(self, event):
        deltax = event.x - self.x
        deltay = event.y - self.y
        x = self.app.winfo_x() + deltax
        y = self.app.winfo_y() + deltay
        self.app.geometry("+%s+%s" % (x, y))
        print(self.app.geometry())

    def creat_backround(self):
        backround_convert = tk.PhotoImage(file = relative_to_assets('entry_1.png'))
        backround_convert_place = self.window.create_image(
            142.5,
            276.99999999999994,
            image = backround_convert
        )
        backround_convert_mp4 = tk.PhotoImage(file = relative_to_assets('entry_2.png'))
        backround_convert_mp4_place = self.window.create_image(
            379.0,
            276.99999999999994,
            image = backround_convert_mp4
        )
        backround_option = tk.PhotoImage(file = relative_to_assets('entry_3.png'))
        backround_option_place = self.window.create_image(
            606.5,
            276.99999999999994,
            image = backround_option
        )
        backround_convert_pdf = tk.PhotoImage(file = relative_to_assets('entry_4.png'))
        backround_convert_pdf_place = self.window.create_image(
            857.5,
            276.99999999999994,
            image = backround_convert_pdf
        )
        return backround_convert, backround_convert_mp4, backround_option, backround_convert_pdf
    
    def creat_Button(self):
        button_image_1 = tk.PhotoImage(
            file = relative_to_assets('Button1.png')
        )
        button_1 = tk.Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.PNG2PDF,
            relief='flat'
        )
        button_1.place(
            x=39.0,
            y=348.99999999999994,
            width=208.0,
            height=88.0
        )
        button_image_2 = PhotoImage(
            file=relative_to_assets("Button2.png"))
        button_2 = Button(
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command = self.MP4TOMP3,
            relief="flat"
        )
        button_2.place(
            x=288.0,
            y=350.99999999999994,
            width=184.0,
            height=81.0
        )
        button_image_3 = PhotoImage(
            file=relative_to_assets("Button3&4.png"))
        button_3 = Button(
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command = self.PNG2PDF,
            relief="flat"
        )
        button_3.place(
            x=766.0,
            y=356.99999999999994,
            width=183.0,
            height=74.0
        )

        button_image_4 = PhotoImage(
            file=relative_to_assets("Button3&4.png"))
        button_4 = Button(
            image=button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=self.Options,
            relief="flat"
        )
        button_4.place(
            x=513.0,
            y=356.99999999999994,
            width=189.0,
            height=71.0
        )
        button_image_5 = PhotoImage(
            file=relative_to_assets("Button5.png"))
        self.button_5 = Button(
            image=button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command = self.browsefunc,
            relief="flat",
        )
        self.button_5.place(
            x=448.0,
            y=595.0,
            width=93.0,
            height=95.0
        )

        button_6 = Button(
            text='X',
            fg='white',
            font=("Roboto blod", 30 * -1),
            borderwidth=0,
            highlightthickness=0,
            command = exit,
            relief="flat",
            background='#DB1A1A'
        )
        button_6.place(
            x=933.0,
            y=0.0,
            width=67.0,
            height=38.0
        )
        return button_image_1, button_image_2, button_image_3, button_image_4,button_image_5
    def creat_rectangel(self):
        self.x = self.window.create_rectangle(
            2.460081759636523e-06,
            2.7064797848197486e-05,
            1000.0000024600818,
            88.00002706479785,
            fill="#1F1F1F",
            outline="")
        self.window.create_rectangle(
            0.0,
            650.0,
            1000.0,
            700.0,
            fill="#1F1F1F",
            outline="")
             
    def Creat_Text(self):
        self.window.create_text(254.0,-10,anchor="nw",text="     Delta",fill="#BB86FC",font=("Times", "70", "bold italic"))
        self.window.create_text(21.0,124.99999999999994,anchor="nw",text="Convert Image To :",fill="#FFFFFF",font=("Roboto Black", 26 * -1, "bold"))
        self.window.create_text(329.0,124.99999999999994,anchor="nw",text="Convert\n   MP4 \n    TO\n   MP3",fill="#FFFFFF",font=("Roboto Black", 26 * -1, "bold"))
        self.window.create_text(740.0,124.99999999999994,anchor="nw",text="PDF TO PNG",fill="#FFFFFF",font=("Roboto Black", 26 * -1, "bold"))
        self.window.create_text(494.0,124.99999999999994,anchor="nw",text="Image Options :",fill="#FFFFFF",font=("Roboto Black", 26 * -1, "bold"))
        self.window.create_text(59.0,185.99999999999994,anchor="nw",text="PNG",fill="#FFFFFF",font=("Roboto Light", 22 * -1))
        self.window.create_text(537.0,185.99999999999994,anchor="nw",text="Black & White",fill="#FFFFFF",font=("Roboto Light", 22 * -1))
        self.window.create_text(537.0,251.99999999999994,anchor="nw",text="Face Detection",fill="#FFFFFF",font=("Roboto Light", 22 * -1))
        self.window.create_text(537.0,317.99999999999994,anchor="nw",text="Smile Detection",fill="#FFFFFF",font=("Roboto Light", 22 * -1))
        self.window.create_text(59.0,233.99999999999994,anchor="nw",text="JPEG",fill="#FFFFFF",font=("Roboto Light", 22 * -1))
        self.window.create_text(740.0,156.99999999999994,anchor="nw",text="Image Name :",fill="#FFFFFF",font=("Roboto Light", 22 * -1))
        self.window.create_text(284.0,251.99999999999994,anchor="nw",text="Video Name :",fill="#FFFFFF",font=("Roboto Light", 22 * -1))
        self.window.create_text(740.0,251.99999999999994,anchor="nw",text="Page Count :",fill="#FFFFFF",font=("Roboto Light", 22 * -1))
        self.window.create_text(59.0,289.99999999999994,anchor="nw",text="PMM",fill="#FFFFFF",font=("Roboto Light", 22 * -1))
        self.window.create_text(183.0,185.99999999999994,anchor="nw",text="TIFF",fill="#FFFFFF",font=("Roboto Light", 22 * -1))
        self.window.create_text(183.0,235.99999999999994,anchor="nw",text="BMP",fill="#FFFFFF",font=("Roboto Light", 22 * -1))
        self.window.create_text(183.0,289.99999999999994,anchor="nw",text="GIF",fill="#FFFFFF",font=("Roboto Light", 22 * -1))
        self.window.create_text(740.0,185.99999999999994,anchor="nw",text="*",fill="#B00020",font=("Roboto Black", 26 * -1))
        self.window.create_text(284.0,276.99999999999994,anchor="nw",text="*",fill="#B00020",font=("Roboto Black", 26 * -1))
        self.window.create_text(737.0,277.99999999999994,anchor="nw",text="*",fill="#B00020",font=("Roboto Black", 26 * -1))
        self.window.create_text(565.0,560.0,anchor="nw",text="Input Path",fill="#FFFFFF",font=("Roboto ligth", 22 * -1))

    def creat_label(self):
        entry_image_5 = PhotoImage(
            file=relative_to_assets("entry_5.png")
        )
        entry_bg_5 = self.window.create_image(
            847.5,
            227.49999999999994,
            image=entry_image_5
        )
        entry_5 = Entry(
            textvariable = self.name_value,
            bd=0,
            bg="#3F3F3F",
            highlightthickness=0,
            font=('Roboto', 15)
        )
        entry_5.place(
            x=753.0,
            y=206.99999999999994,
            width=189.0,
            height=39.0
        )

        entry_image_6 = PhotoImage(
            file=relative_to_assets("entry_6.png")
        )
        entry_bg_6 = self.window.create_image(
            380.0,
            317.49999999999994,
            image=entry_image_6
        )
        entry_6 = Entry(
            textvariable = self.name_mp3,
            bd=0,
            bg="#3F3F3F",
            highlightthickness=0,
            font=('Roboto', 15)
        )
        entry_6.place(
            x=297.0,
            y=296.99999999999994,
            width=166.0,
            height=39.0
        )
        entry_image_7 = PhotoImage(
            file=relative_to_assets("entry_7.png")
        )
        entry_bg_7 = self.window.create_image(
            847.5,
            317.49999999999994,
            image=entry_image_7
        )
        self.entry_7 = Entry(
            textvariable=self.current_value,
            bd=0,
            bg="#3F3F3F",
            highlightthickness=0,
            font=('Roboto', 15),
        )
        self.entry_7.place(
            x=753.0,
            y=296.99999999999994,
            width=189.0,
            height=39.0
        )
        entry_image_8 = PhotoImage(
            file=relative_to_assets("entry_8.png")
        )
        entry_bg_8 = self.window.create_image(
            776.5,
            618.0,
            image=entry_image_8
        )
        self.entry_8 = Entry(
            textvariable = self.path_value,
            fg='white',
            bd=0,
            bg="#3F3F3F",
            highlightthickness=0,
            font=('Roboto', 16)
        )
        self.entry_8.place(
            x=575.0,
            y=594.0,
            width=403.0,
            height=46.0
        )
        # entry_image_9 = PhotoImage(
        #     file=relative_to_assets("entry_8.png")
        # )
        # entry_bg_9 = self.window.create_image(
        #     776.5,
        #     518.0,
        #     image=entry_image_9
        # )
        # self.entry_9 = Entry(
        #     textvariable = self.path_save,
        #     fg='white',
        #     bd=0,
        #     bg="#3F3F3F",
        #     highlightthickness=0,
        #     font=('Roboto', 16)
        # )
        # self.entry_9.place(
        #     x=575.0,
        #     y=494.0,
        #     width=403.0,
        #     height=46.0
        # )
        return entry_image_5, entry_image_6, entry_image_7, entry_image_8
    def creat_checkButton(self):
        Button1 = Checkbutton(self.app, 
            variable = self.Checkbutton1,
            onvalue = 1,
            offvalue = 0,
            height = 0,
            bg = '#1F1F1F',
            activebackground="#1F1F1F",
            width = 0)
  
        Button2 = Checkbutton(self.app,
            variable = self.Checkbutton2,
            onvalue = 1,
            offvalue = 0,
            height = 0,
            bg = '#1F1F1F',
            activebackground="#1F1F1F",
            width = 0)
        
        Button3 = Checkbutton(self.app,
            variable = self.Checkbutton3,
            onvalue = 1,
            offvalue = 0,
            height = 0,
            bg = '#1F1F1F',
            activebackground="#1F1F1F",
            width = 0)
        Button4 = Checkbutton(self.app,
            variable = self.Checkbutton4,
            onvalue = 1,
            offvalue = 0,
            height = 0,
            bg = '#1F1F1F',
            activebackground="#1F1F1F",
            width = 0)
        Button5 = Checkbutton(self.app,
            variable = self.Checkbutton5,
            onvalue = 1,
            offvalue = 0,
            height = 0,
            bg = '#1F1F1F',
            activebackground="#1F1F1F",
            width = 0)
        Button6 = Checkbutton(self.app,
            variable = self.Checkbutton6,
            onvalue = 1,
            offvalue = 0,
            height = 0,
            bg = '#1F1F1F',
            activebackground="#1F1F1F",
            width = 0)
        Button7 = Checkbutton(self.app,
            variable = self.Checkbutton7,
            onvalue = 1,
            offvalue = 0,
            height = 0,
            bg = '#1F1F1F',
            activebackground="#1F1F1F",
            width = 0)
        Button8 = Checkbutton(self.app,
            variable = self.Checkbutton8,
            onvalue = 1,
            offvalue = 0,
            height = 0,
            bg = '#1F1F1F',
            activebackground="#1F1F1F",
            width = 0)
        Button9 = Checkbutton(self.app,
            variable = self.Checkbutton9,
            onvalue = 1,
            offvalue = 0,
            height = 0,
            bg = '#1F1F1F',
            activebackground="#1F1F1F",
            width = 0)           
        Button1.place(x=30.0,y=185.99999999999994)
        Button2.place(x=30.0,y=233.99999999999994)
        Button3.place(x=30.0,y=289.99999999999994)
        Button4.place(x=154.0,y=185.99999999999994)
        Button5.place(x=154.0,y=233.99999999999994)
        Button6.place(x=154.0,y=289.99999999999994)
        Button7.place(x=510.0,y=185.99999999999994)
        Button8.place(x=510.0,y=252.99999999999994)
        Button9.place(x=510.0,y=317.99999999999994)


    def browsefunc(self):
        filename =filedialog.askopenfilename(filetypes=(("jpeg file","*.jpg"),('png file', '*.png'),('gif file', '*.gif'),('pdf file', '*.pdf'),("All files","*.*")))
        self.entry_8.delete(0, 'end')
        self.entry_8.insert(tk.END, filename)

    # def file_save(self):
    #     f = filedialog.asksaveasfile(mode='w', defaultextension=".txt")
    #     if f is None: # asksaveasfile return `None` if dialog closed with "cancel".
    #         return
    #     text2save = str(text.get(1.0, END)) # starts from `1.0`, not `0.0`
    #     f.write(text2save)
    #     f.close()

    def Progressbar(self):
        #self.button_5.config(state='disabled')
        s = ttk.Style()
        s.theme_use('default')
        s.configure("red.Horizontal.TProgressbar", foreground='red', background='#BB86FC')
        my_progress = Progressbar(self.app,style='red.Horizontal.TProgressbar' ,orient= HORIZONTAL, length= 430, mode= 'determinate')
        my_progress.place(x=10, y=625)
        x = 0
        for x in range(101):
            my_progress['value']=x
            self.app.update_idletasks()
            sleep(0.02)
            x=x+1
        sleep(0.5)
        my_progress.destroy()
        #self.button_5.config(state='normal')

    def PNG2PDF(self):
        path = self.path_value.get()
        path_save = filedialog.askdirectory()
        self.Progressbar()
        pages =  int(self.current_value.get())
        name = self.name_value.get()
        images = convert_from_path(f"{path}", poppler_path=r'C:\Program Files\poppler-0.68.0\bin')
        print(pages)
        print(path)
        for i, image in enumerate(images):
            fname = f'{name}'+str(i)+'.png'
            fpath = f'{path_save}/{fname}'
            image.save(fpath, "PNG")
        box_image()

    def MP4TOMP3(self):
        mp4path = self.path_value.get()
        mp3name = self.name_mp3.get()
        path_save = filedialog.askdirectory()
        self.Progressbar()
        videoclip = VideoFileClip(mp4path)
        audioclip = videoclip.audio
        audioclip.write_audiofile(f'{path_save}/{mp3name}.mp3')
        audioclip.close()
        videoclip.close()
        box_Sound()

    def Convert(self):
        if self.Checkbutton1.get() == 1:
            path = self.path_value.get()
            path_save = filedialog.askdirectory()
            self.Progressbar()
            img = Image.open(path)
            #save_path = self.browsefunc()
            #file = filedialog.asksaveasfile(mode='w', defaultextension=".png")
            #print(file[name])
            #if file:
            img.save(f'{path_save}/new image.png')
            box_image()
            #img.save(f'{save_path}')

        if self.Checkbutton2.get() == 1:
            path = self.path_value.get()
            path_save = filedialog.askdirectory()
            self.Progressbar()
            im = Image.open(path)
            rgb_im = im.convert('RGB')
            rgb_im.save(f'{path_save}/colors.jpg')
            box_image()
        if self.Checkbutton3.get() == 1:
            pass

        if self.Checkbutton4.get() == 1:
            path = self.path_value.get()
            path_save = filedialog.askdirectory()
            self.Progressbar()
            im = Image.open(path)
            im.save(f"{path_save}/hello.tiff", 'TIFF')
            box_image()
        if self.Checkbutton5.get() == 1:
            path = self.path_value.get()
            path_save = filedialog.askdirectory()
            self.Progressbar()
            img = Image.open(path)
            ary = np.array(img)

            r,g,b = np.split(ary,3,axis=2)
            r=r.reshape(-1)
            g=r.reshape(-1)
            b=r.reshape(-1)

            bitmap = list(map(lambda x: 0.299*x[0]+0.587*x[1]+0.114*x[2], 
            zip(r,g,b)))
            bitmap = np.array(bitmap).reshape([ary.shape[0], ary.shape[1]])
            bitmap = np.dot((bitmap > 128).astype(float),255)
            im = Image.fromarray(bitmap.astype(np.uint8))
            im.save(f'{path_save}/new_image.bmp')
            box_image()
        if self.Checkbutton6.get() == 1:
            pass
    def Options(self):
        if self.Checkbutton7.get() == 1:
            path = self.path_value.get()
            path_save = filedialog.askdirectory()
            self.Progressbar()
            img = cv2.imread(path)
            #img = cv2.resize(img, (720, 720))
            imgBW = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            cv2.imwrite(f'{path_save}/Black&White.png', imgBW)
            box_image()
        if self.Checkbutton8.get() == 1:
            path = self.path_value.get()
            path_save = filedialog.askdirectory()
            self.Progressbar()
            face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
            img = cv2.imread(path)
            #img = cv2.resize(img, (720, 720))
            imgGRAY = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(imgGRAY, 1.3, 5)
            for (x,y,w,h) in faces:
                cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
                roi_gray = imgGRAY[y:y+h, x:x+w]
                roi_color = img[y:y+h, x:x+w]
            cv2.imwrite(f'{path_save}/Face_DN.png', img)
            box_image()
        if self.Checkbutton9.get() == 1:
            path = self.path_value.get()
            path_save = filedialog.askdirectory()
            self.Progressbar()
            face_cascade = cv2.CascadeClassifier('haarcascade_smile.xml')
            img = cv2.imread(path)
            #img = cv2.resize(img, (740, 740))
            imgGRAY = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(imgGRAY, 1.3, 5)
            for (x,y,w,h) in faces:
                cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
                roi_gray = imgGRAY[y:y+h, x:x+w]
                roi_color = img[y:y+h, x:x+w]
            cv2.imwrite(f'{path_save}/Smile.png', img)
            box_image()
            #cv2.imshow('2', imgGRAY)
                   
    def run(self):
        self.app.mainloop()

if __name__ == "__main__":
    calc = GUI()
    calc.run()