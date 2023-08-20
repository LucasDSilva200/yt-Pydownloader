import requests
import os
import tempfile
from PIL import Image
import moviepy.editor as mp
from mutagen.id3 import ID3, APIC, TPE1, TALB


def convert_to_mp3(yt, name, filepath, album):
    stream = yt.streams.get_highest_resolution()
    stream.download(os.path.join(tempfile.gettempdir()),
                    filename=f"{name}.mp4")
    video_path = os.path.join(tempfile.gettempdir(), f"{name}.mp4")
    banner_url = yt.thumbnail_url
    banner_file = requests.get(banner_url).content
    temp_banner = os.path.join(tempfile.gettempdir(), f"{name}.jpg")
    with open(temp_banner, "wb") as f:
        f.write(banner_file)
    banner = Image.open(temp_banner)
    banner = banner.resize((1280, 720))

    # Open the audio file
    audio_path = f"{filepath}/youtube/musics/{name}.mp3"
    clip = mp.AudioFileClip(video_path)
    clip.write_audiofile(audio_path)

    # Add the image as a tag APIC to the audio file
    audio = ID3(audio_path)
    with open(temp_banner, "rb") as f:
        image_data = f.read()
    audio.add(APIC(encoding=3, mime='image/png',
              type=3, desc=u'Cover', data=image_data))

    # Add o autor com a tag APIC
    audio.add(TPE1(encoding=3, text=yt.author))

    # Adicione o nome da playlist como tag TALB
    audio.add(TALB(encoding=3, text=album))

    # Salva o arquivo
    audio.save()

    # exclui o arquivo
    os.unlink(temp_banner)
    os.unlink(video_path)
