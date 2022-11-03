# importing python module
#moviepy ... pip install moviepy

import moviepy.editor as mp

Clip = mp.VideoFileClip("Variables.mp4")
Clip.audio.write_audiofile("my Audio.mp3")