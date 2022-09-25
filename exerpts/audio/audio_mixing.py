from pydub import AudioSegment
from pydub.playback import play
import audiosegment

sound1 = audiosegment.from_file("../../sounds/fanfare.wav")
sound2 = audiosegment.from_file("../../sounds/test.wav")

combined = sound1.overlay(sound2)

frames = combined.generate_frames_as_segments(5000, True)

first_frame,_ = next(frames)
byte_str = first_frame.serialize()

combined_back = audiosegment.deserialize(byte_str)

play(combined_back)