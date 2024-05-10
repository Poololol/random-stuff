from moviepy.editor import *
clips = []
currentSeason = 'Winter 2024'
info = [('17.567', '5k', '24:13')]
for i in range(18):
    clips.append((VideoFileClip(f'Video{i+1}.webm'),TextClip(f'{currentSeason} {i+1}/n PB:{info[i][0]}/n Top {info[i][1]} World/n Total Time Spent: {info[i][2]}')))
final = concatenate_videoclips((clips[0][0], clips[0][1]))
final.write_videofile(f"{currentSeason} PB's.mp4")(f