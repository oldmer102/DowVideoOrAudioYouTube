from  os import makedirs
from pytube import YouTube
from pytube.helpers import safe_filename

def dowload_video(url,itag=None, audio_only=False, output_path=None,
                           filename=None, filename_prefix=None,
                           proxies=None, progress_callback=None):
    if output_path:
        makedirs(output_path, exist_ok=True)
    if 'http' not in url:
        url = 'https://www.youtube.com/watch?v=%s' % url
    if proxies:
        video = YouTube(url, proxies=proxies)
    else:
        video  = YouTube(url)
    if progress_callback:
        video.register_on_progress_callback(progress_callback)
    if itag:
        itag = int(itag)
        stream = video.streams.get_by_itag(itag)
    else:
        stream = video.streams.filter(only_audio = audio_only).first()
        print('Начинаем: %s' % video.title)
    if filename:
        filename = safe_filename(filename)
    stream.download(output_path=output_path, filename=filename)
    file_type = '.' + stream.mime_type.split('/')[1]
    filename = stream.default_filename if filename is None else filename + file_type
    print('Скачивание завершено. Файл %s' %filename)
    return filename
