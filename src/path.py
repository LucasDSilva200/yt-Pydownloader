#!/usr/bin/env python

import os
from src.detectos import detect


def download_folder_search():
    try:
        file = open("path_for_download.txt")
        path = file.readline()
        file.close()
        return path
    except:
        path = detect()
        path = f"{path}/Downloads"
        with open("path_for_download.txt",'w+') as file:
            file.write(path)
        return path

def list_files():
    path = download_folder_search()
    path = f'{path}/youtube'
    for _, _,files in os.walk(path):
        for file in files:
            print(file)
            

def change_path(path):
    operational_system = detect()
    if '~' in path:
        path = path.replace('~', f'{operational_system}')
        print(path)
        
    with open("path_for_download.txt",'w+') as file:
            file.write(f'{path}')
    print("O caminho foi mudado com sucesso")


def Arrive_if_the_path_exists():
    path = detect()
    try:
        file = open("path_for_download.txt")
        line = file.readline()
        if not os.path.exists(f"{path}/Downloads/youtube/"):
                dir_yt = os.path.join(os.path.expanduser("~"), "Downloads", "youtube")
                dir_vd = os.path.join(os.path.expanduser("~"), "Downloads", "youtube","videos")
                dir_mcs = os.path.join(os.path.expanduser("~"), "Downloads", "youtube", "musics")
                os.makedirs(dir_yt, exist_ok=True)
                os.makedirs(dir_vd, exist_ok=True)
                os.makedirs(dir_mcs, exist_ok=True)
        if not os.path.exists(f"{path}/Downloads/youtube/videos"):
            dir_vd = os.path.join(os.path.expanduser("~"), "Downloads", "youtube","videos")
            os.makedirs(dir_vd, exist_ok=True)
        if not os.path.exists(f"{path}/Downloads/youtube/musics"):
            dir_mcs = os.path.join(os.path.expanduser("~"), "Downloads", "youtube", "musics")
            os.makedirs(dir_mcs, exist_ok=True)    
        if "-" in line:
            path = f"{path}/Downloads"
            with open("path_for_download.txt",'w+') as file:
                file.write(path)
                
    except FileNotFoundError:
        path = detect()
        if not os.path.exists(f"{path}/Downloads/youtube/"):
            dir_yt = os.path.join(os.path.expanduser("~"), "Downloads", "youtube")
            dir_vd = os.path.join(os.path.expanduser("~"), "Downloads", "youtube","videos")
            dir_mcs = os.path.join(os.path.expanduser("~"), "Downloads", "youtube", "musics")
            os.makedirs(dir_yt, exist_ok=True)
            os.makedirs(dir_vd, exist_ok=True)
            os.makedirs(dir_mcs, exist_ok=True)
            path = f"{path}/Downloads"
        with open("path_for_download.txt",'w+') as file:
            file.write(path)
