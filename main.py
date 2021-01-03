import sys
from check_library import *
from for_dev import *

# check requirement
print("Booting program...")
print()
check_library()
print()
print("Checking directory...")
print(f"Current directory: {check_dir()}")
print()

# menu function
from function import *

# Main Menu
while True:
    print("--Main menu--")
    print("What you want to do?")
    print("1.Fetch Clip Data")
    print("2.Download Thumbnail")
    print("0.exit")
    menu = int(input("Press number from menu to continue : "))
    print()
    if menu == 1:
        url = input("Please enter YouTube URL here: ")
        print()
        try:
            fetch_data(url)
        except:
            print("Error : This is not URL, This URL is not from YouTube or this video is private or not available.")
            print()
    elif menu == 2:
        url = input("Please enter YouTube URL here: ")
        print()
        try:
            download_thumbnail(url)
        except:
            print("Error : This is not URL, This URL is not from YouTube or this video is private or not available.")
            print()
    elif menu == 0:
        print("Bye!")
        sys.exit()
    else:
        print("Incorrect input")
        print("")






