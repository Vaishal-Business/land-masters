from pydub.generators import Sine
from pydub import AudioSegment

# Generate deep bass
bass = Sine(50).to_audio_segment(duration=3000).apply_gain(-10)  # 50 Hz low tone for 3 seconds

# Generate a rising tone for tension
rise = AudioSegment.silent(duration=1000)  # Start with silence
for freq in range(200, 1000, 50):  # Gradually increase frequency
    rise += Sine(freq).to_audio_segment(duration=50).apply_gain(-15)

# Create a drum hit (low-frequency impact)
drum_hit = Sine(100).to_audio_segment(duration=100).apply_gain(-5).fade_out(100)

# Add a sharp climax (high-frequency stinger)
stinger = Sine(800).to_audio_segment(duration=500).apply_gain(-3).fade_out(200)

# Layer the elements for cinematic effect
music = bass.overlay(rise, position=1000)  # Add rising tension after 1 second
music = music.overlay(drum_hit, position=4000)  # Add drum hit at 4 seconds
music = music.overlay(stinger, position=4500)  # Add stinger at the climax

# Export the final audio
music.export("villain_theme_custom.wav", format="wav")
print("Villain reveal music created successfully!")
