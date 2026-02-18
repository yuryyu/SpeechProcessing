# A3 Praat Scripts Test Suite

This folder contains a test suite for the A3 Praat scripts.

## Contents

- `pitch_from_wav.praat`: Extract pitch from WAV file
- `formant_vec_from_wav_part.praat`: Extract formants from WAV file
- `formant_vec_from_wav_part_mul.praat`: Batch formant extraction
- `manipulate_pitch_duration_from_wav.praat`: PSOLA-based manipulation
- `testCommandLineCalls.praat`: Test command-line usage
- `cmd/`: Original command-line examples
- `cmd_refactored/`: Cross-platform command-line examples
- `SETUP.md`: Comprehensive setup guide
- `CODE_ANALYSIS.md`: Analysis of cross-platform readiness
- `REFACTORING_SUMMARY.md`: Summary of refactoring changes
- `test_a3_modules.py`: Test suite for the scripts
- `test_report.md`: Detailed test report

## Requirements

To run the tests, you need:

- Python 3.6+
- Praat installed and accessible in the PATH

## Running the Tests

To run the tests:

```bash
python -m unittest test_a3_modules.py
```

## Test Coverage

The test suite covers:

- File existence and structure
- Cross-platform compatibility
- Documentation quality
- Hardcoded paths
- Comparison of original vs. refactored scripts

## Test Report

See `test_report.md` for a detailed analysis of the test results and recommendations.

## Praat Installation

### Windows

1. Download Praat from: https://www.praat.org/download_win.html
2. Run the installer
3. Add Praat to your PATH

### macOS

1. Download Praat from: https://www.praat.org/download_mac.html
2. Drag Praat to Applications folder
3. Add to PATH: `alias praat="/Applications/Praat.app/Contents/MacOS/Praat"`

### Linux

```bash
sudo apt-get install praat  # Ubuntu/Debian
sudo yum install praat      # CentOS/RedHat
```

## Cross-Platform Usage

### Windows (PowerShell)

```powershell
praat script.praat --open --run
```

### macOS/Linux (Bash)

```bash
praat script.praat --open --run
```

## Troubleshooting

- If Praat is not found, make sure it's installed and in your PATH
- If a script fails, check if it contains hardcoded paths
- For more information, see the SETUP.md file