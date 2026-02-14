# A3 CMD Code Analysis & Multi-OS Readiness Report

## Executive Summary

The A3/cmd subfolder contains simple Praat scripts designed for command-line execution. These scripts have **LOW cross-platform readiness** due to hardcoded absolute Windows paths and insufficient platform abstraction.

**Current Status:** ⚠️ **Not multi-OS ready** (Windows only)
**Effort to Fix:** 🔧 **Low** (Remove paths, make relative)

---

## File-by-File Analysis

### 1. create_sin_play

**Status:** ✓ **Cross-Platform Ready**

```plaintext
Create Sound from formula: "sine", 1, 0.0, 1.0, 44100, "1/2 * sin(2*pi*377*x)"
Play
```

**Analysis:**
- No file I/O operations
- No hardcoded paths
- Pure mathematical formula execution
- Works identically on all platforms

**Compatibility:**
- ✓ Windows
- ✓ macOS
- ✓ Linux

**Score:** 10/10 - No changes needed

---

### 2. pitch_textGrid_man

**Status:** ✓ **Cross-Platform Ready**

```plaintext
if numberOfSelected ("Sound") <> 1 or numberOfSelected ("TextGrid") <> 1
    exitScript: "Please select a Sound and a TextGrid first."
endif
...
```

**Analysis:**
- Interactive script (no file parameters)
- User selects files via GUI
- GUI abstraction handles platform differences
- All operations on in-memory objects

**Compatibility:**
- ✓ Windows
- ✓ macOS  
- ✓ Linux

**Strengths:**
- No hard-coded paths needed
- Works with UI file selection
- Platform-agnostic

**Score:** 10/10 - No changes needed

---

### 3. read_and_play_file

**Status:** ❌ **NOT Cross-Platform Ready**

```plaintext
Read from file: "C:\Users\yuzba\Documents\HIT\Speech\Al_page_13_78.wav"
Play
```

**Analysis:**

| Issue | Severity | Impact |
|-------|----------|--------|
| Hardcoded Windows absolute path | HIGH | File not found on Mac/Linux |
| Backslash path separator | HIGH | Invalid on Mac/Linux |
| No file existence check | MEDIUM | Silent failure |
| No error handling | MEDIUM | Unclear what went wrong |

**Current Incompatibilities:**

**❌ Windows:**
```plaintext
Read from file: "C:\Users\yuzba\Documents\HIT\Speech\Al_page_13_78.wav"
# Valid but hardcoded for specific user
```

**❌ macOS:**
```plaintext
Read from file: "C:\Users\yuzba\Documents\HIT\Speech\Al_page_13_78.wav"
# ERROR: File not found
# - Backslash interpreted as escape character
# - Windows user path doesn't exist
# - Entire command fails
```

**❌ Linux:**
```plaintext
Read from file: "C:\Users\yuzba\Documents\HIT\Speech\Al_page_13_78.wav"
# ERROR: File not found
# - Path structure incorrect for Linux
# - No such user or directory
# - Backslash treated as literal character
```

**Score:** 1/10 - Not usable outside Windows

---

## Multi-OS Readiness Matrix

```
Script                  Windows    macOS      Linux      Overall
─────────────────────────────────────────────────────────────────
create_sin_play         ✓ 10/10    ✓ 10/10    ✓ 10/10    ✓ 10/10
pitch_textGrid_man      ✓ 10/10    ✓ 10/10    ✓ 10/10    ✓ 10/10
read_and_play_file      ✓ 9/10     ❌ 0/10    ❌ 0/10    ⚠️ 3/10
────────────────────────────────────────────────────────────────
Folder Average:         ✓ 9.7/10   ⚠️ 6.7/10  ⚠️ 6.7/10  ⚠️ 7.3/10
```

---

## Detailed Issues & Fixes

### Issue 1: Hardcoded Windows File Path

**Location:** `read_and_play_file` (Line 1)

**Current Code:**
```plaintext
Read from file: "C:\Users\yuzba\Documents\HIT\Speech\Al_page_13_78.wav"
```

**Problem:**
- Absolute Windows path
- Assumes specific user "yuzba"
- Directory structure Windows-specific
- Will never work on macOS or Linux

**Fix Options:**

**Option A: Relative Path (Recommended)**
```plaintext
Read from file: "audio.wav"
```
- Works on all platforms if file is in same directory
- Simple and portable
- Most common approach

**Option B: User Selection**
```plaintext
filename$ = chooseReadFile$: "Select audio file:"
if filename$ <> ""
    Read from file: filename$
    Play
endif
```
- No hardcoding needed
- User chooses file via GUI
- Works on all platforms
- Most user-friendly

**Option C: Dynamic Path Construction**
```praat
homedir$ = unicode$ (home$)
filename$ = homedir$ + "/Documents/audio.wav"
Read from file: filename$
Play
```
- Works on all platforms
- Uses home directory variable
- Automatic path construction

---

### Issue 2: String vs System Path Handling

**Problem:** Praat scripts mix file APIs with system paths

**Current:**
```plaintext
Read from file: "C:\Users\yuzba\Documents\HIT\Speech\Al_page_13_78.wav"
# Backslash is path separator on Windows only
# Praat may interpret \ as escape character
```

**Better Approach:**
```plaintext
# Praat automatically converts / to platform-native separator
Read from file: "./audio/sample.wav"
# Or simply
Read from file: "audio.wav"
```

---

## Platform-Specific Analysis

### Windows Behavior
```
✓ Praat installed: C:\Program Files\Praat\
✓ Audio files: C:\Users\[username]\Documents\
✓ Backward slashes work
⚠️ Hardcoded paths break for other users
```

**Issues on Windows:**
- Hardcoded user "yuzba" prevents other Windows users from running
- Path assumes Documents folder location (could be networked)
- Breaks if Praat moved to different directory

**Fix:** Make path relative to working directory
```batch
cd C:\Users\yourusername\Documents\HIT\Speech\
praat read_and_play_file --run
```

### macOS Behavior
```
❌ Praat installed: /Applications/Praat.app/
❌ Windows paths don't exist
❌ Backslash handling different
❌ File system is case-sensitive
```

**Issues on macOS:**
- No `C:\` drive
- No `Users\yuzba\` directory structure
- Path separators are `/` not `\`
- Built-in audio library returns error

**Fix:** Use user home directory variable
```praat
homedir$ = unicode$ (home$)
audiodir$ = homedir$ + "/Documents/audio/"
```

### Linux Behavior
```
❌ No Windows file system
❌ Different path structure
❌ Case-sensitive file system
❌ No default audio library
```

**Issues on Linux:**
- No `C:\` drive
- No `Users` directory
- Paths separated by single `/`
- Audio dependencies platform-specific

**Fix:** Use environment variables or relative paths
```bash
export AUDIO_DIR="/home/$USER/audio"
praat read_and_play_file --run
```

---

## Code Quality Assessment

### Code Metrics

| Metric | Value | Assessment |
|--------|-------|-----------|
| Total Lines | 41 lines | Small, maintainable |
| Platform-Aware Code | 0/3 | Not present |
| Error Handling | None | Missing |
| Comments | Minimal | Lacks documentation |
| Path Abstraction | No | Hardcoded |
| File Validation | No | No checks |

### Issues Summary

| Category | Issue | Scripts Affected | Severity |
|----------|-------|-----------------|----------|
| **Paths** | Hardcoded absolute paths | `read_and_play_file` | HIGH |
| **Paths** | Windows-specific separators | `read_and_play_file` | HIGH |
| **Error Handling** | No file existence checks | `read_and_play_file` | MEDIUM |
| **Error Handling** | No try/catch blocks | All files | MEDIUM |
| **Documentation** | No usage instructions | All files | LOW |
| **Testing** | No validation logic | All files | MEDIUM |

---

## Recommended Refactoring Plan

### Priority 1: Critical Fixes (Must Do)

**Fix `read_and_play_file`:**

```plaintext
# CURRENT (Windows only)
Read from file: "C:\Users\yuzba\Documents\HIT\Speech\Al_page_13_78.wav"
Play

# OPTION 1: Simple relative path
Read from file: "audio.wav"
Play

# OPTION 2: Interactive file selection (Recommended)
filename$ = chooseReadFile$: "Select audio file:"
if filename$ <> ""
    Read from file: filename$
    Play
else
    exitScript: "No file selected"
endif
```

**Impact:** Works on all platforms (Windows, macOS, Linux)

**Effort:** ⏱️ 5 minutes

### Priority 2: Enhancements (Should Do)

Add error handling:
```plaintext
filename$ = chooseReadFile$: "Select audio file:"

if filename$ = ""
    exitScript: "No file selected"
endif

if not fileReadable (filename$)
    exitScript: "File not readable: " + filename$
endif

Read from file: filename$

if numberOfSelected ("Sound") <> 1
    exitScript: "Failed to read audio file"
endif

Play
```

**Impact:** Clearer error messages, prevents crashes

**Effort:** ⏱️ 10 minutes

### Priority 3: Documentation (Nice to Have)

Add usage comments:
```plaintext
# read_and_play_file.praat
# Usage: praat read_and_play_file --run
# Prompts user to select audio file and plays it
# Cross-platform compatible (Windows, macOS, Linux)
# Works with WAV, AIFF, and other audio formats
```

**Impact:** Easier to use and maintain

**Effort:** ⏱️ 5 minutes

---

## Implementation Recommendations

### Short Term (Immediate)

1. **Remove hardcoded paths** from all scripts
2. **Use relative paths** for file operations
3. **Add interactive file selection** via `chooseReadFile$()`

### Medium Term (Next Update)

1. Add error handling and validation
2. Add usage documentation/comments
3. Test on macOS and Linux
4. Create cross-platform examples

### Long Term (Ongoing)

1. Collect user feedback on different platforms
2. Monitor Praat updates for new features
3. Standardize script organization
4. Create automated testing suite

---

## Cross-Platform Testing Checklist

- [ ] **Windows 10/11**
  - [ ] Praat installed and working
  - [ ] Audio files accessible
  - [ ] Scripts run from command line
  - [ ] Output files created correctly

- [ ] **macOS (Intel)**
  - [ ] Praat.app installed
  - [ ] Audio files in expected location
  - [ ] Alias/symlink configured
  - [ ] Audio output working

- [ ] **macOS (Apple Silicon)**
  - [ ] ARM64 version installed
  - [ ] Rosetta fallback tested
  - [ ] Audio I/O compatible
  - [ ] Performance acceptable

- [ ] **Linux (Ubuntu)**
  - [ ] Praat installed via package manager
  - [ ] Audio driver configured (ALSA/PulseAudio)
  - [ ] File permissions correct
  - [ ] Output files readable

---

## Before/After Example

### BEFORE (Windows Only)

```plaintext
# read_and_play_file
Read from file: "C:\Users\yuzba\Documents\HIT\Speech\Al_page_13_78.wav"
Play
```

❌ Only works on Windows  
❌ Only for user "yuzba"  
❌ Fails with no error message  

### AFTER (Cross-Platform)

```plaintext
# read_and_play_file.praat
# Cross-platform audio file player
# Prompts user to select file and plays it

filename$ = chooseReadFile$: "Select an audio file:"

if filename$ = ""
    exitScript: "No file selected"
endif

if not fileReadable (filename$)
    exitScript: "File not readable: " + filename$
endif

Read from file: filename$

if numberOfSelected ("Sound") <> 1
    exitScript: "Failed to load audio file"
endif

Play
```

✓ Works on Windows, macOS, Linux  
✓ User selects file via GUI  
✓ Clear error messages  
✓ Validates file before processing  

---

## Summary & Recommendations

| Aspect | Current | Recommended | Priority |
|--------|---------|-------------|----------|
| **Path Handling** | Hardcoded | Relative + interactive | HIGH |
| **Platform Detection** | None | Auto-detection via Praat | MEDIUM |
| **Error Handling** | Missing | Full validation | MEDIUM |
| **Documentation** | Minimal | Full comments | LOW |
| **Multi-OS Readiness** | 3/10 | 9/10 | HIGH |

**Next Action:** Implement Priority 1 fixes (remove hardcoded paths)

**Estimated Implementation Time:** 30 minutes for all three scripts

**Benefit:** Scripts usable on all platforms by all users
