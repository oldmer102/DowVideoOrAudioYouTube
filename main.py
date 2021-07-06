from pytube import YouTube
from dow_set import dowload_video


def start():
    while True:
        user = input('Будем качать д/н: ')
        if user.lower() in ['да', 'д']:
            url = input('URL: ')
            form = input('В/а?: ')
            if form.lower() in ['в', 'видео']:
                dowload_video(url, output_path='видео/')

            elif form.lower() in ['а', 'аудио']:
                dowload_video(url, audio_only=True, output_path='аудио/')

        elif user.lower() in ['нет', 'н']:
            print('Пока!')
            exit()

if __name__ == '__main__':
    start()

