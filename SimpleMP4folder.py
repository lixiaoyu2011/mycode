import tkinter as tk
import os
import random
import shutil
import pathlib
from tkinter import filedialog
import os
import random
import shutil
import pathlib


# 复制抽取
def copy_random_files_from_subfolders_temp(source_folder, destination_folder, call_count):
    # 获取当前调用次数
    call_count += 1
    # 创建子文件夹
    subfolder_name = f"hecheng_{call_count}"
    subfolder_folder = os.path.join(destination_folder, subfolder_name)
    print(f"subfolder_name {subfolder_name} subfolder_folder {subfolder_folder} ")
    # os.makedirs(subfolder_folder, exist_ok=True)
    # 创建新文件夹
    pathlib.Path(subfolder_folder).mkdir(parents=True, exist_ok=True)

    # 列出source_folder下所有子文件夹
    subfolders = [f.path for f in os.scandir(source_folder) if f.is_dir()]

    for folder in subfolders:
        # 列出每个子文件夹下的文件
        files = [f.path for f in os.scandir(folder) if f.is_file()]

        # 如果文件夹为空，则跳过
        if not files:
            continue

        # 从列表中随机选择一个文件
        random_file = random.choice(files)

        # 设置新文件夹中的文件路径
        new_file_path = os.path.join(subfolder_folder, os.path.basename(random_file))

        # 复制文件
        shutil.copy2(random_file, new_file_path)


import os
import random
import shutil
import pathlib
import sys


# 复制抽取
def move_random_files_from_subfolders_temp(source_folder, destination_folder, call_count):
    # 获取当前调用次数
    call_count += 1
    # 创建子文件夹
    subfolder_name = f"hecheng_{call_count}"
    subfolder_folder = os.path.join(destination_folder, subfolder_name)
    print(f"subfolder_name {subfolder_name} subfolder_folder {subfolder_folder} ")
    # os.makedirs(subfolder_folder, exist_ok=True)
    # 创建新文件夹
    pathlib.Path(subfolder_folder).mkdir(parents=True, exist_ok=True)

    # 列出source_folder下所有子文件夹
    subfolders = [f.path for f in os.scandir(source_folder) if f.is_dir()]

    for folder in subfolders:
        # 列出每个子文件夹下的文件
        files = [f.path for f in os.scandir(folder) if f.is_file()]

        # 如果文件夹为空，则跳过
        if not files:
            sys.exit(0)  # 正常退出
            break

        # 从列表中随机选择一个文件
        random_file = random.choice(files)

        # 设置新文件夹中的文件路径
        new_file_path = os.path.join(subfolder_folder, os.path.basename(random_file))

        # 复制文件
        shutil.move(random_file, new_file_path)


import tkinter as tk
import os
import random
import shutil
import pathlib
from tkinter import filedialog


class MP4folder:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Simple MP4folder")
        self.create_widgets()
        self.folder_selected = ''
        self.log_folder_label
        self.myentry

    def create_widgets(self):
        # 等于按钮
        # 选择文件夹按钮
        select_folder_button = tk.Button(self.window, text="选择文件夹", command=self.select_folder)
        select_folder_button.pack(padx=10, pady=10)

        # # # 显示选择的文件夹
        self.log_folder_label = tk.Label(self.window, text="未选择文件夹", width=80)
        self.log_folder_label.pack()

        # 执行操作按钮
        action_button = tk.Button(self.window, text="每个文件夹奇数编码", command=self.perform_action_jishu)
        action_button.pack(padx=10, pady=10)

        # 执行操作按钮
        action_button2 = tk.Button(self.window, text="每个文件夹偶数编码", command=self.perform_action_oushu)
        action_button2.pack(padx=10, pady=10)

        # 执行操作按钮
        action_button3 = tk.Button(self.window, text="每个文件夹随机抽取复制到新文件夹",
                                   command=self.copy_random_files_from_subfolders)
        action_button3.pack(padx=10, pady=10)

        # 执行操作按钮
        action_button4 = tk.Button(self.window, text="每个文件夹随机抽取移动到新文件夹",
                                   command=self.move_random_files_from_subfolders)
        action_button4.pack(padx=10, pady=10)

        # 执行操作按钮
        action_button5 = tk.Button(self.window, text="显示选择的文件夹", command=self.display_folder)
        action_button5.pack(padx=10, pady=10)

        label = tk.Label(self.window, text="Loop Count:")
        label.pack()
        self.myentry = tk.Entry(self.window)
        self.myentry.pack()
        self.window.mainloop()

    # def on_button_click(self):
    #     try:

    #         loop_count = int(self.myentry.get())
    #         for i in range(loop_count):
    #             print(f"Loop {i+1} of {loop_count}")
    #     except ValueError:
    #         print("Invalid loop count")

    def copy_random_files_from_subfolders(self):
        # 这里可以添加你的操作代码
        try:
            import os
            # 设置新文件夹的名称
            new_folder_name = 'hecheng'
            # 获取当前工作目录的父目录
            parent_dir = os.path.abspath(os.path.join(self.folder_selected, '..'))
            # 创建新文件夹的完整路径
            new_folder_path = os.path.join(parent_dir, new_folder_name)

            # 如果文件夹不存在，则创建它
            if not os.path.exists(new_folder_path):
                os.makedirs(new_folder_path)
                print(f'Folder "{new_folder_path}" created successfully.')
            else:
                print(f'Folder "{new_folder_path}" already exists.')
            # 循环调用
            loop_count = int(self.myentry.get())
            for i in range(loop_count):
                print(f"Loop {i + 1} of {loop_count}")
                # 使用示例
                source_folder = self.folder_selected  # 源文件夹路径
                destination_folder = new_folder_path  # 目标文件夹路径
                copy_random_files_from_subfolders_temp(source_folder, destination_folder, i)

        except ValueError:
            print("Invalid loop count")
        print("Action performed copy_random_files_from_subfolders!")

    def move_random_files_from_subfolders(self):

        try:
            import os
            # 设置新文件夹的名称
            new_folder_name = 'hecheng'
            # 获取当前工作目录的父目录
            parent_dir = os.path.abspath(os.path.join(self.folder_selected, '..'))
            # 创建新文件夹的完整路径
            new_folder_path = os.path.join(parent_dir, new_folder_name)

            # 如果文件夹不存在，则创建它
            if not os.path.exists(new_folder_path):
                os.makedirs(new_folder_path)
                print(f'Folder "{new_folder_path}" created successfully.')
            else:
                print(f'Folder "{new_folder_path}" already exists.')
            # 循环调用
            loop_count = int(self.myentry.get())
            for i in range(loop_count):
                print(f"Loop {i + 1} of {loop_count}")
                # 使用示例
                source_folder = self.folder_selected  # 源文件夹路径
                destination_folder = new_folder_path  # 目标文件夹路径
                move_random_files_from_subfolders_temp(source_folder, destination_folder, i)

        except ValueError:
            print("Invalid loop count")
        print("Action performed move_random_files_from_subfolders!")

    def select_folder(self):
        self.folder_selected = filedialog.askdirectory()
        my_folder_selected = self.folder_selected
        print(f"my_folder  {my_folder_selected}")
        folder_label = tk.Label(self.window, width=80)
        folder_label.pack()
        folder_label.config(text=my_folder_selected)
        self.log_folder_label.config(text="已选择文件夹")

    def perform_action_jishu(self):
        # 这里可以添加你的操作代码
        print("Action performed _jishu!")
        root_dir = self.folder_selected
        for root_dirpath, subdirs, files in os.walk(root_dir):
            for subdir in subdirs:
                # print(os.path.join(root_dirpath, subdir))
                subdir = os.path.join(root_dirpath, subdir)
                print(subdir)
                folder_path = subdir
                files = os.listdir(folder_path)
                count = 1
                for file in files:
                    if file.endswith('.mp4'):  # 假设我们只处理mp4文件
                        file_path = os.path.join(folder_path, file)
                        print(f"file_path  {file_path}")
                        # 构建新的文件名
                        parent_dir_name = os.path.dirname(file_path)
                        print(f"parent_dir_name {parent_dir_name}")
                        zi_folder_name = os.path.basename(parent_dir_name)

                        print(f"folder_name {zi_folder_name}")
                        new_name = f"{count}_{zi_folder_name}.mp4"  # f"{base}_{1}{extension}"
                        print(f"new_name {new_name}")
                        # 重命名文件
                        old_path = os.path.join(folder_path, file)
                        # print(f"old_path {old_path}")
                        new_path = os.path.join(folder_path, new_name)
                        print(f"new_path {new_path}")
                        # 检查文件是否存在
                        if os.path.exists(new_path):
                            print(f"文件 {new_path} 存在。")
                        else:
                            # print(f"文件 {new_path} 不存在。")
                            os.rename(old_path, new_path)
                        count += 2

    def perform_action_oushu(self):
        # 这里可以添加你的操作代码
        print("Action performed _oushu!")
        root_dir = self.folder_selected
        for root_dirpath, subdirs, files in os.walk(root_dir):
            for subdir in subdirs:
                # print(os.path.join(root_dirpath, subdir))
                subdir = os.path.join(root_dirpath, subdir)
                print(subdir)
                folder_path = subdir
                files = os.listdir(folder_path)
                count = 0
                for file in files:
                    if file.endswith('.mp4'):  # 假设我们只处理mp4文件
                        file_path = os.path.join(folder_path, file)
                        # print(f"file_path  {file_path}")
                        # 构建新的文件名
                        parent_dir_name = os.path.dirname(file_path)
                        print(f"parent_dir_name {parent_dir_name}")
                        zi_folder_name = os.path.basename(parent_dir_name)

                        print(f"folder_name {zi_folder_name}")
                        new_name = f"{count}_{zi_folder_name}.mp4"  # f"{base}_{1}{extension}"
                        print(f"new_name {new_name}")
                        # 重命名文件
                        old_path = os.path.join(folder_path, file)
                        # print(f"old_path {old_path}")
                        new_path = os.path.join(folder_path, new_name)
                        print(f"new_path {new_path}")
                        # 检查文件是否存在
                        if os.path.exists(new_path):
                            print(f"文件 {new_path} 存在。")
                        else:
                            # print(f"文件 {new_path} 不存在。")
                            os.rename(old_path, new_path)
                        count += 2

    def display_folder(self):
        # 这里可以添加你的操作代码
        print(f"folder_selected {self.folder_selected}")


# 运行计算器
MP4folder()