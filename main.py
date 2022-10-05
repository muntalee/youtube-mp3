import pytube
import subprocess
import os

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
    
    #stream.download(output_path='output/',filename=f"{yt.title.replace('/','')}.mp3")
    filename = yt.title.replace('/','').replace(' ','_')

    print(f"Downloading {yt.title}...")
    stream.download(output_path='output/', filename = filename + ".webm")
    print("WEBM Download Complete")
    print("Starting MP3 Download")
    #subprocess.run(f'ffmpeg -i "output/{yt.title}".webm "output/{yt.title}".mp3', shell=True)

    subprocess.run([
        'ffmpeg',
        '-i', os.path.join('output',f'{filename}.webm'),
        os.path.join('output', f'{filename}.mp3')
    ])

    print("MP3 Download Complete")

    os.remove(f"output/{filename}.webm")

print("Finished going throgh links.txt!")
print("Thank you for using my script <3 - krakenegg101")
links.close()
