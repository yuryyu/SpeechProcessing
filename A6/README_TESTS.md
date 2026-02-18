# A6 Voice Assistant Test Suite

This folder contains a test suite for the A6 Voice Assistant application.

## Contents

- `tts_class.py`: Text-to-Speech using Google Cloud API
- `stt_class.py`: Speech-to-Text using Google Cloud API
- `player.py`: Audio playback and recording
- `BL_example.py`: Voice assistant business logic
- `SETUP.md`: Comprehensive setup guide
- `requirements.txt`: List of dependencies
- `REFACTORING_SUMMARY.md`: Summary of refactoring changes
- `test_a6_modules.py`: Test suite for the modules
- `test_report.md`: Detailed test report

## Requirements

To run all the examples and tests, you need the following Python packages:

```
pip install -r requirements.txt
```

The main requirements are:
- Google Cloud APIs (google-cloud-texttospeech, google-cloud-speech)
- Audio processing libraries (sounddevice, scipy, soundfile)

## Running the Tests

To run the tests:

```
python -m unittest test_a6_modules.py
```

Note: Many tests will be skipped if the required dependencies are not installed.

## Google Cloud Credentials

To fully test the application, you need to set up Google Cloud credentials:

1. Create a Google Cloud project
2. Enable the Speech-to-Text and Text-to-Speech APIs
3. Create a service account and download JSON credentials
4. Set the GOOGLE_APPLICATION_CREDENTIALS environment variable

See `SETUP.md` for detailed instructions.

## Test Coverage

The test suite covers:
- File existence and structure
- Module initialization
- TTS functionality
- STT functionality
- Audio playback and recording
- Business logic
- Credential setup

## Test Report

See `test_report.md` for a detailed analysis of the test results and recommendations.