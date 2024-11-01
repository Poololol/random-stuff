from moviepy.editor import *
import os
clips = []
currentSeason = 'Fall 2022'
info = [('17.567', '4758', '1:24:13')]
os.chdir(f'{currentSeason}')
for i in range(1):
    video = VideoFileClip(f'Poololol53_{currentSeason} - {i+1 if i>9 else f"0{i+1}"}_PersonalBest_TimeAttack.Replay.gbx')
    mapNum = i+1 if i>9 else f'0{i+1}'
    text = TextClip(method='caption', size=(999, 200), align='West', txt=f'{currentSeason} - {mapNum}\nPB: {info[i][0]}\nTop {info[i][1]} World\nTime Spent: {info[i][2]}', color='white')
    clip = CompositeVideoClip((video, text))
    clip.duration = 51
    clips.append(clip)
final = concatenate_videoclips(clips)
#final.duration = 51
final.write_videofile(filename=f"{currentSeason} PB's.mp4", audio=False)