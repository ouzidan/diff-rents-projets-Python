import pyshorteners

shortener = pyshorteners.Shortener()
long_link = input(" Your link: ")
short_link = shortener.tinyurl.short(long_link)
print(short_link)
