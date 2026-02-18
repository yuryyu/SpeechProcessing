# A1 Audio Processing Examples

This folder contains examples of audio processing using Python.

## Contents

- `wav_play_sounddev.py`: WAV file playback using sounddevice
- `sin_sampleaudio.py`: Sine wave generation and playback
- `fftexample.py`: FFT computation and visualization
- `Al_page_13_78.wav`: Sample WAV file for testing
- `test_a1_modules.py`: Test suite for the modules
- `test_report.md`: Detailed test report

## Requirements

To run all the examples and tests, you need the following Python packages:

```
pip install numpy matplotlib sounddevice soundfile simpleaudio
```

## Running the Examples

Each Python script can be run directly:

```
python wav_play_sounddev.py
python sin_sampleaudio.py
python fftexample.py
```

## Running the Tests

To run the tests:

```
python -m unittest test_a1_modules.py
```

Note: Some tests may be skipped if the required dependencies are not installed.

## Test Report

See `test_report.md` for a detailed analysis of the test results and recommendations.