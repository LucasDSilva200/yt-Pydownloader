#!/usr/bin/env python

import logging
import os
import threading
import concurrent.futures
from pytube import YouTube, Playlist
from time import sleep


print_lock = threading.Lock()

def download(link, path_to_save, itag):
    yt = YouTube(link)
    stream = yt.streams.get_by_itag(itag)
    print(f">>>>Downloading....\n{yt.title}<<<<")
    sleep(2)
    if itag == 22:
        stream.download(f'{path_to_save}/youtube/videos')
    else:
        music = stream.download(f'{path_to_save}/youtube/musics/')

        base, _ = os.path.splitext(music)
        new_file = base + '.mp3'
        os.rename(music, new_file)
    print(">>>>Download completed<<<<")

def multi_download(video,path,name_playlist,itag):
    if itag == 22:
        print(f"Baixando o video {video.title}")
        video.streams.get_by_itag(itag).download(f'{path}/youtube/{name_playlist}/')
    else:
        print(f"Baixando a música {video.title}")
        music = video.streams.get_by_itag(itag).download(
                    f'{path}/youtube/{name_playlist}/')

        base, _ = os.path.splitext(music)
        new_file = base + '.mp3'
        os.rename(music, new_file)

def download_playlist(link, path_to_save, itag, workers):
    try:
        pl = Playlist(link)
        name_playlist = pl.title

        with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as executor:
            for video in pl.videos:
                executor.submit(multi_download, video,path_to_save,name_playlist,itag)

    except KeyError:
        print("Erro, provalvelmente a playlist é privada...")
    except Exception as e:
        logging.exception(e)
