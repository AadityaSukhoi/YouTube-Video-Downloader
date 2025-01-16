# import yt_dlp
# import streamlit as st

# st.title("YouTube Video Downloader")

# link = st.text_input("Enter the URL of the YouTube video")

# if st.button("Download"):
#     try:
#         ydl_opts = {
#             'outtmpl': '%(title)s.%(ext)s',
#         }
#         with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#             ydl.download([link])
#         st.success("Video downloaded successfully")
#     except Exception as e:
#         st.error(f"An error occurred: {e}")

import yt_dlp
import streamlit as st
import os
from io import BytesIO

st.title("YouTube Video Downloader")

link = st.text_input("Enter the URL of the YouTube video")

if st.button("Download"):
    try:
        # Create a temporary directory for downloads
        if not os.path.exists("temp"):
            os.makedirs("temp")
        
        ydl_opts = {
            'outtmpl': 'temp/%(title)s.%(ext)s',
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # Get video info first
            info = ydl.extract_info(link, download=False)
            filename = ydl.prepare_filename(info)
            
            # Download the video
            ydl.download([link])
            
            # Read the file and create a download button
            with open(filename, 'rb') as f:
                st.download_button(
                    label="Download Video",
                    data=f,
                    file_name=os.path.basename(filename),
                    mime="video/mp4"
                )
            
            # Clean up
            os.remove(filename)
            
        st.success("Video ready for download!")
    except Exception as e:
        st.error(f"An error occurred: {e}")
        