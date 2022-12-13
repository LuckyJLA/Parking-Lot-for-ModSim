from tkinter import *

def main():
    window = Tk()

    window.geometry("1366x768")
    window.configure(bg = "#000000")
    from Login_Frame import login_frame

    login_frame(window)

main()