

from pytube import YouTube

link= input('enter link here: ')

yt= YouTube(link)


yt_down= yt.streams.get_lowest_resolution()

yt_down.download()

print('Successful ')