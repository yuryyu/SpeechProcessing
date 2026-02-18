# A2 Audio Recording and Processing Examples

This folder contains examples of audio recording, playback, and visualization using Python.

## Contents

- `wav_play_sounddev.py`: WAV file playback using sounddevice
- `spectrogram_on_wav.py`: Generate spectrogram from WAV file
- `rec_wav.py`: Record audio using sounddevice and save as WAV
- `rec_pyaudio.py`: Record audio using PyAudio and save as WAV
- `record.py`: Another audio recording script using sounddevice
- `test_a2_modules.py`: Test suite for the modules
- `test_report.md`: Detailed test report

## Requirements

To run all the examples and tests, you need the following Python packages:

```
pip install numpy matplotlib sounddevice soundfile pyaudio scipy
```

## Running the Examples

Each Python script can be run directly:

```
python wav_play_sounddev.py
python spectrogram_on_wav.py
python rec_wav.py
python rec_pyaudio.py
python record.py
```

Note: Some scripts may require a microphone for recording or speakers for playback.

## Running the Tests

To run the tests:

```
python -m unittest test_a2_modules.py
```

Note: Some tests may be skipped if the required dependencies are not installed.

## Test Report

See `test_report.md` for a detailed analysis of the test results and recommendations.