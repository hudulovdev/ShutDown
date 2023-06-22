import os

def shutdown_computer():
    answer=input("(y)es or (n)o")
    if answer=="y":
        os.system("taskkill /f /im *")
        os.system("shutdown /s /t 0")
    else:
        exit()

shutdown_computer()
