import sys
from check import *
from for_dev import *
import getpass

print("Booting program...")
print()

# check internet connection
print("Checking internet connection with YouTube...")
connection = check_internet()
if connection == True:
    print("Connection complete!")
else:
    print("Connection failed! Please check your internet connection or YouTube status.")
    sys.exit()
print()

# check requirement
check_library()
print()
print("Checking directory...")
print(f"Current directory: {check_dir()}")
print()

# menu function
from function import *

# turn on and turn off dev mode here
dev = True

# Main Menu
while True:
    print("--Main menu--")
    print(f"Hi! {getpass.getuser()}. What you want to do?")
    print("1.Fetch Video Data")
    print("2.Download Video Thumbnail")
    print("3.Download Video as mp4")
    print("0.exit")
    menu = input("Press number from menu to continue : ")
    if menu.isnumeric():
        menu = int(menu)
        if menu == 1:
            url = input("Please enter YouTube URL here: ")
            print()
            try:
                fetch_data(url)
            except Exception as ex:
                print(f"Error : {ex}")
                print(f"Please check your YouTube URL again!")
                print()
        elif menu == 2:
            url = input("Please enter YouTube URL here: ")
            print()
            try:
                download_thumbnail(url)
            except Exception as ex:
                print(f"Error : {ex}")
                print(f"Please check your YouTube URL again!")
                print()
        elif menu == 3:
            url = input("Please enter YouTube URL here: ")
            print()
            try:
                download_mp4(url)
            except Exception as ex:
                print(f"Error : {ex}")
                print(f"Please check your YouTube URL again!")
                print()
        elif menu == 0:
            print("Bye!")
            sys.exit()
        else:
            print("Incorrect input")
            print()
    else:
        print("Incorrect input")
        print()
