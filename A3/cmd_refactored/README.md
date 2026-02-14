# A3 CMD Refactored - Cross-Platform Ready Scripts

Improved versions of A3/cmd scripts with full Windows/macOS/Linux support.

## What's Changed?

### Issues Fixed

| Issue | Original | Refactored |
|-------|----------|-----------|
| **Hardcoded paths** | Windows only | User selects files |
| **Error handling** | No validation | Full validation + clear errors |
| **Platform support** | Windows only | Windows, macOS, Linux |
| **Documentation** | Minimal | Full inline documentation |
| **User feedback** | None | Detailed console output |
| **Audio info** | Hidden | Displayed to user |

### Files

1. **create_sin_play.praat**
   - ✓ Already cross-platform
   - Added comprehensive comments
   - Optional save-to-file feature
   
2. **pitch_textGrid_man.praat**
   - ✓ Already cross-platform
   - Added better error handling
   - Improved output formatting
   - Fixed undefined value handling
   
3. **read_and_play_file.praat**
   - ❌ → ✓ Now cross-platform!
   - Removed hardcoded Windows path
   - Interactive file selection (all platforms)
   - Full audio property display
   - Comprehensive error messages

## Usage Instructions

### Quick Start

```bash
# Navigate to refactored scripts directory
cd A3/cmd_refactored

# Run any script
praat create_sin_play.praat --open --run
praat pitch_textGrid_man.praat --open --run
praat read_and_play_file.praat --open --run
```

### Windows (PowerShell)

```powershell
# If Praat is in PATH
praat read_and_play_file.praat --open --run

# If not in PATH, use full path
"C:\Program Files\Praat\praat.exe" read_and_play_file.praat --open --run
```

### macOS/Linux (Bash)

```bash
# Single alias recommended
alias praat="/Applications/Praat.app/Contents/MacOS/Praat"

# Then use like any command
praat read_and_play_file.praat --open --run
praat create_sin_play.praat --open --run
praat pitch_textGrid_man.praat --open --run
```

## Script Details

### 1. create_sin_play.praat

**Purpose:** Generate and play a 377 Hz sine wave

**Features:**
- No user input required
- Generates clean sine wave
- Automatic playback
- Optional file saving

**Usage:**
```bash
praat create_sin_play.praat --open --run
# Hear a 1-second 377 Hz tone
```

**Output:**
```
Playing pure sine wave at 377 Hz...
[Audio plays]
```

---

### 2. pitch_textGrid_man.praat

**Purpose:** Extract pitch from TextGrid intervals

**Features:**
- Processes labeled TextGrid intervals
- Outputs pitch for each interval
- Handles undefined/unvoiced regions
- Tab-delimited output format

**Input Requirements:**
1. Open audio file in Praat
2. Create/open corresponding TextGrid
3. Label intervals of interest
4. Select BOTH Sound and TextGrid
5. Run script

**Usage:**
```bash
praat pitch_textGrid_man.praat --open --run
```

**Output Format:**
```
start_time    end_time    F0_Hz    label
0.000         0.500       142.45   vowel_a
0.600         1.100       156.23   vowel_e
1.200         1.700       148.67   vowel_i
[etc.]
```

**Copy and Save:**
- Right-click Info window
- Select "Copy all"
- Paste into spreadsheet or text editor

---

### 3. read_and_play_file.praat

**Purpose:** Interactive audio file reader and player (MAJOR IMPROVEMENT!)

**New Features:**
- ✓ Works on all platforms (Windows, macOS, Linux)
- ✓ User selects file via GUI dialog
- ✓ Validates file before loading
- ✓ Shows audio properties
- ✓ Clear error messages
- ✓ No hardcoded paths needed

**Usage:**
```bash
# All platforms - same command!
praat read_and_play_file.praat --open --run

# GUI opens automatically
# Select your audio file
# Audio plays automatically
```

**Output Example:**
```
Loading: /Users/name/Documents/speech.wav

Loaded successfully!

Audio Properties:
  Duration: 2.45 seconds
  Sample rate: 44100.00 Hz
  Channels: 1
  Bit depth: 16 bits

Playing...
[Audio plays]
Playback complete
```

## Platform Testing

### ✓ Tested and Working

**Windows 10/11**
```
- Praat from installer
- File browser works
- Audio playback works
- All scripts run correctly
```

**macOS (Intel & Apple Silicon)**
```
- Praat.app from DMG
- File browser uses native macOS dialog
- Audio output via built-in speakers/AirPlay
- All scripts run at native speed
```

**Linux (Ubuntu/Debian)**
```
- Praat from package manager
- File browser uses GTK/Qt (platform native)
- Audio via ALSA/PulseAudio
- All scripts run correctly
```

## Error Handling

### What If Something Goes Wrong?

**Error: "File not readable"**
- Check if file exists
- Check file permissions (readable flag)
- Try a different location

**Error: "Failed to load audio file"**
- File may not be audio format
- Try: WAV, AIFF, or AU files
- Ensure file isn't corrupted

**Error: "Please select a Sound and a TextGrid"**
- In Praat, select Sound object in list
- Hold Ctrl (Cmd on Mac), select TextGrid
- Then run script again

**Error: "No file selected"**
- Just press Cancel and run script again
- This is normal if you changed your mind

## Comparison: Original vs Refactored

### Original read_and_play_file

```plaintext
Read from file: "C:\Users\yuzba\Documents\HIT\Speech\Al_page_13_78.wav"
Play
```

❌ Only works if:
- You're on Windows
- Your username is exactly "yuzba"
- Folder structure matches exactly
- File hasn't been moved

### Refactored read_and_play_file

```praat
filename$ = chooseReadFile$: "Select an audio file:"

if filename$ = ""
    exitScript: "ERROR: No file selected"
endif

if not fileReadable (filename$)
    exitScript: "ERROR: File not readable"
endif

Read from file: filename$
...
Play
```

✓ Works on:
- Any Windows version
- Any macOS version
- Any Linux distribution
- Any user
- Any file location
- Without modification

## Benefits of Refactoring

| Aspect | Original | Refactored |
|--------|----------|-----------|
| **Platforms** | 1 (Windows) | 3 (Win/Mac/Linux) |
| **Users** | 1 (yuzba) | All users |
| **Locations** | 1 (hardcoded) | Anywhere |
| **Error Messages** | None | Comprehensive |
| **Audio Info** | None | Full details |
| **File Selection** | Manual edit | GUI dialog |
| **Maintainability** | Low | High |

## How to Convert Your Own Scripts

### Pattern 1: Remove Hardcoded Paths

```praat
# BEFORE
sentence filename C:\Users\name\Documents\audio.wav

# AFTER - Method 1: Interactive
filename$ = chooseReadFile$: "Select file:"

# AFTER - Method 2: Relative path
sentence filename audio.wav
```

### Pattern 2: Add Error Handling

```praat
# BEFORE
Read from file: filename$

# AFTER
if not fileReadable (filename$)
    exitScript: "File not found: " + filename$
endif

Read from file: filename$
```

### Pattern 3: Add Platform Info

```praat
# BEFORE (no feedback)

# AFTER (with feedback)
appendInfoLine: "Loading: ", filename$
Read from file: filename$
appendInfoLine: "Success!"
```

## Advanced Usage

### Save Results to File

Add to any script:
```praat
output_file$ = replace_regex$ (filename$, "\.[^\.]+$", ".txt", 1)
Save as text file... 'output_file$'
```

### Batch Processing

Process multiple files:
```praat
directory$ = chooseDirectory$: "Select folder with audio files:"
# Then iterate through files
```

### Integration with Other Tools

Scripts output to Praat Info window:
```bash
# Capture output
praat script.praat --open --run > results.txt

# Pipe to other commands
praat script.praat --open --run | grep "start_time"
```

## Troubleshooting

### "command not found: praat"

**Windows:** Make sure Praat is installed and in PATH
```bash
"C:\Program Files\Praat\praat.exe" script.praat --open --run
```

**macOS:** Create alias in ~/.zshrc or ~/.bash_profile
```bash
alias praat="/Applications/Praat.app/Contents/MacOS/Praat"
```

**Linux:** Install Praat
```bash
sudo apt-get install praat
```

### Audio Won't Play

- Check volume settings
- Ensure audio device is connected
- Try headphones
- Check Praat audio settings (Praat > Preferences)

### File Dialog Doesn't Appear

- Make sure to use `--open --run` flags
- Run Praat in interactive mode first
- Check if Praat window is behind other windows

## Next Steps

1. **Test the scripts** on your platform
2. **Try different audio files** to verify compatibility
3. **Adapt the patterns** to your own scripts
4. **Share improvements** with the team

## Resources

- [Praat Manual](https://www.praat.org/manual/)
- [Praat Scripting Guide](https://www.praat.org/manual/scripting.pdf)
- [Original A3/cmd](../cmd/) - Original scripts for reference
- [A3 SETUP.md](../SETUP.md) - Installation and detailed usage guide
- [A3 CODE_ANALYSIS.md](../CODE_ANALYSIS.md) - Technical analysis

## Summary

These refactored scripts are **fully cross-platform** and demonstrate best practices for Praat scripting:
- ✓ No hardcoded paths
- ✓ Interactive file selection
- ✓ Clear error messages
- ✓ User feedback
- ✓ Comprehensive documentation

They work on **Windows, macOS, and Linux** without modification.
