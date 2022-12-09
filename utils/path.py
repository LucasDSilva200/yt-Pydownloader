#!/usr/bin/env python

import os
from utils.detectos import detect


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