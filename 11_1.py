import random
from pytube import YouTube
import moviepy.editor as mp

# Запрашиваем ссылку на видео
url = input("Введите ссылку на видео: ")

# Загружаем видео
yt = YouTube(url)
stream = yt.streams.filter(progressive=True).first()
stream.download()

# Получаем путь к загруженному видео
video_path = stream.default_filename

# Выбираем случайный промежуток времени (от 10 до 30 секунд)
start_time = random.randint(10, 30)
end_time = start_time + 10

# Вырезаем фрагмент из видео
clip = mp.VideoFileClip(video_path).subclip(start_time, end_time)
clip.preview()
