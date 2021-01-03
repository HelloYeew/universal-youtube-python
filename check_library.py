import subprocess
import sys

def check_library():
    print("Start checking important library to run a program...")

    # check tkinter
    print("Checking tkinter...")
    try:
        import tkinter
    except ImportError:
        print("Tkinter not found.")
        print("Run install command : -m pip install tk")
        subprocess.check_call([sys.executable, "-m", "pip", "install", 'tk'])
        print("Tkinter install complete!")
    finally:
        import tkinter

    # check pytube
    print("Checking pytube...")
    try:
        import pytube
    except ImportError:
        print("Pytube not found.")
        print("Run install command : -m pip install pytube")
        subprocess.check_call([sys.executable, "-m", "pip", "install", 'pytube'])
        print("Pytube install complete!")
    finally:
        import pytube

    # check progressbar
    print("Checking progressbar...")
    try:
        import progressbar
    except ImportError:
        print("Progressbar not found.")
        print("Run install command : -m pip install progressbar")
        subprocess.check_call([sys.executable, "-m", "pip", "install", 'progressbar'])
        print("Progressbar install complete!")
    finally:
        import progressbar

    # check tqdm
    print("Checking tqdm...")
    try:
        import tqdm
    except ImportError:
        print("tqdm not found.")
        print("Run install command : -m pip install tqdm")
        subprocess.check_call([sys.executable, "-m", "pip", "install", 'tqdm'])
        print("tqdm install complete!")
    finally:
        import tqdm

    # check wget
    print("Checking wget...")
    try:
        import wget
    except ImportError:
        print("wget not found.")
        print("Run install command : -m pip install wget")
        subprocess.check_call([sys.executable, "-m", "pip", "install", 'wget'])
        print("wget install complete!")
    finally:
        import wget

    print("Checking complete!")
