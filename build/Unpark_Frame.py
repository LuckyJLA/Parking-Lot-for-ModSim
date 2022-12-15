
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from BackEnd_LotStatus import button_color
from BackEnd_parkunpark import go_unpark
import datetime as dt


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\alama\OneDrive\Desktop\Figma to Python 3.0\build\assets\frame1")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


'''window = Tk()

window.geometry("1366x768")
window.configure(bg = "#000000")'''

def unpark_frame(window):
    canvas = Canvas(
        window,
        bg = "#000000",
        height = 768,
        width = 1366,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    def menu_command(choice):
        match choice:
            case 'a':
                go_unpark(parklotnum.get(),timenow.get())
                from MainMenu_Frame import mainmenu
                mainmenu(window)
            case 'b':
                from MainMenu_Frame import mainmenu
                mainmenu(window)

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

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    cancel_button = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: menu_command('b'),
        relief="flat"
    )
    cancel_button.place(
        x=1139.0,
        y=682.0,
        width=122.0,
        height=41.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    unpark_button = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: menu_command('a'),
        relief="flat"
    )
    unpark_button.place(
        x=1139.0,
        y=605.0,
        width=122.0,
        height=43.0
    )

    image_image_4 = PhotoImage(
        file=relative_to_assets("image_4.png"))
    image_4 = canvas.create_image(
        1199.0,
        336.0,
        image=image_image_4
    )

    image_image_5 = PhotoImage(
        file=relative_to_assets("image_5.png"))
    image_5 = canvas.create_image(
        1201.0,
        204.0,
        image=image_image_5
    )

    ### fills the textbox
    def new_info(new_lot):
        new_time = dt.datetime.now()
        parklotnum.delete(0, 'end')
        timenow.delete(0, 'end')

        timenow.insert(0, new_time)
        parklotnum.insert(0, new_lot)

    entry_image_1 = PhotoImage(
        file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(
        1200.0,
        370.0,
        image=entry_image_1
    )
    parklotnum = Entry(canvas, font="Arial 20",
        bd=0,
        bg="#D9D9D9",
        fg="Blue",
        highlightthickness=0,
        justify='center'
    )
    parklotnum.place(
        x=1092.0,
        y=343.0,
        width=216.0,
        height=52.0
    )

    entry_image_2 = PhotoImage(
        file=relative_to_assets("entry_2.png"))
    entry_bg_2 = canvas.create_image(
        1200.0,
        498.0,
        image=entry_image_2
    )
    timenow = Entry(canvas, font="Arial 17",
        bd=0,
        bg="#D9D9D9",
        fg="Red",
        highlightthickness=0,
        justify='center'
    )
    timenow.place(
        x=1092.0,
        y=471.0,
        width=216.0,
        height=52.0
    )

    canvas.create_text(
        1093.0,
        310.0,
        anchor="nw",
        text="Parking Lot Number",
        fill="#000000",
        font=("Inter ExtraBold", 20 * -1)
    )

    canvas.create_text(
        1093.0,
        438.0,
        anchor="nw",
        text="Timestamp",
        fill="#000000",
        font=("Inter ExtraBold", 20 * -1)
    )


    ###BUTTONS

    button_1 = Button(canvas,
            text='305', 
            font= ('Arial 40'), 
            background=button_color(305),
            command=lambda: new_info(305),
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
        command=lambda: new_info(304),
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
            command=lambda: new_info(303),
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
            command=lambda: new_info(302),
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
        command=lambda: new_info(301),
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
        command=lambda: new_info(205),
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
        command=lambda: new_info(204),
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
        command=lambda: new_info(203),
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
        command=lambda: new_info(202),
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
        command=lambda: new_info(201),
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
        command=lambda: new_info(105),
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
        command=lambda: new_info(104),
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
        command=lambda: new_info(103),
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
        command=lambda: new_info(102),
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
        command=lambda: new_info(101),
        relief="flat"
    )
    button_15.place(
        x=49.0,
        y=116.0,
        width=237.0,
        height=96.0
    )

    window.resizable(True, True)
    window.mainloop()

'''unpark_frame(window)'''