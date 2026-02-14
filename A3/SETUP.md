# A3 Praat Speech Processing Setup Guide

Audio feature extraction and manipulation using Praat scripting language.

## Platform Support

- **Windows** (XP+, tested with 7/10/11)
- **macOS** (10.6+, Intel and Apple Silicon, tested with Big Sur+)
- **Linux** (Ubuntu/Debian/CentOS, tested with Ubuntu 18.04+)

## Prerequisites

### 1. Praat Installation

Praat is a free speech analysis software available at: https://www.praat.org/

**Windows:**
```
Download installer from: https://www.praat.org/download_win.html
Run: praat_XXXX_win64.exe
Default install path: C:\Program Files\Praat
Add to PATH (optional, recommended)
```

**macOS (Intel):**
```
Download: praat_XXXX_osx64.dmg
Drag Praat to Applications folder
Run: /Applications/Praat.app/Contents/MacOS/Praat
```

**macOS (Apple Silicon):**
```
Download: praat_XXXX_osx_arm64.dmg
Drag Praat to Applications folder
Make sure to use native ARM64 version for best performance
```

**Linux (Ubuntu/Debian):**
```bash
sudo apt-get install praat
# or build from source: https://github.com/praat/praat
```

**Linux (CentOS/RedHat):**
```bash
sudo yum install praat
# or build from source
```

### 2. Audio Files

- WAV format (recommended: 16-bit PCM, 44.1 kHz or 16 kHz)
- MP3 support limited (Praat prefers WAV)
- Sample files should be placed in the working directory

## File Structure & Descriptions

```
A3/
├── pitch_from_wav.praat               - Extract pitch from audio
├── formant_vec_from_wav_part.praat    - Extract formants from audio
├── formant_vec_from_wav_part_mul.praat - Batch formant extraction
├── manipulate_pitch_duration_from_wav.praat - PSOLA-based manipulation
├── testCommandLineCalls.praat         - Test command-line usage
└── cmd/                               - Shell/Praat script examples
    ├── create_sin_play                - Generate and play sine wave
    ├── pitch_textGrid_man             - Pitch extraction with TextGrid
    └── read_and_play_file             - Read and play audio file
```

## Script Descriptions

### pitch_from_wav.praat
**Purpose:** Extract fundamental frequency (pitch/F0) from a WAV file

**Features:**
- Autocorrelation-based pitch detection (AC method)
- Configurable pitch range (default: 25-900 Hz)
- Cache support for faster re-analysis
- Parameter adjustment via command line

**Parameters:**
```
filename          - Path to input WAV file
minpitch          - Minimum pitch value (Hz, default: 25)
maxpitch          - Maximum pitch value (Hz, default: 900)
cache             - Use cached results if available (1/0)
moreArgs          - Additional detection parameters
```

**Output:**
- Time step (frame interval)
- Number of frames
- Pitch values for each frame (Hertz)

**Usage:**
```praat
praat pitch_from_wav.praat --open --run audio_file.wav 25 900 1
```

---

### formant_vec_from_wav_part.praat
**Purpose:** Extract formant frequencies from a specific time segment

**Features:**
- Burg-method formant analysis
- Configurable formant parameters
- Cache support for large files
- Single sample range or time-based extraction

**Parameters:**
```
filename          - Path to input WAV file
samp_start        - Sample number (or 0 for start)
samp_end          - Sample number (or 0 for end)
cache             - Use cached results (1/0)
moreArgs          - Advanced parameters
```

**Output:**
- Formant frequencies (F1, F2, F3, ... F7) in Hertz
- NaN for undefined values

**Usage:**
```praat
praat formant_vec_from_wav_part.praat --open --run audio_file.wav 0 0 1
```

---

### formant_vec_from_wav_part_mul.praat
**Purpose:** Batch extract formants from multiple time segments

**Features:**
- Process multiple segments in one call
- Efficient for database preparation
- Each segment analyzed independently
- Maintains cache for acceleration

**Parameters:**
```
filename          - Path to input WAV file
samp_starts       - Space-separated sample numbers
samp_ends         - Space-separated sample numbers
cache             - Use cached results (1/0)
moreArgs          - Advanced parameters
```

**Output:**
- Tab-delimited formant values, one line per segment

**Usage:**
```praat
praat formant_vec_from_wav_part_mul.praat --open --run \
  audio_file.wav "0 1000 2000" "500 1500 2500" 1
```

---

### manipulate_pitch_duration_from_wav.praat
**Purpose:** Modify pitch and duration of speech using PSOLA

**Features:**
- PSOLA (Pitch Synchronous OverLap Add) algorithm
- Independent pitch and duration modification
- Preserves formant structure
- Supports pitch tier and duration tier files

**Parameters:**
```
concatenatedFile  - Input WAV file
pitchFile         - PitchTier file (.PitchTier)
durationFile      - DurationTier file (.DurationTier)
outFile           - Output WAV file
minpitch          - Minimum pitch (Hz, default: 40)
maxpitch          - Maximum pitch (Hz, default: 450)
```

**Tier File Format:**
```
File type = "ooTextFile"
Object class = "PitchTier"
...
<time> <value>
```

**Usage:**
```praat
praat manipulate_pitch_duration_from_wav.praat --open --run \
  input.wav pitch.PitchTier duration.DurationTier output.wav 40 450
```

---

### CMD Scripts (Simple Examples)

#### create_sin_play
Generates a 377 Hz sine wave (sample rate: 44100 Hz) and plays it.

**Usage:**
```bash
# Interactive mode (opens Praat UI)
praat create_sin_play

# Command line mode
praat create_sin_play --run
```

---

#### pitch_textGrid_man
Extracts pitch values corresponding to TextGrid intervals.

**Requirements:**
- Select a Sound object
- Select a TextGrid object (must be created)
- Run script

**Output:**
- Tab-separated: start_time end_time mean_F0 interval_label

---

#### read_and_play_file
Reads a WAV file and plays it immediately.

**Usage:**
```bash
praat read_and_play_file
# Script will prompt for file path
```

## Cross-Platform Usage

### Running Praat Scripts from Command Line

#### Windows (PowerShell)
```powershell
$praat_path = "C:\Program Files\Praat\praat.exe"
& $praat_path script.praat --open --run

# With parameters
& $praat_path pitch_from_wav.praat --open --run "audio.wav" 75 600 1
```

#### macOS/Linux (Bash)
```bash
praat pitch_from_wav.praat --open --run "audio.wav" 75 600 1

# Full path examples
/Applications/Praat.app/Contents/MacOS/Praat pitch_from_wav.praat --open --run "audio.wav" 75 600 1
praat pitch_from_wav.praat --open --run "audio.wav" 75 600 1
```

### Path Handling Best Practices

**❌ Avoid Absolute Paths:**
```praat
sentence filename C:\Users\name\Documents\audio.wav  # Windows only
sentence filename /Users/name/Documents/audio.wav    # macOS only
```

**✓ Use Relative Paths:**
```praat
sentence filename audio.wav                          # Current directory
sentence filename ../data/audio.wav                  # Parent directory
sentence filename ./sounds/audio.wav                 # Explicit current dir
```

**✓ Use Environment Variables:**
```bash
# Set working directory
cd /path/to/audio/files
praat pitch_from_wav.praat --open --run "audio.wav" 75 600 1
```

## Current Code Status & Multi-OS Readiness

### Issues Identified

| Issue | Files | Platform Impact | Severity |
|-------|-------|-----------------|----------|
| Hardcoded Windows paths | All `.praat` files | Windows only | HIGH |
| Backslash path separators | All `.praat` files | Windows only | HIGH |
| No platform detection | All files | General | MEDIUM |
| Temporary paths hard to configure | `manipulate_pitch_duration_from_wav.praat` | All platforms | MEDIUM |

### Specific Script Hardcoding

1. **pitch_from_wav.praat** (Line 1)
   ```praat
   sentence filename C:\Users\yuzba\Documents\HIT\Speech\HandsOn3\Al_page_13_78.wav
   ```

2. **formant_vec_from_wav_part.praat** (Line 2)
   ```praat
   sentence filename C:\Users\yuzba\Documents\HIT\Speech\Al_page_13_78.wav
   ```

3. **formant_vec_from_wav_part_mul.praat** (Line 2)
   ```praat
   sentence filename C:\Users\yuzba\Documents\HIT\Speech\HandsOn3\Al_page_13_78.wav
   ```

4. **manipulate_pitch_duration_from_wav.praat** (Lines 1-4)
   ```praat
   sentence concatenatedFile C:\Users\MOTIZ~1\AppData\Local\Temp\Vivotext\...
   # Multiple hardcoded temporary file paths
   ```

5. **cmd/read_and_play_file** (Line 1)
   ```praat
   Read from file: "C:\Users\yuzba\Documents\HIT\Speech\Al_page_13_78.wav"
   ```

### Recommended Improvements

#### 1. Remove Hardcoded Paths
```praat
# BEFORE
sentence filename C:\Users\yuzba\Documents\HIT\Speech\Al_page_13_78.wav

# AFTER
sentence filename audio.wav
```

#### 2. Add Platform Detection
```praat
procedure getPlatformPath .filename$
    # Praat automatically handles / and \ on all platforms
    # Just use forward slashes or relative paths
endproc
```

#### 3. Use Environment Variables
```praat
# Get home directory
homedir$ = unicode$ (home$)
datadir$ = homedir$ + "/speech_data/"
```

#### 4. Better Default Paths
```praat
sentence filename ./audio/sample.wav
# Or
sentence filename specifyFileLocation
```

## Running Scripts Safely on Multiple Platforms

### Method 1: Direct Script Execution
```bash
# All platforms - must be in same directory
praat pitch_from_wav.praat --open --run "myaudio.wav" 25 900 1
```

### Method 2: Batch Processing (Recommended)
Create a wrapper script to manage paths:

```praat
# process_audio.praat
path$ = chooseReadFile$: "Select audio file"
if path$ <> ""
    call run_pitch_analysis: path$
    call run_formant_analysis: path$
endif

procedure run_pitch_analysis: .file$
    runScript: "pitch_from_wav.praat", .file$, "25", "900", "1"
endproc
```

### Method 3: Interactive GUI
1. Use Praat's built-in `chooseReadFile$()` and `chooseWriteFile$()`
2. Scripts automatically follow platform conventions
3. No hardcoding needed

## File Format Support

**Input Audio:**
- WAV (recommended)
- AIFF
- AU
- MP3 (limited platform support)
- FLAC (version dependent)

**Output Format:**
- WAV (standard)
- AIFF
- AU
- Raw

**Tier Formats:**
- PitchTier (.PitchTier)
- DurationTier (.DurationTier)
- TextGrid (.TextGrid)

## Environment Setup

### Windows
```batch
REM Add Praat to PATH (after installation)
set PATH=%PATH%;C:\Program Files\Praat
praat pitch_from_wav.praat --open --run "audio.wav" 25 900 1
```

### macOS
```bash
# Add to ~/.zshrc or ~/.bash_profile
alias praat="/Applications/Praat.app/Contents/MacOS/Praat"

# Then use directly
praat pitch_from_wav.praat --open --run "audio.wav" 25 900 1
```

### Linux
```bash
# Praat should be in PATH after installation
which praat
# Then use directly
praat pitch_from_wav.praat --open --run "audio.wav" 25 900 1
```

## Troubleshooting

### Issue: "Script not found" or "File not found"
- Ensure you're in the correct directory
- Use absolute paths if relative paths don't work
- Check file permissions

### Issue: Audio file not found
- Verify the file exists in the specified path
- Use forward slashes (/) - Praat converts them automatically
- Avoid spaces in filenames or use quotes

### Issue: Parameter mismatch
- Check parameter order against documentation
- Verify parameter types (text, real, integer, boolean)
- Use `--verbose` flag for debugging

### Issue: Out of memory
- Praat loads entire files into RAM
- Use `formant_vec_from_wav_part.praat` for large files
- Cache can help with repeated operations

### Issue: Different results on different platforms
- Audio processing algorithms work identically
- Results should be identical across platforms
- Differences are due to file paths, not computation

## Performance Tips

1. **Use Caching** - Enable caching for repeated analyses
2. **Process in Batches** - Use `_mul` versions for multiple files
3. **Monitor Memory** - Praat loads files entirely in RAM
4. **Parallel Processing** - Run multiple Praat instances (with different file locks)

## Resources

- [Praat Manual](https://www.fon.hum.uva.nl/praat/manual/)
- [Praat Scripting Documentation](https://www.fon.hum.uva.nl/praat/manual/scripting.pdf)
- [Praat Forums](https://www.praat.org/forums/)
- [Praat GitHub Repository](https://github.com/praat/praat)

## Known Limitations

1. **File Paths** - Must be text (converted to platform-native)
2. **Maximum File Size** - Limited by available RAM
3. **Real-Time Processing** - Praat processes entire files at once
4. **Parallel Processing** - File locking may prevent concurrent access

## Cross-Platform Compatibility Checklist

- [ ] Praat installed on all target platforms
- [ ] Audio files in WAV format (16-bit PCM)
- [ ] Scripts use relative paths only
- [ ] No hardcoded directory separators
- [ ] Parameters properly quoted
- [ ] Data files copied to working directory
- [ ] File permissions set correctly
- [ ] PATH environment variable configured

## Next Steps

1. Install Praat on your platform
2. Place audio files in project directory
3. Edit scripts to remove hardcoded paths
4. Test scripts individually first
5. Combine scripts for batch processing
