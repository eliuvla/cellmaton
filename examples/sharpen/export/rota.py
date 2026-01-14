from moviepy.editor import *
import os
import moviepy.video.fx.all as vfx
import moviepy.editor as mp
from moviepy.video.fx.resize import resize
import random

r = os.path.realpath(__file__).replace("\\","/").replace("rota.py","")

clips = []

num_images = 59


#duración en frames
duration = [4]*num_images


for j in range(0,2):
    for i in range(0,num_images):
        clips.append(ImageClip(r+str(i+1)+".png",duration= duration[i]/30))


result = mp.concatenate_videoclips(clips, method="compose")


#invert = result.fx(vfx.invert_colors)


#result.preview(fps=30)

result.write_videofile(r+"sharpen.mp4",threads = 4 ,fps=30)


#invert.write_videofile(r+"pruebainvert.mp4",fps=30)
#CompositeVideoClip( [txtClip.set_pos('center')], size=screensize)