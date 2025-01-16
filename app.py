import yt_dlp
import streamlit as st
import os
import tempfile

st.title("YouTube Video Downloader")

link = st.text_input("Enter the URL of the YouTube video")

def download_video(url):
    with tempfile.TemporaryDirectory() as temp_dir:
        ydl_opts = {
            'outtmpl': os.path.join(temp_dir, '%(title)s.%(ext)s'),
            'format': 'best[ext=mp4]',  # Forces MP4 format
            'no_warnings': True,
            'extract_flat': False
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # First extract info to handle both regular videos and shorts
            info = ydl.extract_info(url, download=True)
            filename = ydl.prepare_filename(info)
            
            # Read the downloaded file
            with open(filename, 'rb') as f:
                video_data = f.read()
                
            return video_data, os.path.basename(filename)

if link:
    try:
        # Convert shorts URL to regular URL if needed
        if "/shorts/" in link:
            link = link.replace("/shorts/", "/watch?v=")
            
        video_data, filename = download_video(link)
        
        st.download_button(
            label="Download Video",
            data=video_data,
            file_name=filename,
            mime="video/mp4"
        )
        
    except Exception as e:
        st.error(f"An error occurred: {e}")
