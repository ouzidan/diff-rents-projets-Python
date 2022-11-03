# python modules i use in this project
# sounddevice
# scipy ... write

import sounddevice
from scipy.io.wavfile import write

seconds = int(input("How many seconds you need to record:  "))
print("recording Started...")
recording = sounddevice.rec((seconds*44100), channels=2)
sounddevice.wait()
file_name = input("give the name to save: ")
write(file_name,44100,recording)
print("record done.")