#!/usr/bin/env python

from pytube import YouTube, Playlist, exceptions
from time import sleep

from src.convert_to_mp3 import convert_to_mp3


def download(link, path_to_save, itag):
    try:
        yt = YouTube(link, use_oauth=True, allow_oauth_cache=True)
        name = yt.title
        if "|" in name:
            name = name.replace("|", "")
        if "/" in name:
            name = name.replace("/", "")
        if "-" in name:
            name = name.replace("-", "")
        print(f">>>>Downloading....\n{name}<<<<")
        sleep(2)
        if itag == 22:
            stream = yt.streams.get_highest_resolution()
            stream.download(f'{path_to_save}/youtube/videos')
        else:
            convert_to_mp3(yt=yt, name=name,
                           filepath=path_to_save, album=yt.author)
        print(">>>>Download completed<<<<")
    except exceptions.PytubeError:
        download(link=link, path_to_save=path_to_save, itag=itag)


def multi_download(video, path, name_playlist, itag):
    try:
        if itag == 22:

            yt = YouTube(video, use_oauth=True, allow_oauth_cache=True)
            print(f"Baixando o video {yt.title}")
            stream = yt.streams.get_highest_resolution()
            stream.download(
                f'{path}/youtube/{name_playlist}/')
        else:
            print(f"Baixando a música {video.title}")
            convert_to_mp3(name=video.title, yt=video,
                           filepath=path, album=video.author)
    except exceptions.PytubeError:
        return
        multi_download(video=video, path=path,
                       name_playlist=name_playlist, itag=itag)


def download_playlist(link, path_to_save, itag):
    try:
        pl = Playlist(link)
        name_playlist = pl.title
        print(name_playlist)
        if itag == 22:
            for video in pl.videos:
                multi_download(video.watch_url,
                               path_to_save, name_playlist, itag)
        else:
            for video in pl.videos:
                multi_download(video=video, path=path_to_save,
                               name_playlist=name_playlist, itag=itag)
    except KeyError:
        print("Erro, provalvelmente a playlist é privada...")

    except Exception as e:
        print(e)
