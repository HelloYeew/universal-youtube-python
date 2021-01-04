import subprocess
import sys
import urllib.request

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

    # check google api python client
    print("Checking Google API Python Client...")
    try:
        import googleapiclient
    except ImportError:
        print("Google API Python Client not found.")
        print("Run install command : pip install --upgrade google-api-python-client")
        subprocess.check_call([sys.executable, "-m", "pip", "install", '--upgrade', 'google-api-python-client'])
        print("Google API Python Client install complete!")
    finally:
        import googleapiclient

    # check google oauth
    print("Checking Google Oauth Library...")
    try:
        import google_auth_oauthlib
    except ImportError:
        print("wget not found.")
        print("Run install command : pip install --upgrade google-auth-oauthlib google-auth-httplib2")
        subprocess.check_call([sys.executable, "-m", "pip", "install", '--upgrade', 'google-auth-oauthlib', 'google-auth-httplib2'])
        print("Google Oauth Library Client install complete!")
    finally:
        import google_auth_oauthlib

    print("Checking complete!")

def check_internet(url='http://www.youtube.com', timeout=3):
    try:
        urllib.request.urlopen(url, timeout=timeout)
        return True
    except Exception as e:
        print(e)
        return False
