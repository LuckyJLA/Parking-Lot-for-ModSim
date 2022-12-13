
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\\Users\\alama\\OneDrive\\Desktop\\Figma to Python 3.0\\build\\assets\\frame4")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

'''window = Tk()

window.geometry("1366x768")
window.configure(bg = "#000000")'''

from BackEnd_Login import logging_in
from MainMenu_Frame import mainmenu

def einz(window, username, password):
    mm = logging_in(username.get(), password.get())
    if mm == True:
        mainmenu(window)
        

def login_frame(window):
    canvas = Canvas(
        window,
        bg = "#000000",
        height = 768,
        width = 1366,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: einz(window, username, password),
        relief="flat"
    )
    button_1.place(
        x=781.0,
        y=616.0,
        width=100.0,
        height=35.0
    )

    entry_image_1 = PhotoImage(
        file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(
        690.0,
        562.0,
        image=entry_image_1
    )
    password = Entry(font='Arial 16',
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0
    )
    password.place(
        x=479.0,
        y=537.0,
        width=422.0,
        height=48.0
    )

    canvas.create_text(
        474.0,
        512.0,
        anchor="nw",
        text="Password",
        fill="#FFFFFF",
        font=("Inter ExtraBold", 16 * -1)
    )

    entry_image_2 = PhotoImage(
        file=relative_to_assets("entry_2.png"))
    entry_bg_2 = canvas.create_image(
        690.0,
        473.0,
        image=entry_image_2
    )
    username = Entry(font='Arial 16',
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0
    )
    username.place(
        x=479.0,
        y=448.0,
        width=422.0,
        height=48.0
    )

    canvas.create_text(
        474.0,
        424.0,
        anchor="nw",
        text="Username",
        fill="#FFFFFF",
        font=("Inter ExtraBold", 16 * -1)
    )


    image_image_2 = PhotoImage(
        file=relative_to_assets("image_2.png"))
    image_2 = canvas.create_image(
        690.0,
        275.0,
        image=image_image_2
    )


    window.resizable(False, False)
    window.mainloop()

'''login_frame(window)'''