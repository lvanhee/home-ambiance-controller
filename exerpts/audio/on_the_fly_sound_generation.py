import audioserver.dynamic_audio_generator as dynagen
from pydub.playback import play
import audiosegment

from time import sleep


music = audiosegment.from_file("../../sounds/fanfare.wav")
music = music.resample(sample_rate_Hz=44100, sample_width=2, channels=2)

sound1 = audiosegment.from_file("../../sounds/heartbeat.wav")
sound1 = sound1.resample(sample_rate_Hz=44100, sample_width=2, channels=2)

dynagen.repeat_forever(sound1, 1)
dynagen.blend_sound_once_at_start_of_stream(music)

sleep(5)
print("play")
play(audiosegment.from_numpy_array(dynagen.pop_buffered_array(),dynagen.FRAMERATE))
print("play2")
play(audiosegment.from_numpy_array(dynagen.pop_buffered_array(),dynagen.FRAMERATE))
