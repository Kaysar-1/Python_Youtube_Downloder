from pytube import YouTube
from pytube import Playlist

print('''\nPython YT Dowloader\n''')

def SingleVideo():
    while True:

        def Download():
            yd.download("/Users/User/Documents/PythonPrograms/YoutubeDownloads")
            print("Finished Downloading")

        link = input("Enter YT Link(q to Quit)...\n")

        if link == "q":
            print("Quiting!")
            break

        yt = YouTube(link)

        print("Title: ", yt.title)
        print("Views: ", yt.views)

        print('''\n 1. Highest Resoloution
 2. Mid(360p) Resoloution
 3. Lowest Resoloution
 4. Quit\n''')
        resolutionChoice = input("Pls Pick download resolotion labled above by its number...\n")

        if resolutionChoice == "1":
            print("High Res")
            print("Downloading...")
            yd = yt.streams.get_highest_resolution()
            Download()

        elif resolutionChoice == "2":
            print("Mid Res")
            print("Downloading...")
            yd = yt.streams.get_by_resolution(resolution="360p")
            Download()       

        elif resolutionChoice == "3":
            print("Low Res")
            print("Downloading...")
            yd = yt.streams.get_lowest_resolution()
            Download()

        elif resolutionChoice == "4":
            print("Quiting")
            break

        else:
            print("That is not an Available option")
            print("Restarting!\n")



def Plist():
    while True:
        link = input("Enter YT Playlist Link(q to Quit)...\n")

        if link == "q":
            print("Quiting!")
            break

        p = Playlist(link)

        print("Title: ", p.title)

        print('''\n 1. Highest Resoloution
 2. Mid(360p) Resoloution
 3. Lowest Resoloution
 4. Quit\n''')
        resolutionChoice = input("Pls Pick download resolotion labled above by its number...\n")

        if resolutionChoice == "1":
            print("High Res")
            print(f'Downloading: {p.title}')
            for video in p.videos:
                print("\nDownloading...")
                video.streams.get_lowest_resolution().download("/Users/User/Documents/PythonPrograms/YoutubeDownloads")
                print("Finished Download.\n")

        elif resolutionChoice == "2":
            print("Low Res")
            print(f'Downloading: {p.title}')
            for video in p.videos:
                print("\nDownloading...")
                video.streams.get_by_resolution(resolution="360p").download("/Users/User/Documents/PythonPrograms/YoutubeDownloads")
                print("Finished Download.\n")

        elif resolutionChoice == "3":
            print("Low Res")
            print(f'Downloading: {p.title}')
            for video in p.videos:
                print("\nDownloading...")
                video.streams.get_highest_resolution().download("/Users/User/Documents/PythonPrograms/YoutubeDownloads")
                print("Finished Download.\n")

        elif resolutionChoice == "4":
            print("Quiting")
            break

        else:
            print("That is not an Available option")
            print("Restarting!\n")



def SingleAudioOnly():
    pass

def PlaylistAudioOnly():
    pass

while True:

    print('''\n 1. Download a single YT Video
 2. Download from a YT Playlist
 5. Quit\n''')
        
    DownloadType = input("Pls Pick Download Type labled above by its number...\n")

    if DownloadType == "1":
        SingleVideo()  

    elif DownloadType == "2":
        Plist()

    elif DownloadType == "3":
        SingleAudioOnly()

    elif DownloadType == "4":
        PlaylistAudioOnly()

    elif DownloadType == "5":
        print("Quiting")
        break

    else:
        print("That is not an Available option")
        print("Restarting!\n")