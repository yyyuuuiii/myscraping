# -*- coding: utf-8 -*-
import urllib.request
from bs4 import BeautifulSoup

url = "https://www.youtube.com/user/Hak5Darren/videos"
try:
    html = urllib.request.urlopen(url)
    print(url)
    soup = BeautifulSoup(html.read(), "html.parser")
except:
    print("Not Found:" + url)

for uls in soup("ul", {"id": "channels-browse-content-grid"}):
    for lockupTitle in soup("a", {"class": "yt-uix-sessionlink"}):
        print(lockupTitle.get("href"))

    for times in soup("span", {"class": "video-time"}):
        print(times.text)

    for yt_thumb_clip in soup("span", {"class": "yt-thumb-clip"}):
        srcb = yt_thumb_clip.img
        print(srcb["src"])

    for ulc in soup("ul", {"class": "yt-lockup-meta-info"}):
        print(ulc.li.text)

html.close()

