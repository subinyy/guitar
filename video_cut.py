from moviepy.editor import *
print("video file name :")
videofilename = input()
print("clip frame text file name :")
textfilename = input()
clip = VideoFileClip(videofilename)
fps = clip.fps
num=1
print("read video file "+videofilename+"  fps:"+str(fps))

noncuttedTimings=[]
with open(textfilename) as file:
    lines = file.readlines()
    for line in lines:
        line_arr = line.split()
        start_time = float(line_arr[0])/fps
        end_time = float(line_arr[1])/fps
        noncuttedTimings.append(start_time)
        noncuttedTimings.append(end_time)
        print("#"+str(num)+": sub clipping "+str(start_time)+" ~ "+str(end_time))
        subclip = clip.subclip(start_time, end_time)
        subclip.write_videofile(videofilename.split('.')[0]+" "+str(num)+'.'+videofilename.split('.')[1])
        num=num+1

print('done. will you cut non-cutted parts? (yes/no, default=no)')
ddddd=input()
if ddddd=="yes":
    dddd=1
    while dddd+1<len(noncuttedTimings):
        start_time=noncuttedTimings[dddd]
        end_time=noncuttedTimings[dddd+1]
        if start_time>end_time:
            continue
        print("#"+str(num)+": sub clipping "+str(start_time)+" ~ "+str(end_time))
        subclip = clip.subclip(start_time, end_time)
        subclip.write_videofile(videofilename.split('.')[0]+" nocut "+str(dddd/2+1)+'.'+videofilename.split('.')[1])
        dddd+=2

clip.close()
