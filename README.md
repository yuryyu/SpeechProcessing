# SpeechProcessing

Supplementary materials for Speech Processing with Python. This repository contains practical examples for audio signal processing, including audio playback, recording, FFT analysis, and spectrogram visualization.

## Installation

Install all required dependencies:

```bash
pip install -r requirements.txt
```

## Supported Platforms

- Windows
- macOS (Darwin)
- Linux

All Python files include automatic platform detection and conditional imports for cross-platform compatibility.

## Directory Structure

```
SpeechProcessing/
├── A1/                          # Assignment 1 - Audio Playback & Analysis
├── A2/                          # Assignment 2 - Audio Recording & Visualization
├── requirements.txt             # Project dependencies with version constraints
└── test_platform_detection.py  # Platform detection validation script
```

## Python Files Description

### Assignment 1: Audio Playback & Analysis (A1/)

#### fftexample.py
Demonstrates Fast Fourier Transform (FFT) analysis on a synthetic audio signal.

**Features:**
- Generates a 12 Hz sine wave
- Performs FFT to compute frequency domain representation
- Plots time-domain and frequency-domain signals
- Calculates one-sided frequency spectrum

**Dependencies:** numpy, matplotlib

**Output:** Displays plots of signal and frequency spectrum

---

#### sin_sampleaudio.py
Generates and plays a 440 Hz sine wave tone using simpleaudio library.

**Features:**
- Generates a 440 Hz pure tone (A4 note)
- Plays audio with conditional import error handling
- Supports optional visualization of waveform
- Cross-platform audio playback

**Dependencies:** numpy, simpleaudio, matplotlib (optional)

**Output:** Plays audio tone for 3 seconds, optionally displays waveform plot

---

#### wav_play_sounddev.py
Reads and plays WAV audio files using sounddevice library with optional amplification.

**Features:**
- Loads and reads WAV files using soundfile
- Plays audio using sounddevice
- Volume amplification support (AMP factor configurable)
- Optional waveform visualization
- Cross-platform audio playback

**Dependencies:** sounddevice, soundfile, matplotlib (optional)

**Usage:** Modify `filename` variable to point to your WAV file

**Output:** Plays audio file with specified amplification

---

### Assignment 2: Audio Recording & Visualization (A2/)

#### rec_pyaudio.py
Records audio from microphone using PyAudio library with PortAudio backend.

**Features:**
- Records stereo audio (2 channels)
- Configurable sample rate (44100 Hz)
- Records in 1024-sample chunks for efficiency
- Saves output to WAV file
- Uses 16-bit PCM format

**Dependencies:** pyaudio, wave

**Output:** Saves recording to `output.wav` (3 seconds)

**Parameters:**
- `channels = 2` - Stereo recording
- `fs = 44100` - Sample rate in Hz
- `seconds = 3` - Recording duration

---

#### rec_wav.py
Records stereo audio from microphone using sounddevice and saves to WAV format.

**Features:**
- Records stereo audio (2 channels)
- Uses scipy for WAV file writing
- Sample rate: 44100 Hz
- Recording duration: 3 seconds

**Dependencies:** sounddevice, scipy

**Output:** Saves recording to `output_one.wav`

---

#### record.py
Records mono audio from microphone using sounddevice and saves to WAV format.

**Features:**
- Records mono audio (1 channel)
- 16-bit signed integer format
- Uses scipy for WAV file writing
- Sample rate: 44100 Hz
- Recording duration: 2 seconds

**Dependencies:** sounddevice, scipy

**Output:** Saves recording to `output_ee.wav`

---

#### spectrogram_on_wav.py
Analyzes WAV audio file and generates spectrogram visualization.

**Features:**
- Reads WAV files and extracts audio data
- Plots time-domain waveform
- Generates spectrogram (frequency vs. time representation)
- Automatically calculates optimal FFT window size
- Saves visualization as PNG image
- Displays plots interactively

**Dependencies:** wave, numpy, matplotlib, scipy

**Input:** WAV file (default: `output_ee.wav`)

**Output:**
- Interactive plot with waveform and spectrogram
- PNG image: `spectrogram_<filename>.png`

**Parameters:**
- `time_window = 0.04` - 40 ms FFT window duration

---

#### wav_play_sounddev.py
Reads and plays WAV audio files with optional volume amplification.

**Features:**
- Loads and reads WAV files using soundfile
- Plays audio using sounddevice
- Configurable volume amplification
- Optional waveform visualization
- Cross-platform audio playback

**Dependencies:** sounddevice, soundfile, matplotlib (optional)

**Usage:** Modify `filename` variable to point to your WAV file

**Parameters:**
- `AMP = 2` - Volume amplification factor

---

## Platform Detection

All Python files automatically detect the running platform and print platform information:

```
Running on: Darwin (darwin)
```

This uses:
- `sys.platform` - Short platform identifier (darwin, win32, linux)
- `platform.system()` - Full OS name (Darwin, Windows, Linux)

## Testing

Run the platform detection validation script:

```bash
python test_platform_detection.py
```

This verifies that all Python files have correct platform detection imports and syntax.

## Dependencies Overview

**Core Audio Libraries:**
- `sounddevice` - Cross-platform audio I/O
- `soundfile` - WAV file reading/writing
- `pyaudio` - Audio recording via PortAudio

**Audio Playback:**
- `simpleaudio` - Simple cross-platform audio playback

**Scientific Computing:**
- `numpy` - Numerical computations
- `scipy` - Scientific functions (FFT, WAV operations)
- `matplotlib` - Visualization and plotting
