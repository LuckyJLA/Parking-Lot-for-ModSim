from MainMenu_Frame import mainmenu

def logging_in(username, password):

    print(username)
    print(password)

    if (username == 'admin'):
        if (password == 'Password'):
            print("You successfully logged in")
            return True

        else:
            check = 1
    else:
        check = 1
    

    if(check == 1):
        print("\nIncorrect Username/Password")
        print("Try Again: ")
        return
    

    return check
