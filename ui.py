import customtkinter as ctk
from tkinterdnd2 import DND_FILES
from datetime import datetime
from time import sleep
import os

#Disable title bar
Custom_bar = False

#file type
file_type_strict = "mp3"


def move_win(e):
    root.geometry(f'{e.x_root}+{e.y_root}')

def drop(event):
    file_type = (event.data[1:-1]).split(".")[-1]
    path = (event.data[1:-1]).replace("/","\\")
    file_name = path.split("\\")[-1]
    if file_type in ["mp3","wav","ogg"]:
        try:
            os.system(rf'del "{os.getcwd()}\main.{file_type_strict}"')
            os.system(rf'copy "{path}" "{os.getcwd()}"')
            os.system(rf'ren "{os.getcwd()}\{file_name}" "main.{file_type_strict}"')
            label.configure(text="Sound effect updated!")
        except:
            label.configure(text="There was an error reading the file, please check the file")
    else:
        label.configure(text="Try another file D:")

ctk.set_appearance_mode("system")
def msg(label_name,msg):
    label.configure(text="Copying files...")
ctk.set_default_color_theme("blue")

#Window

windowX,windowY = 700,500

root = ctk.CTk()
root.geometry(f"{windowX}x{windowY}")
root.title("Mech Key Sound")
root.columnconfigure((0,1,2),weight=1)
root.rowconfigure((0,1,2),weight=1)
if Custom_bar:
    root.overrideredirect(True)

#Custom title bar
if Custom_bar:
    custom_title_bar = ctk.CTkFrame(master=root,corner_radius=20,height=30,width=9999)
    hide_top_corner = ctk.CTkFrame(master=root,height=10,width=9999)
    custom_title_bar.columnconfigure((0,1,2,3,4,5,6,7,8,9,10),weight=1)
    custom_title_bar.rowconfigure(0,weight=1)
    exit_button = ctk.CTkLabel(master=custom_title_bar,text="x",font=("Century Gothic",20))

#Main
div = ctk.CTkFrame(master=root,corner_radius=50)
div.rowconfigure((0,1,2),weight=1)
div.columnconfigure(0,weight=1)
label = ctk.CTkLabel(master=div,text="Drag and drop sound file here",font=("Century Gothic",20),wraplength=400)
drop_zone = ctk.CTkFrame(master=div,corner_radius=20,height=70)


#Packing
label.grid(row=1,column=0)
div.grid(row=1,column=1,sticky="news")
if Custom_bar:
    hide_top_corner.grid(row=0,column=1,sticky="n") 
    exit_button.grid(row=0,column=10)
    custom_title_bar.grid(row=0,column=1,sticky="n")


#Drag and drop system
div.drop_target_register(DND_FILES)

#Binds
div.dnd_bind("<<Drop>>",drop)
if Custom_bar:
    custom_title_bar.bind("<B1-Motion>",move_win)
    hide_top_corner.bind("<B1-Motion>",move_win)


#Loop
root.mainloop()