import srt
import re
import codecs
from pathlib import Path
import subprocess
import glob
def cut(timestamps):
    vf = ""
    for i in range(len(timestamps)):
        current = timestamps[i]
        if i != 0:
            vf += "+"
        vf += f"between(t,{current[0]},{current[1]})"
    vf += ""
    return vf

def segments(timestamps, name):
    ss = []
    for i in range(len(timestamps)):
        current = timestamps[i]
        ss += ["-t", str(current[1]-current[0]), f"out_2/{name}_{i}.mkv", "-ss", str(current[0])]
    return ss

for name in glob.glob('**/*.srt'):
    path = Path(name)
    stem = path.stem
    print(name)
    with open(name, "rb") as f:
        r_enc = codecs.getreader("utf-8-sig")
        lines = r_enc(f).read()
        subs = list(srt.parse(lines))
        sense = []
        for sub in subs:
            if len(sub.content) > 0 and (re.search("sense", sub.content) or re.search("kinda", sub.content)):
                #print(sub)
                sense.append([sub.start.seconds, sub.end.seconds])
        select = segments(sense, stem)
        #print(select)
        #print( ' '.join(["ffmpeg", "-i", f"{stem}/{stem}_room.mkv","-vf", f"\"select='{select}',setpts=N/FRAME_RATE/TB\"","-af", f"\"aselect='{select}',asetpts=N/SR/TB\"", f"out/{stem}.mkv"]))
        #subprocess.run(["ffmpeg", "-i", f"{stem}/{stem}_room.mkv","-vf", f"select='{select}',setpts=N/FRAME_RATE/TB","-af", f"aselect='{select}',asetpts=N/SR/TB", f"out/{stem}.mkv"], capture_output=True, check=True)
        subprocess.run(["ffmpeg", "-i", f"{stem}/{stem}_room.mkv", *select], capture_output=True, check=True)
        #print(srt.compose(sense))
