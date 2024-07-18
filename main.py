import streamlit as st
from yt_dlp import YoutubeDL
import subprocess


def link_convert(youtube_URL):
    subprocess.run(["pip", "install", "yt-dlp"])
    subprocess.run(["yt-dlp", "-U"])
    cmd = f"yt-dlp -g {youtube_URL}"
    
    result = subprocess.run(cmd.split(), capture_output=True, text=True).stdout

    
    return result
    
    
    
    
    """
    ydl_opts = {
    'format': 'best',
    'quiet': True,  # 不要な出力を抑制
    'skip_download': True  # 実際のダウンロードをスキップ
    }

    with YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(youtube_URL, download=True)
        print(info_dict)
        return info_dict
        video_url = info_dict['url']
        

    #st.codde(video_url)
    """


parms = st.query_params.to_dict()
youtube_url = parms["URL"]



result = str()
g = link_convert(youtube_url)
r = g.split()

for i in r:
    if ".m3u8" in i:
        result = i
        break
print(result)
st.write(result)
