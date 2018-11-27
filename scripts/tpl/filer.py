import tkinter as tk
from tkinter import filedialog
import os
import csv

def file_chooser():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()
    print(file_path)
    return file_path


def dirzao_chooser():
    direzao = filedialog.askdirectory()
    return direzao


def make_dir(path_dir):
    string = "Results-Python"
    path_dir += string
    if not os.path.exists(path_dir):
        os.makedirs(path_dir)
   

def read_csv(path):
    with open(path,'rb') as csvzao:
        reader = csv.reader(csvzao)
        for row in reader:
            print(', '.join(row))


def write_csv(r):
    with open("csvzao.csv", "wb") as csv:
        for chunk in r.iter_content(chunk_size=1024):

            if chunk:
                csv.write(chunk)


def mkdirzao():
    x = os.getcwd()
    print(x)
    make_dir(x)
