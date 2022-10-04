import pytube

links = open("links.txt", "r")

for link in links:
    yt = pytube.YouTube(link)
    
    audio = yt.streams.filter(only_audio=True)
    largestABR = 0
    id = 0
    for i in audio:
        if int(i.abr[:-4]) > largestABR:
            id = i.itag
    
    stream = yt.streams.get_by_itag(id)
    
    print(f"Downloading {yt.title}...")
    stream.download(output_path='output/',filename=f"{yt.title.replace('/','')}.mp3")
    print("Download Complete")

links.close()
