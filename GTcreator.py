import ffmpeg

from os import listdir
from os.path import isfile, join, normpath

from sys import argv, exit

def parseFoldersFromArgs():
    folderArr = []
    if (len(argv) == 1):
        print("no files provided")        
        exit(0)
        return
    for URL in argv:
       folderArr.append(URL) 
    return folderArr

def mergePicturesIntoVID(folder):
    images = ffmpeg.input(folder+"*.JPG", pattern_type="glob", framerate=25)
    reescaledImages = images.filter('scale', size='hd1080')
    return reescaledImages

def mergeFolderVideos(vidArr):
    stream = vidArr[0]
    for i in range(1,len(vidArr)):
        stream = ffmpeg.concat(stream, vidArr[i])
    return stream

def exportToMP4(stream):
    out = ffmpeg.output(stream, "test.mp4", format="mp4", crf=20, pix_fmt="yuv420p")
    out.run()

def __main__():
    folderArr = []

    folderArr = parseFoldersFromArgs()

    imageStreamArr = []
    for i in range(1, len(folderArr)):
        imageStreamArr.append(mergePicturesIntoVID(folderArr[i]))
    
    print(imageStreamArr)

    stream = mergeFolderVideos(imageStreamArr)

    exportToMP4(stream)
    
__main__()
