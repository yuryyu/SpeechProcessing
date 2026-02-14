# create_sin_play.praat
# Cross-platform sine wave generator and player
# 
# Description:
#   Creates a pure 377 Hz sine wave and plays it immediately
#   No user input required
#
# Usage:
#   praat create_sin_play.praat --open --run
#
# Compatibility:
#   ✓ Windows
#   ✓ macOS (Intel and Apple Silicon)
#   ✓ Linux (Ubuntu, Debian, CentOS)
#
# Parameters:
#   None - generates fixed 377 Hz sine wave

# Create a 1-second sine wave at 377 Hz
# Sample rate: 44100 Hz
# Amplitude: 1/2
Create Sound from formula: "sine", 1, 0.0, 1.0, 44100, "1/2 * sin(2*pi*377*x)"

# Play the generated sound
Play

# Optional: Save to file
# Uncomment lines below to save output
# Save as WAV file... sine_377Hz.wav
# appendInfoLine: "Saved to: sine_377Hz.wav"

# Optional: Display sound object properties
# appendInfoLine: "Frequency: 377 Hz"
# appendInfoLine: "Duration: 1.0 second"
# appendInfoLine: "Sample rate: 44100 Hz"
