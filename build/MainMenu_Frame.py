
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from BackEnd_LotStatus import button_color
from Park_Frame import park_frame


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\alama\OneDrive\Desktop\Figma to Python 3.0\build\assets\frame3")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

window = Tk()

window.geometry("1366x768")
window.configure(bg = "#000000")  

def mainmenu(window):
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
    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        1200.0,
        426.0,
        image=image_image_1
    )

    image_image_2 = PhotoImage(
        file=relative_to_assets("image_2.png"))
    image_2 = canvas.create_image(
        517.0,
        426.0,
        image=image_image_2
    )

    button_1 = Button(canvas,
            text='305', 
            font= ('Arial 40'), 
            background=button_color(305),
            command=lambda: print("button_1 clicked"),
            relief="flat"
        )
    button_1.place(
        x=748.0,
        y=640.0,
        width=237.0,
        height=96.0
    )


    button_2 = Button(canvas,
        text='304', 
        font= ('Arial 40'), 
        background=button_color(304),
        command=lambda: print("button_2 clicked"),
        relief="flat"
    )
    button_2.place(
        x=748.0,
        y=509.0,
        width=237.0,
        height=96.0
    )


    button_3 = Button(canvas,
            text='303', 
            font= ('Arial 40'), 
            background=button_color(303),
            command=lambda: print("button_3 clicked"),
            relief="flat"
        )
    button_3.place(
        x=748.0,
        y=378.0,
        width=237.0,
        height=96.0
    )


    button_4 = Button(canvas,
            text='302', 
            font= ('Arial 40'), 
            background=button_color(302),
            command=lambda: print("button_4 clicked"),
            relief="flat"
        )
    button_4.place(
        x=748.0,
        y=247.0,
        width=237.0,
        height=96.0
    )


    button_5 = Button(canvas,
        text='301', 
        font= ('Arial 40'), 
        background=button_color(301),
        command=lambda: print("button_5 clicked"),
        relief="flat"
    )
    button_5.place(
        x=748.0,
        y=116.0,
        width=237.0,
        height=96.0
    )


    button_6 = Button(canvas,
        text='205', 
        font= ('Arial 40'), 
        background=button_color(205),
        command=lambda: print("button_6 clicked"),
        relief="flat"
    )
    button_6.place(
        x=398.0,
        y=640.0,
        width=237.0,
        height=96.0
    )


    button_7 = Button(canvas,
        text='204', 
        font= ('Arial 40'), 
        background=button_color(204),
        command=lambda: print("button_7 clicked"),
        relief="flat"
    )
    button_7.place(
        x=398.0,
        y=509.0,
        width=237.0,
        height=96.0
    )


    button_8 = Button(canvas,
        text='203', 
        font= ('Arial 40'), 
        background=button_color(203),
        command=lambda: print("button_8 clicked"),
        relief="flat"
    )
    button_8.place(
        x=398.0,
        y=378.0,
        width=237.0,
        height=96.0
    )


    button_9 = Button(canvas,
        text='202', 
        font= ('Arial 40'), 
        background=button_color(202),
        command=lambda: print("button_9 clicked"),
        relief="flat"
    )
    button_9.place(
        x=398.0,
        y=247.0,
        width=237.0,
        height=96.0
    )


    button_10 = Button(canvas,
        text='201', 
        font= ('Arial 40'), 
        background=button_color(201),
        command=lambda: print("button_10 clicked"),
        relief="flat"
    )
    button_10.place(
        x=398.0,
        y=116.0,
        width=237.0,
        height=96.0
    )


    button_11 = Button(canvas,
        text='105', 
        font= ('Arial 40'), 
        background=button_color(105),
        command=lambda: print("button_11 clicked"),
        relief="flat"
    )
    button_11.place(
        x=49.0,
        y=640.0,
        width=237.0,
        height=96.0
    )


    button_12 = Button(canvas,
        text='104', 
        font= ('Arial 40'), 
        background=button_color(104),
        command=lambda: print("button_12 clicked"),
        relief="flat"
        )
    button_12.place(
        x=49.0,
        y=509.0,
        width=237.0,
        height=96.0
    )


    button_13 = Button(canvas,
        text='103', 
        font= ('Arial 40'), 
        background=button_color(103),
        command=lambda: print("button_13 clicked"),
        relief="flat"
    )
    button_13.place(
        x=49.0,
        y=378.0,
        width=237.0,
        height=96.0
    )

    button_14 = Button(canvas,
        text='102', 
        font= ('Arial 40'), 
        background=button_color(102),
        command=lambda: print("button_14 clicked"),
        relief="flat"
    )
    button_14.place(
        x=49.0,
        y=247.0,
        width=237.0,
        height=96.0
    )


    button_15 = Button(canvas,
        text='101', 
        font= ('Arial 40'), 
        background=button_color(101),
        command=lambda: print("button_15 clicked"),
        relief="flat"
    )
    button_15.place(
        x=49.0,
        y=116.0,
        width=237.0,
        height=96.0
    )



    image_image_3 = PhotoImage(
        file=relative_to_assets("image_3.png"))
    image_3 = canvas.create_image(
        52.0,
        38.0,
        image=image_image_3
    )

    def menu_commands(choice):
        match choice:
            case 'a':
                from Park_Frame import park_frame
                park_frame(window)
            case 'b':
                from Unpark_Frame import unpark_frame
                unpark_frame(window)
            case 'c':
                from Logs_Frame import log_frame
                log_frame(window)
            case 'd':
                from Login_Frame import login_frame
                login_frame(window)


    #Logout
    button_image_16 = PhotoImage(
        file=relative_to_assets("button_16.png"))
    button_16 = Button(canvas,
        image=button_image_16,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: menu_commands('d'),
        relief="flat"
    )
    button_16.place(
        x=1094.0,
        y=612.0,
        width=211.0,
        height=86.0
    )


    #Logs
    button_image_17 = PhotoImage(
        file=relative_to_assets("button_17.png"))
    button_17 = Button(canvas,
        image=button_image_17,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: menu_commands('c'),
        relief="flat"
    )
    button_17.place(
        x=1094.0,
        y=476.0,
        width=211.0,
        height=86.0
    )


    #Unpark
    button_image_18 = PhotoImage(
        file=relative_to_assets("button_18.png"))
    button_18 = Button(canvas,
        image=button_image_18,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: menu_commands('b'),
        relief="flat"
    )
    button_18.place(
        x=1094.0,
        y=340.0,
        width=211.0,
        height=86.0
    )

    #Park
    button_image_19 = PhotoImage(
        file=relative_to_assets("button_19.png"))
    button_19 = Button(canvas,
        image=button_image_19,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: menu_commands('a'),
        relief="flat"
    )
    button_19.place(
        x=1094.0,
        y=204.0,
        width=211.0,
        height=86.0
    )

    canvas.create_text(
        1081.0,
        125.0,
        anchor="nw",
        text="MAIN MENU",
        fill="#FFFFFF",
        font=("Inter ExtraBold", 40 * -1)
    )
    window.resizable(False, False)
    window.mainloop()


mainmenu(window)