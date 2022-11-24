#bin/user/python3
import os
import time as t
import pyfiglet
import colorama
from colorama import *
colorama.init(autoreset=True)
try:
    import update_check
except:
    os.system("pip install --upgrade pip")
    os.system("pip install update-check")
from update_check import isUpToDate, update
if isUpToDate(__file__,  "https://raw.githubusercontent.com/spider863644/WhatsApp-Crash/main/crash.py") == False:
    print(Fore.YELLOW+ "This version is outdated, will update the tool in a minute")
    t.sleep(3)
    update("wordlist.py",  "https://raw.githubusercontent.com/spider863644/Wordlist-Generator/main/crash.py")
    print(Fore.GREEN + "Updated\nRun tool again")
    exit()
def loop():
    os.system ("clear")
    head = pyfiglet.figlet_format("Wordlist Generator")
    print(Fore.YELLOW + head)
    print (Fore.RED + "Version 1.0".center(70))
    print("""
""")
    print (Fore.CYAN + """
[A] Generate Wordlist
[B] Update program
[C] Join WhatsApp Group
[D] Exit Program
""")
    option = input(Fore.GREEN +  "Enter a valid option: " + Fore.YELLOW).upper().strip()
    os.system("clear")
    if option == "A":
        print(Fore.CYAN + """
[A] Numeric Only
[B] Alphabetic Only
[C] Alphanumeric
""")
        typee = input(Fore.GREEN + " Enter a valid option: " + Fore.YELLOW).upper().strip()
        if typee == "A":
            filename = input (Fore.GREEN + "Create a new file[Enter file name]: ").strip()
            if len(filename) < 3 and len(filename) > 0:
                print(Fore.RED + "File name must be equal to or greater than three characters")
                t.sleep(3)
                loop()
            elif len(filename) == 0:
                print(Fore.RED + " Filename must not be empty")
                t.sleep(3)
                loop()
            print(Fore.YELLOW + "\n\nCreating " + filename + ".txt...  Please wait for five minutes...")
            print (Fore.RED + " NOTE: File size is 848mb")
            file = open(filename + ".txt",  "w")
            for x in range(1000, 100000000):
              v = str(x)
              file.write(v + "\n")
            file.close()
            print(Fore.BLUE + "Wordlist has been created Successfully√ in the current directory")
            t.sleep(1.5)
        
        elif typee == "B":
            print(Fore.RED + "Unavailable")
            t.sleep(2)
            loop()
        elif typee == "C":
            print(Fore.RED + " Unavailable")
            t.sleep(2)
            loop()
        else:
            print(Fore.RED + "INVALID OPTION! ".capitalize())
            t.sleep(3)
            loop()
    elif option == "B":
        print(Fore.GREEN + "UPDATING... ")
        os.system("""
        cd $HOME
        rm -rf Wordlist-Generator
        git clone https://github.com/spider863644/Wordlist-Generator
        """)
        print(Fore.BLUE + """
        Now type the following commands:
        cd $HOME
        cd Wordlist-Generator
        python3 wordlist.py
        """)
        exit() 
    elif option == "C":
        print(Fore.BLUE + "Redirecting to my WhatsApp group")
        t.sleep(2)
        os.system("xdg-open https://chat.whatsapp.com/IWqGOsJPjkp2vXcMSJKYns")
    elif option == "D":
        print(Fore.YELLOW + " THANKS FOR USING MY TOOL\nFOLLOW ME ON GITHUB FOR MORE TOOLS".capitalize())
    else:
        print(Fore.RED + "Invalid option! ") 
        t.sleep(3)
        loop()        
        
    
loop()