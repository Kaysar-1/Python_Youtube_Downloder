# Setup Instructions 

1. Install Visual Code Studio(500 MB or under)

2. Install Python 3.11 (90 MB or under or more)

3. Open the terminal in Visual Code Studio's terminal or Open Comand line and copy and paste...

`pip install pytube`

(Note: When installing pytube you will get a deprication warning and an error. ignore those.)

4. Open YtDownloaderApp.py in Visual Code Studio and find the def Download function.

```
def Download():
    yd.download("/Users/User/Documents/PythonPrograms/YoutubeDownloads")
    print("Finished Downloading")
```

5. Then put the current file path of the "YoutubeDownloads" folder inside the curly brackets of yd.download(""). There should be my file path to the YoutubeDownloads folder currently in their.

```
def Download():
    yd.download("Put your file path here of YoutubeDownload Folder")
    print("Finished Downloading")
```
6. Now look at the function "Plist" and find the 3 resolotion choices. Within those 3 if and elif statements go to...

```
video.streams.get_lowest_resolution().download("/Users/User/Documents/PythonPrograms/YoutubeDownloads")
video.streams.get_by_resolution(resolution="360p").download("/Users/User/Documents/PythonPrograms/YoutubeDownloads")
video.streams.get_lowest_resolution().download("/Users/User/Documents/PythonPrograms/YoutubeDownloads")
```
7. Then put the current file path of the "YoutubeDownloads" folder inside the curly brackets of yd.download(""). There should be my file path to the YoutubeDownloads folder currently in their.

8. Congrats! your youtube downloader is setup (NOTE: Evertime you move the location of the YoutubeDownloads folder you have to redo steps 4-7 to make sure the program can find the YoutubeDownloads folder.)
