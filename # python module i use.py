# python module i use
# pytube
from pytube import YouTube

link = input("Video Link: ")
Download_Video_Link = YouTube(link)
Title = Download_Video_Link.title
Num_of_Views = Download_Video_Link.views
Length_of_Video = Download_Video_Link.length
Author_of_Video = Download_Video_Link.author


print("Title: ",Title)
print("Num of Views: ",Num_of_Views)
print("Length os Video: ",Length_of_Video, "Seconds")
print("Author: ",Author_of_Video)


Download_Video_Link.streams.get_highest_resolution().download()
print("Download Don")