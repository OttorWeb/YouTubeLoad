from pytube import YouTube, Playlist
import time

# https://www.gogleapis.com/youtube/v3/search?key=AIzaSyDXhF1gPiuYdeQc-aBLbtAggYwRFZDSjg8&channelId=UCxGELV31d5e-llwFHiL0zIA&maxResults=50
# Ссылка со списком видео нас странице канала

channel = "https://www.youtube.com/channel/UCxGELV31d5e-llwFHiL0zIA/videos"
link = "https://www.youtube.com/watch?v=oqUqdyMRP-E"

link = "https://youtube.com/watch?v=aGMNgLLcZWk"

# загрузка конкретоного видео
def download_video(link):
    yt = YouTube(link)
    print("Title:", yt.title) # Заголовок видео
    print("Views:", yt.views) # Количесво просмотров
    print("date:", yt.publish_date) # Дата публикации видео
    print("length:", time.strftime("%H:%M:%S", time.gmtime(yt.length))) # Продолжительность видео
    # print("Cap:", yt.channel_id) # ID канала
    # Список всех вариантов качества видео + тут можно забрать отдельно дорожку звука
    # print("Streams: ", yt.streams)

    # Выбираем максимальное разрешение с progressive="True"
    # print("highest: ", yt.streams.get_highest_resolution())

    # Загружаем видео в папку videos
    yt.streams.get_highest_resolution().download("videos")

# Вызываем функцию загрзки конкретного видео
#download_video(link)

link = "https://www.youtube.com/playlist?list=PLe-iIMbo5JOK17gsY2dEi90RP5fLemd9U"

def download_playlist(link):
     playlist = Playlist(link)
     for video in playlist.videos:
         video_file = video.title
         print("#T1:", video.title, "T2:", video_file, "T3:", video.watch_url)
         video_file = video_file.replace('.', '')
         video_file = video_file.replace('#', '')
         video_file = video_file.replace('|', '')
         video_file = "./videos/" + video_file + ".mp4"
         print("T2: ", video_file)
         try:
             file = open(video_file)
         except IOError as e:
             #print('T3: --NO --')
             try:
                 video.streams.get_highest_resolution().download("videos")
             except:
                 print("T3: --Удаляем файл --", video_file)
         else:
             with file:
                 print('T3: --Пропускаем --')

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