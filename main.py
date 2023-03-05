from pytube import YouTube
from customtkinter import *
import customtkinter
from tkinter import PhotoImage
from PIL import Image
import threading
import os
from lxml import etree

window = CTk()
window.geometry("500x500")
window.minsize(500, 500)
window.maxsize(500, 500)
window.title("Youtube video downloader")
customtkinter.set_appearance_mode("dark")
photo = PhotoImage(file="youtube.png")
window.iconphoto(False, photo)


def yt_dwl():
    try:
        link = str(entry.get())
        yt = YouTube(link)
        video = yt.streams.get_highest_resolution()
        video.download(r"C:\Users\name\Videos\youtube_videos")
        loadingbar.stop()
        loadingbar.place(x=510, y=0)
        label_txt2.configure(text="Download succes.")
    except:
        label_txt2.configure(text="  Download failed.")
        loadingbar.stop()
        loadingbar.place(x=510, y=0)


def start(event):
    t = threading.Thread(target=yt_dwl)
    t.start()
    loadingbar.start()
    loadingbar.place(x=150, y=370)
    label_txt2.configure(text="")


def vid_info(event):
    info_window = CTkToplevel()
    info_window.title("Video info")
    info_window.geometry("400x400")
    info_window.minsize(400, 400)
    info_window.maxsize(400, 400)
    info_window.iconphoto(False, photo)
    textbox = CTkTextbox(info_window, width=400, height=400, corner_radius=0, fg_color="#161616", font=("helvetica", 15))
    textbox.place(x=0, y=0)
    try:
        link = str(entry.get())
        yt = YouTube(link)
        views = "{:,}".format(yt.views)
        vid_length = yt.length
        minutes = vid_length // 60
        seconds = vid_length % 60
        textbox.insert(0.0, f"Channel: \n{yt.author}\n\n\nTitle: \n{yt.title}\n\nViews: "
                            f"\n{views}\n\nLength: \n{minutes} Minutes and {seconds} Seconds\n\n___________________________________________\n\nDescription:\n{yt.description}"
                            f"\n\nPublish date: \n{yt.publish_date}")
    except:
        info_window.destroy()


def clear(event):
    entry.delete(0, END)
    label_txt2.configure(text="")


def open_folder(event):
    os.startfile(r"C:\Users\name\Videos\youtube_videos")


frame = CTkFrame(window, fg_color="#161616", corner_radius=0, width=500, height=500)
frame.place(x=0, y=0)

img = customtkinter.CTkImage(dark_image=Image.open("youtube (1).png"), size=(250, 250))
label_img = CTkLabel(frame, text="", image=img)
label_img.place(x=125, y=0)

label_txt = CTkLabel(frame, text="link", text_color="white", font=("helvetica", 30))
label_txt.place(x=225, y=260)

label_txt2 = CTkLabel(frame, text="", text_color="blue", font=("helvetica", 15))
label_txt2.place(x=190, y=400)

entry = CTkEntry(frame, width=250, height=40, corner_radius=10, border_width=2, border_color="white")
entry.place(x=125, y=300)

loadingbar = CTkProgressBar(frame, width=200, height=5, progress_color="blue", corner_radius=20, indeterminate_speed=1.0
                            , mode='indeterminate')

window.bind("<Return>", start)
window.bind("<i>", vid_info)
window.bind("<c>", clear)
window.bind("<f>", open_folder)
window.mainloop()
