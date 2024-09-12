import os
import shutil


def move_files_to_parent_dir(directory):
    # 获取目录中的所有文件和子目录
    contents = os.listdir(directory)
    for item in contents:
        # 构建完整的路径
        item_path = os.path.join(directory, item)
        # 如果是文件，直接移动到父目录
        if os.path.isfile(item_path):
            parent_dir = os.path.dirname(directory)
            shutil.move(item_path, parent_dir)
        # 如果是目录，递归调用函数
        elif os.path.isdir(item_path):
            move_files_to_parent_dir(item_path)


import os


def delete_empty_folders(path):
    move_files_to_parent_dir(path)
    for folder_name, subfolders, filenames in os.walk(path):
        if not filenames and not subfolders:
            os.rmdir(folder_name)
            print(f"Deleted empty folder: {folder_name}")


import os
import shutil

def create_everyone_folders(source_dir):
    # 遍历源目录下的所有文件
    for filename in os.listdir(source_dir):
        # 获取文件的绝对路径
        file_path = os.path.join(source_dir, filename)

        # 如果是文件，而不是目录
        if os.path.isfile(file_path):
            # 创建一个新目录，与文件同名
            new_dir = os.path.join(source_dir, filename.rsplit('.', 1)[0])
            os.makedirs(new_dir, exist_ok=True)

            # 移动文件到新目录
            shutil.move(file_path, new_dir)
# # 使用示例
# path_to_check = 'ceshihebing'
# delete_empty_folders(path_to_check)

# # 使用示例
# directory_path = 'ceshihebing'
# move_files_to_parent_dir(directory_path)

import tkinter as tk
import os
import random
import shutil
import pathlib
from tkinter import filedialog


class MP4folder:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("SimpleHebingFolder")
        self.create_widgets()
        self.folder_selected = ''

    def create_widgets(self):
        # 等于按钮
        # 选择文件夹按钮
        select_folder_button = tk.Button(self.window, text="选择文件夹", command=self.select_folder)
        select_folder_button.pack(padx=10, pady=10)

        # # # 显示选择的文件夹
        self.log_folder_label = tk.Label(self.window, text="未选择文件夹", width=80)
        self.log_folder_label.pack()

        # 执行操作按钮
        action_button1 = tk.Button(self.window, text="合并文件夹内文件到二级目录", command=self.display_folder)
        action_button1.pack(padx=10, pady=10)

        # 执行操作按钮
        action_button2 = tk.Button(self.window, text="为每一个文件创建单独的文件夹", command=self.everyone_folder)
        action_button2.pack(padx=10, pady=10)

        label = tk.Label(self.window, text="请选择要操作的文件夹")
        label.pack()

        self.window.mainloop()

    def select_folder(self):
        self.folder_selected = filedialog.askdirectory()
        my_folder_selected = self.folder_selected
        print(f"my_folder  {my_folder_selected}")
        folder_label = tk.Label(self.window, width=80)
        folder_label.pack()
        folder_label.config(text=my_folder_selected)
        self.log_folder_label.config(text="已选择文件夹")

    def display_folder(self):
        # 这里可以添加你的操作代码
        print(f"folder_selected {self.folder_selected}")
        delete_empty_folders(self.folder_selected)

    def everyone_folder(self):
        # 这里可以添加你的操作代码
        print(f"everyone_folder {self.folder_selected}")
        create_everyone_folders(self.folder_selected)


# 运行计算器
MP4folder()
