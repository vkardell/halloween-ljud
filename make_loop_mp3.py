# ABOUTME: Encodes an audio file (WAV, OGG, MP3, FLAC) to MP3, repeated back to back a given number of times.
# ABOUTME: Usage: make_loop_mp3.py <in> <out.mp3> <repeats> [--crossfade s] [--start s] [--end s] [--gain-db dB]
import argparse
import numpy as np
import soundfile as sf

parser = argparse.ArgumentParser()
parser.add_argument('src')
parser.add_argument('dst')
parser.add_argument('repeats', type=int)
parser.add_argument('--crossfade', type=float, default=0.0, help='seconds each repeat overlaps the previous one')
parser.add_argument('--start', type=float, default=0.0, help='seconds cut from the start, e.g. a fade-in')
parser.add_argument('--end', type=float, default=None, help='second where the source is cut off, e.g. before a fade-out')
parser.add_argument('--gain-db', type=float, default=0.0, help='level change, for sources much quieter than the rest')
args = parser.parse_args()

audio, rate = sf.read(args.src, always_2d=True)
end = int(args.end * rate) if args.end is not None else len(audio)
audio = audio[int(args.start * rate):end] * 10 ** (args.gain_db / 20)

# Each repeat overlaps the previous one by the crossfade, so ambience that does not loop on its own has no seam.
# Equal-power curves keep noise-like ambience (wind, rain) from dipping in loudness halfway through the fade.
overlap = int(args.crossfade * rate)
phase = np.linspace(0.0, np.pi / 2, overlap)[:, None]
fade_in, fade_out = np.sin(phase), np.cos(phase)
looped = audio
for _ in range(args.repeats - 1):
    if overlap:
        seam = looped[-overlap:] * fade_out + audio[:overlap] * fade_in
        looped = np.concatenate([looped[:-overlap], seam, audio[overlap:]])
    else:
        looped = np.concatenate([looped, audio])
sf.write(args.dst, np.clip(looped, -1.0, 1.0), rate, format='MP3', bitrate_mode='CONSTANT', compression_level=0.3)
