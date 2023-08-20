#!/usr/bin/env python

import os
from src.detectos import detect


def download_folder_search():
    try:
        file = open("path_for_download.txt")
        path = file.readline()
        file.close()
        return path
    except FileNotFoundError:
        path = detect()
        path = f"{path}/Downloads"
        with open("path_for_download.txt", 'w+') as file:
            file.write(path)
        return path


def list_files():
    path = download_folder_search()
    path = f'{path}/youtube'
    for _, _, files in os.walk(path):
        for file in files:
            print(file)


def change_path(path):
    operational_system = detect()
    if '~' in path:
        path = path.replace('~', f'{operational_system}')
        print(path)

    with open("path_for_download.txt", 'w+') as file:
        file.write(f'{path}')
    print("O caminho foi mudado com sucesso")


def Arrive_if_the_path_exists():
    path = detect()+"/Downloads"
    path_for_download_file = "path_for_download.txt"
    download_dir = os.path.join(
        os.path.expanduser("~"), "Downloads", "youtube")
    videos_dir = os.path.join(download_dir, "videos")
    musics_dir = os.path.join(download_dir, "musics")

    try:
        with open(path_for_download_file, 'r') as file:
            line = file.readline().strip()

        if not os.path.exists(download_dir):
            os.makedirs(download_dir, exist_ok=True)
            os.makedirs(videos_dir, exist_ok=True)
            os.makedirs(musics_dir, exist_ok=True)

        # Verifica se há uma marca de separador no caminho
        if "-" in line:
            path = os.path.join(path, "Downloads")

        with open(path_for_download_file, 'w') as file:
            file.write(path)

    except FileNotFoundError:
        if not os.path.exists(download_dir):
            os.makedirs(download_dir, exist_ok=True)
            os.makedirs(videos_dir, exist_ok=True)
            os.makedirs(musics_dir, exist_ok=True)

        with open(path_for_download_file, 'w') as file:
            file.write(path)
