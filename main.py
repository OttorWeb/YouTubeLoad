from pytube import YouTube, Playlist

# https://www.googleapis.com/youtube/v3/search?key=AIzaSyDXhF1gPiuYdeQc-aBLbtAggYwRFZDSjg8&channelId=UCxGELV31d5e-llwFHiL0zIA&maxResults=50
# Ссылка со списком видео нас странице канала

link = "https://www.youtube.com/watch?v=oqUqdyMRP-E"
channel = "https://www.youtube.com/channel/UCxGELV31d5e-llwFHiL0zIA/videos"

# загрузка конкретоного видео
def download_video(link):
    yt = YouTube(link)
    print("Title:", yt.title) # Заголовок видео
    print("Views:", yt.views) # Количесво просмотров
    print("Cap:", yt.captions)
    print("Cap:", yt.channel_id)
    # Список всех вариантов качества видео + тут можно забрать отдельно дорожку звука
    # print("Streams: ", yt.streams)

    # Выбираем максимальное разрешение с progressive="True"
    # print("highest: ", yt.streams.get_highest_resolution())

    # Загружаем видео в папку videos
    yt.streams.get_highest_resolution().download("videos")

# Вызываем функцию загрзки конкретного видео
# download_video(link)

link = "https://www.youtube.com/playlist?list=PLrHE5fFt2en98iI1dKYjQLx3SgyCIe6bi"

def download_playlist(link):
     playlist = Playlist(link)
     for video in playlist.videos:
         print("T1:", video.title, "T2:", video.watch_url)
         # video.streams.get_highest_resolution().download("videos")

download_playlist(link)

def download():
     link = input("Enter a link: ")
     content_type = input("Type 1 for video 2 for playlist: ")
     if content_type == "1":
         download_video(link)
     elif content_type == "2":
         download_playlist(link)
     else:
         print("Unknown option")

# download()
