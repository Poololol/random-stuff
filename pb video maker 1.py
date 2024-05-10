from moviepy.editor import *
clips = []
currentSeason = 'Winter 2024'
info = [('17.567', '4758', '1:24:13')]
for i in range(1):
    video = VideoFileClip(f'Video{i+1}.webm')
    mapNum = i+1 if i>9 else f'0{i+1}'
    text = TextClip(method='caption', size=(999, 200), align='West', txt=f'{currentSeason} - {mapNum}\nPB: {info[i][0]}\nTop {info[i][1]} World\nTime Spent: {info[i][2]}', color='white')
    clip = CompositeVideoClip((video, text))
    clip.duration = 51
    clips.append(clip)
final = concatenate_videoclips(clips)
#final.duration = 51
final.write_videofile(filename=f"{currentSeason} PB's.mp4", audio=False)