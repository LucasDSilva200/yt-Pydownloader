#!/usr/bin/env python

import logging
import os
import threading
import concurrent.futures
from pytube import YouTube, Playlist
from time import sleep

from src.convert_to_mp3 import convert_to_mp3


print_lock = threading.Lock()

def download(link, path_to_save, itag):
    yt = YouTube(link)
    name = yt.title
    print(f">>>>Downloading....\n{name}<<<<")
    sleep(2)
    if itag == 22:
        stream = yt.streams.get_highest_resolution()
        stream.download(f'{path_to_save}/youtube/videos')
    else:
        convert_to_mp3(yt=yt,name=name,filepath=path_to_save)
    print(">>>>Download completed<<<<")

def multi_download(video,path,name_playlist,itag):
    if itag == 22:
        print(f"Baixando o video {video.title}")
        video.streams.get_by_itag(itag).download(f'{path}/youtube/{name_playlist}/')
    else:
        print(f"Baixando a música {video.title}")
        convert_to_mp3(name=video.title, yt=video, filepath=path)

def download_playlist(link, path_to_save, itag, workers):
    try:
        pl = Playlist(link)
        name_playlist = pl.title
        if itag == 22:
            with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as executor:
                for video in pl.videos:
                    executor.submit(multi_download, video,path_to_save,name_playlist,itag)
        else:
            for video in pl.videos:
                multi_download(video=video,path=path_to_save,name_playlist=name_playlist,itag=itag)
    except KeyError:
        print("Erro, provalvelmente a playlist é privada...")
    except Exception as e:
        logging.exception(e)
