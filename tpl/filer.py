import tkinter as tk
from tkinter import filedialog
import os


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
