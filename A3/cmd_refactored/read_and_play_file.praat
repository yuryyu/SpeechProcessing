# read_and_play_file.praat
# Cross-platform audio file reader and player
#
# Description:
#   Interactive script that prompts user to select an audio file,
#   validates it, loads it, and plays it.
#   Provides clear error messages if anything goes wrong.
#
# Usage:
#   praat read_and_play_file.praat --open --run
#
# Compatibility:
#   ✓ Windows    (All versions with Praat)
#   ✓ macOS      (Intel and Apple Silicon)
#   ✓ Linux      (Ubuntu, Debian, CentOS, etc.)
#
# Input:
#   User selects audio file via file browser dialog
#
# Supported Formats:
#   - WAV (recommended: 16-bit PCM)
#   - AIFF
#   - AU
#   - MP3 (limited support)
#   - FLAC (version dependent)
#
# Output:
#   Audio playback + console messages

# Get platform info for debugging (optional)
appendInfoLine: "Platform: ", osVersion$
appendInfoLine: ""

# Step 1: Prompt user to select audio file
writeInfoLine: "Select an audio file to play..."
filename$ = chooseReadFile$: "Select an audio file:"

# Step 2: Validate file selection
if filename$ = ""
    exitScript: "ERROR: No file selected - operation cancelled"
endif

# Step 3: Validate file exists and is readable
if not fileReadable (filename$)
    exitScript: "ERROR: File not readable: " + newline$ + filename$
endif

# Step 4: Display filename being processed
writeInfoLine: "Loading: ", filename$

# Step 5: Load audio file
try
    Read from file: filename$
catch
    exitScript: "ERROR: Failed to load audio file" + newline$ + 
    ... "This may not be a valid audio file." + newline$ + 
    ... "Try: WAV, AIFF, or AU format"
endtry

# Step 6: Validate audio was loaded
if numberOfSelected ("Sound") <> 1
    exitScript: "ERROR: Failed to load audio file correctly"
endif

# Step 7: Get audio properties
appendInfoLine: "Loaded successfully!"
selectObject: selected ("Sound")
duration = Get total duration
sample_rate = Get sampling frequency (Hz)
channels = Get number of channels
bit_depth = Get bit depth

# Step 8: Display audio information
appendInfoLine: ""
appendInfoLine: "Audio Properties:"
appendInfoLine: "  Duration: ", fixed$ (duration, 2), " seconds"
appendInfoLine: "  Sample rate: ", fixed$ (sample_rate, 0), " Hz"
appendInfoLine: "  Channels: ", channels
appendInfoLine: "  Bit depth: ", bit_depth, " bits"
appendInfoLine: ""
appendInfoLine: "Playing..."

# Step 9: Play the audio
Play

# Step 10: Confirm completion
appendInfoLine: "Playback complete"
appendInfoLine: ""
appendInfoLine: "Optional: Save this sound to a file"
appendInfoLine: "  Save as WAV file... output.wav"
appendInfoLine: "  Save as AIFF file... output.aiff"
