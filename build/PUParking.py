from tkinter import *

def main():
    window = Tk()
    window.attributes('-fullscreen', True)
    

    ''''window.geometry("1366x768")'''
    w, h = window.winfo_screenwidth(), window.winfo_screenheight()
    window.geometry("%dx%d+0+0" % (w, h))
    window.configure(bg = "#000000")
    from Login_Frame import login_frame
    
    window.resizable(True, True)
    login_frame(window)

main()