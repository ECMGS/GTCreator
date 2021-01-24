import ffmpeg
import argparse

from os import listdir
from os.path import isfile, join, normpath

from sys import argv, exit

import config

def inputParser():
    """
        Parses the arguments and return an object with them
    """
    parser = argparse.ArgumentParser(description="Creates a single vide from multiple folders, if no optional parametters, the config especified in config.py is used", prog="GTcreator")

    # Required arguments
    requiredArguments = parser.add_mutually_exclusive_group(required=True)
    requiredArguments.add_argument("-i", "--input_folders", help="input folders to be parsed", nargs="+")

    # Optional arguments
    parser.add_argument("-o", "--output_file", help="sets the name of the output file")
    parser.add_argument("-c", "--codec", help="sets the codec for processing the video, refer to ffmpeg codec section in order to see which codec to use")
    parser.add_argument("-p", "--photo_format", help="the format of the pictures that are going to be converted to video")
    parser.add_argument("-f", "--fps", help="fps of the output video")
    parser.add_argument("-s", "--video_size", help="video size as used in the ffmpeg parameters, for example hd1080")
    return parser.parse_args()

def changeConfigFromArgs(parsedArgs):
    """
        Sets the optional parameters to the config object
    """
    if parsedArgs.output_file:
        config.out_name = parsedArgs.output_file
    if parsedArgs.codec:
        config.codec = parsedArgs.codec
    if parsedArgs.fps:
        config.fps = int(parsedArgs.fps)
    if parsedArgs.video_size:
        config.video_size = parsedArgs.video_size

def mergePicturesIntoVideo(folder):
    """
        Merges the pictures of a folder into a video
    """
    images = ffmpeg.input(folder+"*."+config.input_format, pattern_type="glob", framerate=config.fps)
    reescaledImages = images.filter('scale', size=config.video_size)
    return reescaledImages

def mergeFolderVideos(vidArr):
    """
        Merges the created videos containing one folder of images together
    """
    stream = vidArr[0]
    for i in range(1,len(vidArr)):
        stream = ffmpeg.concat(stream, vidArr[i])
    return stream

def exportToVideo(stream):
    """
        Exports everything into video format
    """
    out = ffmpeg.output(stream, config.out_name, codec=config.codec, format=config.video_format, crf=20, pix_fmt=config.pix_fmt)
    out.run()

def __main__():
    folderArray = []
    
    # Sets the parameters from the args
    parsedArgs = inputParser()
    folderArray = parsedArgs.input_folders
    changeConfigFromArgs(parsedArgs)

    imageStreamArr = []
    for i in range(0, len(folderArray)):
        imageStreamArr.append(mergePicturesIntoVideo(folderArray[i]))
    
    print(imageStreamArr)

    stream = mergeFolderVideos(imageStreamArr)
    exportToVideo(stream)
    
__main__()
