from pytube import YouTube
import urllib.request
import os
import wget

def fetch_data(url):
    print("Fetching data...")
    clip = YouTube(url)
    clip.prefetch()
    print(f"Title : {clip.title}")
    print(f"Length : {clip.length} seconds")
    print(f"Views : {clip.views}")
    print(f"Author : {clip.author}")
    print(f"Rating : {clip.rating}")
    print(f"Thumbnail URL : {clip.thumbnail_url}")
    if len(clip.caption_tracks) == 0:
        print("Available Captions : No caption available")
    else:
        print(f"Available Captions : {len(clip.caption_tracks)} languages include")
        for i in range(len(clip.caption_tracks)):
            print(f"{i+1}.{clip.caption_tracks[i]}")
    print(f"Description :")
    print(clip.description)
    print()
    print("Complete!")
    print()
    command = input("Do you want to download thumbnail?(y/n) : ")
    if command == "y":
        print("Start downloading thumbnail...")
        urllib.request.urlretrieve(clip.thumbnail_url, f"{os.getcwd()}/thumbnail.jpg")
        print("Download complete!")
        print(f"File directory : {os.getcwd()}/thumbnail.jpg")
        print()
    else:
        print()


def download_thumbnail(url):
    print("Fetching data...")
    clip = YouTube(url)
    print("Start downloading thumbnail...")
    urllib.request.urlretrieve(clip.thumbnail_url, f"{os.getcwd()}/thumbnail.jpg")
    print("Download complete!")
    print(f"File directory : {os.getcwd()}/thumbnail.jpg")
    print()