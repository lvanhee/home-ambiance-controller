import audiosegment
from pydub.playback import play

music = audiosegment.from_file("D:\perso\sounds\\3 Mirror Stage [TFreCAdHWkA].mp3")
print("framerate:"+str(music.frame_rate)+" "+str(music.to_numpy_array().size))

music_2 = music.resample(22000)
print("framerate:"+str(music_2.frame_rate)+" "+str(music_2.to_numpy_array().size))
play(music_2)
