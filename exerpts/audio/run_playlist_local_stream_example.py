import audioserver.dynamic_audio_generator
import audioserver.stream_player

playlist = ["../../sounds/sawing_wood.wav", "../../sounds/fanfare.wav"]
audioserver.dynamic_audio_generator.run_playlist(playlist)

while True:
    audioserver.stream_player.add_sound_to_stream(audioserver.dynamic_audio_generator.pop_buffered_array())
