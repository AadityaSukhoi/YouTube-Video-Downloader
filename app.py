# from pytube import YouTube
# import streamlit as st

# st.title("YouTube Video Downloader")

# link = st.text_input("Enter the URL of the YouTube video")

# if st.button("Download"):

#     yt = YouTube(link)
#     video = yt.streams.get_highest_resolution()

#     video.download()

#     st.success("Video downloaded successfully")

import yt_dlp
import streamlit as st

st.title("YouTube Video Downloader")

link = st.text_input("Enter the URL of the YouTube video")

if st.button("Download"):
    try:
        ydl_opts = {
            'outtmpl': '%(title)s.%(ext)s',
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([link])
        st.success("Video downloaded successfully")
    except Exception as e:
        st.error(f"An error occurred: {e}")
