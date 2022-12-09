# yt-Pydownloader
A CLI program that downloads videos from YouTube and can convert them to .mp3 music.


usage: main.py [-h] [-V VIDEO | -M MUSIC | --showpath | -ls | -cp CHANGEPATH | -Pv VIDEOS | -Pm MUSICS]                                                         

options:
  -h, --help            show this help message and exit\n
  -V VIDEO, --Video VIDEO\n
                        The link to the video you want to download\n
  -M MUSIC, --Music MUSIC\n
                        The link to the music you want to download\n
  --showpath\n            Shows the way the files will be saved\n
  -ls, --list\n           Lists all downloaded files.\n
  -cp CHANGEPATH, --changepath CHANGEPATH\n
                        Changes the path for downloading the files.\n
  -Pv VIDEOS, --Videos VIDEOS\n
                        The link to the video playlist you want to download.\n
  -Pm MUSICS, --Musics MUSICS\n
                        The link to the Playlist of Songs you want to download.\n
  -W WORKERS, --Workers WORKERS\n
                        Sets the number of workers (Default 4) to download playlists.