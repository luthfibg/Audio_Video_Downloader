from os import path
import os

from tkinter import *
from tkinter import filedialog
from moviepy import *
from moviepy.editor import VideoFileClip
from pytube import YouTube


import shutil


#functions
def select_path():
    #allows user to select path from the explorer
    path = filedialog.askdirectory()
    path_label.config(text=path)

def download_video():
    #get user path
    get_link = link_field.get()
    #get selected path
    user_path = path_label.cget("text")
    screen.title("Downloading Youtube Video...")
    #download video
    mp4_video = YouTube(get_link).streams.get_highest_resolution().download()
    vid_clip = VideoFileClip(mp4_video)
    vid_clip.close()
    #move video to selected directory
    shutil.move(mp4_video, user_path)
    screen.title("Download Complete! Let's Download Another Video or Audio...")

def download_audio():
    #get user path
    get_link = link_field.get()
    #get selected path
    user_path = path_label.cget("text")
    screen.title("Downloading Youtube Audio...")
    #download audio
    mp3_audio = YouTube(get_link).streams.filter(only_audio = True).first()
    audio_file = mp3_audio.download()

    #rename mp3 from video title
    base, ext = os.path.splitext(audio_file)
    new_file = base + ".mp3"
    os.rename(audio_file, new_file)

    #move audio to selected directory
    shutil.move(new_file, user_path)
    screen.title("Download Complete! Let's Download Another Audio or Video...")

screen = Tk()
title = screen.title('Youtube Audio & Video Downloader')
canvas = Canvas(screen, width=500, height=500)
canvas.pack()

#image logo
logo_img = PhotoImage(file='yt.png')
#resize image
logo_img = logo_img.subsample(14, 14)

canvas.create_image(250, 80, image=logo_img)

#link field
link_field = Entry(screen, width=50)
link_label = Label(screen, text="Enter Youtube Video Link", font=("Arial", 13))

#add widgets to window
canvas.create_window(250, 180, window=link_label)
canvas.create_window(250, 220, window=link_field)

#select path to place file
path_label = Label(screen, text="Select Path For File", font=("Arial", 13))
select_btn = Button(screen, text="Select", command=select_path)

#add to window
canvas.create_window(250, 280, window=path_label)
canvas.create_window(250, 320, window=select_btn)

#download video button
download_mp4_btn = Button(screen, text="Download Video (mp4)", command= download_video)
#add mp4 dwndld btn to canvas
canvas.create_window(250, 380, window=download_mp4_btn)

#download audio button
download_mp3_btn = Button(screen, text="Download Audio (mp3)", command= download_audio)
#add mp3 dwndld btn to canvas
canvas.create_window(250, 420, window=download_mp3_btn)

screen.mainloop()

