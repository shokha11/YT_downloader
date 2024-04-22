from pytube import YouTube

video_url = str(input(""))

ytb = YouTube(video_url)

video_format = ytb.streams.get_highest_resolution()
video_file = video_format.download("YT_Video.mp4")

print(f"Видео скачано: {video_file}")