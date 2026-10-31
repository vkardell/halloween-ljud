# ABOUTME: Cuts leading silence from CBR MP3 files on frame boundaries, without re-encoding.
# ABOUTME: Usage: trim_mp3.py <in.mp3> <out.mp3> <seconds to drop>
import sys
BR = [0,32,40,48,56,64,80,96,112,128,160,192,224,256,320]
src, dst, drop_s = sys.argv[1], sys.argv[2], float(sys.argv[3])
b = open(src, 'rb').read()
frames, i = [], 0
while i + 4 <= len(b) and b[i] == 0xFF and (b[i+1] & 0xE0) == 0xE0:
    br = BR[b[i+2] >> 4] * 1000; pad = (b[i+2] >> 1) & 1
    ln = 144 * br // 44100 + pad
    frames.append(b[i:i+ln]); i += ln
assert i == len(b), "unparsed bytes"
audio = frames[1:] if (b'Xing' in frames[0] or b'Info' in frames[0]) else frames
skip = int(drop_s * 44100 / 1152)
open(dst, 'wb').write(b''.join(audio[skip:]))
print(f"{dst.split('/')[-1]}: dropped {skip} frames = {skip*1152/44100:.3f} s")
