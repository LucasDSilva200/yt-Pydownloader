#!/usr/bin/env python

import argparse
from utils.path import change_path, download_folder_search, list_files
from utils.utils import download, download_playlist


PATH_FOR_SAVE_FILE = download_folder_search()


def handling_of_arguments(args):
    if args['Video']:
        download(link=args['Video'], path_to_save=PATH_FOR_SAVE_FILE, itag=22)
    elif args['showpath']:
        print(f'{PATH_FOR_SAVE_FILE}/youtube/')
    elif args['Music']:
        download(link=args['Music'], path_to_save=PATH_FOR_SAVE_FILE, itag=140)
    elif args['Videos']:
        download_playlist(link=args['Videos'],
                          path_to_save=PATH_FOR_SAVE_FILE, itag=22,workers=args['Workers'])
    elif args['Musics']:
        download_playlist(link=args['Musics'],
                          path_to_save=PATH_FOR_SAVE_FILE, itag=140,workers=args['Workers'])
    elif args['changepath']:
        change_path(args['changepath'])
    elif args['list']:
        list_files()


'''
ARGUMENTOS:

Tipo (video ou playlist)
-V para baixar video
-M para baixar musica
--Pv para baixar playlist de video
--Pm para baixar playlist de musica
'''


def main():
    parser = argparse.ArgumentParser(
        description="A tool made to download youtube.")
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-V', '--Video', type=str,
                       help="The link to the video you want to download")
    group.add_argument('-M', '--Music', type=str,
                       help="The link to the music you want to download")
    group.add_argument('--showpath', help='Shows the way the files will be saved',
                       default=False, action='store_true')
    group.add_argument('-ls', '--list', help='Lists all downloaded files.',
                       default=False, action='store_true')
    group.add_argument('-cp', '--changepath',
                       help='Changes the path for downloading the files.')
    group.add_argument('-Pv', '--Videos', type=str,
                       help="The link to the video playlist you want to download.")
    group.add_argument('-Pm', '--Musics', type=str,
                       help="The link to the Playlist of Songs you want to download.")
    parser.add_argument('-W', '--Workers', type=int, default=4,
                        help="Sets the number of workers (Default 4) to download playlists.")
    args = vars(parser.parse_args())

    if not any(args.values()):
        parser.error('No arguments provided.')
    handling_of_arguments(args=args)


if __name__ == '__main__':
    main()
