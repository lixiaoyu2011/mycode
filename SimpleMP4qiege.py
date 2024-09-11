import moviepy
import os
from moviepy.editor import VideoFileClip

import proglog
def get_video_duration(file_path):
    video = VideoFileClip(file_path)
    duration = video.duration
    video.close()
    return duration

def read_videos_duration_in_folder(folder_path):
    shichang = set()
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(('.mp4', '.mov', '.avi', '.mkv')):
            file_path = os.path.join(folder_path, filename)
            duration, video_name = get_video_duration(file_path)
            # print(f"{filename}  file_path: {file_path}")
            shichang.add(duration)
            # print(f"{filename}  duration: {duration} seconds")
    return shichang

from collections import defaultdict
#使用集合作为默认值
shichang_set_dict = defaultdict(set)
def read_videos_duration_in_folder_fuzhi(folder_path):
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(('.mp4', '.mov', '.avi', '.mkv')):
            file_path = os.path.join(folder_path, filename)
            duration, video_name = get_video_duration(file_path)
            # print(f"{filename}  duration: {duration} seconds")
            shichang_set_dict[duration].add(file_path)


import moviepy
import os
from moviepy.editor import VideoFileClip
# 获取时长
def get_video_duration(file_path):
    video_clip = VideoFileClip(file_path)
    duration = video_clip.duration
    video_name_file = video_clip.filename.split('\\')[-1]
    # 使用os.path.splitext分离文件名和扩展名
    video_name, file_extension = os.path.splitext(video_name_file)
    print(video_clip.filename.split('\\'))
    print("Video Name:", video_name)
    video_clip.close()
    return duration, video_name

# 根据时间点进行切割
from moviepy.editor import VideoFileClip

def split_video(input_video_path, output_folder, split_points, video_name):
    video_clip = VideoFileClip(input_video_path)
    duration, video_name = get_video_duration(input_video_path)
    print(f"时长为: {duration}秒 video_name {video_name}")
    for i, point in enumerate(split_points):
        start_time, end_time = point
        if start_time < 0:
            start_time = 0
        if end_time > duration:
            end_time = duration
        sub_clip = video_clip.subclip(start_time, end_time)
        output_path = f"{output_folder}/{video_name}_{i+1}.mp4"
        sub_clip.write_videofile(output_path)


import tkinter as tk
import os
import random
import shutil
import pathlib
from tkinter import filedialog


class MP4folder:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Simple MP4qiege")
        self.create_widgets()
        self.folder_selected = ''
        self.label_result
        self.shichang
        self.entry1
        self.entry2
        self.entry3
        self.entry4
        self.entry5
        self.entry6
        self.entry7
        self.entry8

    def create_widgets(self):
        # 等于按钮
        # 选择文件夹按钮
        select_folder_button = tk.Button(self.window, text="选择文件夹", command=self.select_folder)
        select_folder_button.pack(padx=10, pady=10)

        # # # 显示选择的文件夹
        self.log_folder_label = tk.Label(self.window, text="未选择文件夹", width=80)
        self.log_folder_label.pack()

        # 执行操作按钮
        action_button2 = tk.Button(self.window, text="对文件夹内视频按照时长分类",
                                   command=self.read_videos_shichang_in_folder)
        action_button2.pack(padx=10, pady=10)

        # 执行操作按钮
        action_button1 = tk.Button(self.window, text="显示选择的文件夹", command=self.display_folder)
        action_button1.pack(padx=10, pady=10)

        # 执行操作按钮
        action_button2 = tk.Button(self.window, text="对文件夹内视频按照时间段进行切割", command=self.qiege)
        action_button2.pack(padx=10, pady=10)
        self.label_result = tk.Label(self.window, text="先填写时间段:")
        self.label_result.pack()

        label = tk.Label(self.window, text="第1段:")
        label.pack()
        self.entry1 = tk.Entry(self.window)
        self.entry1.pack()

        label2 = tk.Label(self.window, text="第2段:")
        label2.pack()
        self.entry2 = tk.Entry(self.window)
        self.entry2.pack()

        label3 = tk.Label(self.window, text="第3段:")
        label3.pack()
        self.entry3 = tk.Entry(self.window)
        self.entry3.pack()

        label4 = tk.Label(self.window, text="第4段:")
        label4.pack()
        self.entry4 = tk.Entry(self.window)
        self.entry4.pack()

        label5 = tk.Label(self.window, text="第5段:")
        label5.pack()
        self.entry5 = tk.Entry(self.window)
        self.entry5.pack()

        label6 = tk.Label(self.window, text="第6段:")
        label6.pack()
        self.entry6 = tk.Entry(self.window)
        self.entry6.pack()

        label7 = tk.Label(self.window, text="第7段:")
        label7.pack()
        self.entry7 = tk.Entry(self.window)
        self.entry7.pack()

        label8 = tk.Label(self.window, text="第8段:")
        label8.pack()
        self.entry8 = tk.Entry(self.window)
        self.entry8.pack()

        self.window.mainloop()

    def read_videos_shichang_in_folder(self):
        self.shichang = read_videos_duration_in_folder(self.folder_selected)
        print(f"read_videos_shichang {self.shichang}")
        import os
        shichang = self.shichang
        # 将集合中的数字转换为字符串
        shichang_str = set(map(str, shichang))
        # 使用集合中的数字作为文件夹名称
        # folder_path = open(r"d:\shichangfenlei")
        for number in shichang_str:
            os.makedirs(f"shichangfenlei/folder_{number}", exist_ok=True)
        read_videos_duration_in_folder_fuzhi(self.folder_selected)
        print(f"shichang_set_dict {shichang_set_dict}")
        import shutil
        for key, value in shichang_set_dict.items():
            number = float(key)
            # print(f"number {number}")
            destination_folder = f"shichangfenlei/folder_{number}"  # 确保目标文件夹存在
            os.makedirs(destination_folder, exist_ok=True)
            # print(f"value {value}")
            # 文件列表，每个文件是其完整的路径
            files_to_copy = value
            # 复制文件到目标文件夹
            for file_path in files_to_copy:
                shutil.copy2(file_path, destination_folder)

    def qiege(self):
        # 这里可以添加你的操作代码
        print(f"qiege")
        split_points = [self.entry1.get(), self.entry2.get(), self.entry3.get(), self.entry4.get(), self.entry5.get(),
                        self.entry6.get()
            , self.entry7.get(), self.entry8.get()]  # 分割点时间范围（秒）

        self.label_result.config(text=f"结果是: {split_points}")
        print(f"split_points {split_points}")
        split_points_list = [point.split(', ') for point in split_points if point]
        print(f"split_points_list {split_points_list}")
        split_points_float_nested_list = [[float(item) for item in sublist] for sublist in split_points_list]
        print(f"split_points_float_nested_list {split_points_float_nested_list}")
        import os
        # 设置新文件夹的名称
        new_folder_name = 'output_videos'
        folder_path = self.folder_selected
        # 获取当前工作目录的父目录
        parent_dir = os.path.abspath(os.path.join(folder_path, '..'))
        # 创建新文件夹的完整路径
        new_folder_path = os.path.join(parent_dir, new_folder_name)

        # 如果文件夹不存在，则创建它
        if not os.path.exists(new_folder_path):
            os.makedirs(new_folder_path)
            print(f'Folder "{new_folder_path}" created successfully.')
        else:
            print(f'Folder "{new_folder_path}" already exists.')

        output_folder = new_folder_name

        for filename in os.listdir(folder_path):
            if filename.endswith('.mp4'):  # 假设我们只处理mp4文件
                file_path = os.path.join(folder_path, filename)
                duration, video_name = get_video_duration(file_path)
                input_video_path = file_path

                output_folder2 = os.path.join(output_folder, video_name)  # 'output_videos'  # 输出文件夹路径
                os.makedirs(f"{output_folder2}", exist_ok=True)
                split_video(input_video_path, output_folder2, split_points_float_nested_list, video_name)
        self.label_result.config(text=f"完成分割")

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


# 运行计算器
MP4folder()