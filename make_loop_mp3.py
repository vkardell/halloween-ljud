# ABOUTME: Encodes an audio file (WAV, OGG, MP3, FLAC) to MP3, repeated back to back a given number of times.
# ABOUTME: Usage: make_loop_mp3.py <in> <out.mp3> <repeats>
import sys
import numpy as np
import soundfile as sf

src, dst, repeats = sys.argv[1], sys.argv[2], int(sys.argv[3])
audio, rate = sf.read(src, always_2d=True)
sf.write(dst, np.tile(audio, (repeats, 1)), rate, format='MP3', bitrate_mode='CONSTANT', compression_level=0.3)
