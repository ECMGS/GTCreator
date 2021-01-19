import ffmpeg

from os import listdir
from os.path import isfile, join, normpath

from sys import argv, exit

import config

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
    images = ffmpeg.input(folder+"*."+config.input_format, pattern_type="glob", framerate=config.fps)
    reescaledImages = images.filter('scale', size=config.video_size)
    return reescaledImages

def mergeFolderVideos(vidArr):
    stream = vidArr[0]
    for i in range(1,len(vidArr)):
        stream = ffmpeg.concat(stream, vidArr[i])
    return stream

def exportToMP4(stream):
    out = ffmpeg.output(stream, config.out_name, codec=config.codec, format=config.video_format, crf=20, pix_fmt=config.pix_fmt)
    out.run()

def __main__():
    folderArr = []

    folderArr = parseFoldersFromArgs()

    print("parsing "+str(len(folderArr))+" folders")
    imageStreamArr = []
    for i in range(1, len(folderArr)):
        imageStreamArr.append(mergePicturesIntoVID(folderArr[i]))
    
    print(imageStreamArr)

    stream = mergeFolderVideos(imageStreamArr)

    exportToMP4(stream)
    
__main__()
