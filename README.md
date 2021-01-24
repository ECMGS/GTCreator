# GTCreator
Creates a video time-lapses for a series of images

GTCreator uses the python-ffmpeg library to automate the process of creating timelapses from a series of still images stored in different folders, exponentially reducing the complexity of the process, and allows you to configure a series of parametters so that you don't have to specify everything everytime

**installation:**

```
   pip install GTCreator
```

**usage:**

Basic timelapse

```
   GTCreator -i <input-folders> -o <output file>.mp4
```

this command will create a mp4 output file with a resolution of 1920x1080 @ 25 fps using the libx264 encoding library and yuv420p pixel format

for example, this command will create a timelapse using files from two different folders:

```
   GTCreator -i ~/100GOPRO ~/101GOPRO -o timelapse.mp4
```

**Options**

-h --help:            Shows the help
-i --input_folders:   The input folders to be imported
-c --codec:           The codec for processing the video, refer to ffmpeg codec section in order to see which codec to use
-p --photo_format:    The format of the pictures that are going to be converted to video
-f --fps:             FPS of the output video
-s --video_size:      The video size as specified in the ffmpeg library, for example hd1080 or hd720
