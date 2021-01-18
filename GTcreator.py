import ffmpeg
import graphviz

from os import listdir
from os.path import isfile, join, normpath

def getFilesFromFolder(folderArr):
    fileArr = []
    for folder in folderArr:
        allFiles = listdir(normpath(folder))
        for file in allFiles:
            fileURL = join(folder, file)
            if isfile(fileURL):
                fileArr.append(fileURL)
    fileArr.sort() 
    return fileArr 

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
    folderArr = ['/home/ecmgs/100GOPRO/', '/home/ecmgs/101GOPRO/']

    imageStreamArr = []
    for folder in folderArr:
        imageStreamArr.append(mergePicturesIntoVID(folder))
    
    print(imageStreamArr)

    stream = mergeFolderVideos(imageStreamArr)

    exportToMP4(stream)
    
__main__()
