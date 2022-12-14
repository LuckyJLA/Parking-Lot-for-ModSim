
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from tkinter import *
import tkinter.ttk as ttk
import tkinter.font as tkfont
import csv


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\alama\OneDrive\Desktop\Figma to Python 3.0\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def log_frame(window):
    
    
    canvas = Canvas(
        window,
        bg = "#000000",
        height = 768,
        width = 1366,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    def menu_commands(choice):
        match choice:
            case 'a': 
                from MainMenu_Frame import mainmenu
                Tframe.destroy()
                mainmenu(window)
            case 'b':
                from Park_Frame import park_frame
                Tframe.destroy()
                park_frame(window)
            case 'c':
                from Unpark_Frame import unpark_frame
                Tframe.destroy()
                unpark_frame(window)
            case 'd':
                from Login_Frame import login_frame
                Tframe.destroy()
                login_frame(window)

    canvas.place(x = 0, y = 0)
    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        1200.0,
        426.0,
        image=image_image_1
    )

    canvas.create_text(
        1081.0,
        125.0,
        anchor="nw",
        text="LOGS MENU",
        fill="#FFFFFF",
        font=("Inter ExtraBold", 40 * -1)
    )


    ###LOGOUT
    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: menu_commands('d'),
        relief="flat"
    )
    button_1.place(
        x=1094.0,
        y=612.0,
        width=211.0,
        height=86.0
    )


    ###UNPARK
    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: menu_commands('c'),
        relief="flat"
    )
    button_2.place(
        x=1094.0,
        y=476.0,
        width=211.0,
        height=86.0
    )


    ###PARK
    button_image_3 = PhotoImage(
        file=relative_to_assets("button_3.png"))
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: menu_commands('b'),
        relief="flat"
    )
    button_3.place(
        x=1094.0,
        y=340.0,
        width=211.0,
        height=86.0
    )


    ###HOME
    button_image_4 = PhotoImage(
        file=relative_to_assets("button_4.png"))
    button_4 = Button(
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: menu_commands('a'),
        relief="flat"
    )
    button_4.place(
        x=1094.0,
        y=204.0,
        width=211.0,
        height=86.0
    )

    image_image_2 = PhotoImage(
        file=relative_to_assets("image_2.png"))
    image_2 = canvas.create_image(
        52.0,
        38.0,
        image=image_image_2
    )

    ###Logs Table
    Tframe = Frame(window, height=684, width=1034)
    Tframe.pack(padx=0,pady=84,side=LEFT)

    #scroll bar
    table_scroll = Scrollbar(Tframe)
    table_scroll.pack(side=RIGHT, fill=Y)

    table = ttk.Treeview(Tframe, yscrollcommand=table_scroll.set)
    table.config(height=684)
    table.pack()

    #config scroll bar
    table_scroll.config(command=table.yview)

    style = ttk.Style()
    style.configure("Treeview.Heading", font=('Arial', 20))
    style.configure("Treeview", font=('Arial 20'))
    style.configure("Treeview", background='White', rowheight = 50)

    #defining table colums
    table['columns'] = ("Timestamp","Lot Number", "Parking", "Counter")
    table.column('#0', minwidth=0, width=0)
    table.column('Timestamp', minwidth=0, width=410)
    table.column('Lot Number', minwidth=0, width=210, anchor=CENTER)
    table.column('Parking', minwidth=0, width=200, anchor=CENTER)
    table.column('Counter', minwidth=0, width=200, anchor=CENTER)

    #Create headings
    table.heading('Timestamp', text="Time Stamp", anchor=W)
    table.heading('Lot Number', text="Lot Number", anchor=CENTER)
    table.heading('Parking', text="Parking", anchor=CENTER)
    table.heading('Counter', text="Counter", anchor=CENTER)

    with open('C:\\Users\\alama\\OneDrive\\Desktop\\ModSim Parking\\ParkingLogs.csv') as f:
        reader = csv.DictReader(f, delimiter=',')
        for row in reader:
            timestamp = row['timestamp']
            lot_num = row['lot_num']
            in_out = row['in_out']
            parked_counter = row['parked_counter']
            table.insert("", 0, values=(timestamp, lot_num, in_out, parked_counter))

    
    window.resizable(False, False)
    window.mainloop()


'''window = Tk()

window.geometry("1366x768")
window.configure(bg = "#000000")

log_frame(window)'''