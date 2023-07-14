from pytube import YouTube

l = "https://youtu.be/ym52G8M2TEE"
y = YouTube(l)

v = y.streams.all()
vid = list(enumerate(v))

for i in vid:
    print(i)
print()
s = int(input("enter : "))

v[s].download()
print("Video download successfully")