# Import everything needed to edit video clips
from moviepy.editor import *

# loading video dsa gfg intro video
clip = VideoFileClip("Video01.webm")

# clipping of the video
# getting video for only starting 10 seconds
clip = clip.subclip(0, 10)

# rotating video by 180 degree
clip = clip.rotate(180)

# Reduce the audio volume (volume x 0.5)
clip = clip.volumex(0.5)

# showing clip
clip.ipython_display(width = 280)
