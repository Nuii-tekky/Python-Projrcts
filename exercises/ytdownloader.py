
from pytube import YouTube


query= input('Enter the link: ')

def download_file(value):
  yt_obj= YouTube(value)

  yt_dwnld_obj= yt_obj.streams.get_by_resolution(480)

  yt_dwnld_obj.download(r'C:\Users\ekomobong\Videos\Shorts')

download_file(query)