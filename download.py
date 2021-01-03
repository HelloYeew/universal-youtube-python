from pytube import YouTube
yt_url = "https://www.youtube.com/watch?v=sAuEeM_6zpk"
yt_obj = YouTube(yt_url)

# fetch resolution
print("Fetch Resolution")
for stream in yt_obj.streams:
    print(stream)
print()

# filter data
print("Filter data")
filters = yt_obj.streams.filter(progressive=True, file_extension='mp4')
for mp4_filter in filters:
    print(mp4_filter)

# Download video
filters.get_highest_resolution().download()
