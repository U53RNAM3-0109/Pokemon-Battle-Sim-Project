from pygame import mixer as mx
import random
from os import walk


def play_random_battle():
    tracks = next(walk('music/'), (None, None, []))[2]  # [] if no file
    track = random.choice(tracks)

    mx.music.load(f'music/{track}')
    mx.music.play()
