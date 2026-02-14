# A6 Voice Assistant Setup Guide

Cross-platform voice assistant using Google Cloud Speech-to-Text and Text-to-Speech APIs.

## Platform Support

- **Windows** (tested)
- **macOS** (Darwin) (tested)
- **Linux** (Ubuntu/Debian)

## Prerequisites

### 1. Google Cloud Setup

1. Create a Google Cloud project: https://console.cloud.google.com
2. Enable these APIs:
   - Google Cloud Speech-to-Text API
   - Google Cloud Text-to-Speech API
3. Create a service account and download JSON credentials

### 2. Python Requirements

- Python 3.7+
- pip or conda package manager

## Installation

### Step 1: Install Python Dependencies

```bash
pip install -r requirements.txt
```

Or with specific versions:

```bash
pip install google-cloud-texttospeech>=0.10.0
pip install google-cloud-speech>=2.14.0
pip install sounddevice>=0.4.4
pip install scipy>=1.5.0
pip install soundfile>=0.10.3
```

### Step 2: Setup Google Cloud Credentials

#### Option A: Environment Variable (Recommended)

**Windows (PowerShell):**
```powershell
$env:GOOGLE_APPLICATION_CREDENTIALS="C:\path\to\your\credentials.json"
```

**Windows (Command Prompt):**
```cmd
set GOOGLE_APPLICATION_CREDENTIALS=C:\path\to\your\credentials.json
```

**macOS/Linux (Bash/Zsh):**
```bash
export GOOGLE_APPLICATION_CREDENTIALS="/path/to/your/credentials.json"
```

#### Option B: Place Credentials File

Simply copy your `credentials.json` to one of these locations:
- Project root directory (same folder as this file)
- `~/.google/credentials.json`
- `~/Downloads/credentials.json`

The application will automatically find it.

## Usage

### 1. Audio Player/Recorder Module

```python
from player import Player

# Create player instance
player = Player(
    sample_rate=44100,    # Audio sample rate
    duration=3,           # Recording duration in seconds
    amplitude=1.0         # Playback volume (1.0 = normal)
)

# Record audio
player.record('my_recording.wav')

# Play audio
player.play('my_recording.wav')
```

### 2. Speech-to-Text Module

```python
from stt_class import STT

# Create STT instance
stt = STT(
    language_code='en-US',   # Language
    sample_rate=44100        # Sample rate of audio
)

# Recognize speech from file
audio = stt.opensoundfile('audio_file.wav')
result = stt.recognize(audio)

# Print transcript
if result and result.results:
    for res in result.results:
        print(f"Transcript: {res.alternatives[0].transcript}")
```

### 3. Text-to-Speech Module

```python
from tts_class import TTS

# Create TTS instance
tts = TTS()

# Generate speech
response = tts.tts_request(
    'Hello, world!',
    language_code='en-US'
)

# Save to file
tts.save2file(response, 'output.wav')
```

### 4. Voice Assistant (Full Example)

```bash
python BL_example.py
```

The voice assistant will:
1. Greet the user
2. Record user voice input
3. Transcribe speech to text
4. Respond with generated speech
5. Continue until user says "stop it"

## Voice Commands

- **"stop it"** - Exit the assistant
- **"hi there"** - Get a greeting response
- **"what's up"** - Get a status response
- Any other phrase - Echoed back by the assistant

## File Structure

```
A6/
├── player.py              # Audio playback and recording
├── stt_class.py           # Speech-to-text class
├── tts_class.py           # Text-to-speech class
├── BL_example.py          # Voice assistant example
├── SETUP.md               # This setup guide
├── credentials.json       # (Optional) Google Cloud credentials
└── audio_files/           # (Auto-created) Temporary audio files
    ├── user_input.wav
    └── tts_output.wav
```

## Troubleshooting

### Issue: "GOOGLE_APPLICATION_CREDENTIALS not set"

**Solution:**
1. Check if environment variable is set: `echo $GOOGLE_APPLICATION_CREDENTIALS` (Unix) or `echo %GOOGLE_APPLICATION_CREDENTIALS%` (Windows)
2. Place `credentials.json` in project directory
3. Verify JSON file is valid

### Issue: Audio playback/recording fails

**Windows:**
- Check audio drivers are installed
- Ensure microphone is connected
- Run as administrator if permission issues

**macOS:**
- Grant microphone permission: System Preferences → Security & Privacy → Microphone
- Ensure audio devices are not in use by other applications

**Linux:**
- Install: `sudo apt install portaudio19-dev`
- Check ALSA config: `alsamixer`

### Issue: Speech recognition not working

**Solutions:**
1. Verify audio file is valid WAV format
2. Check microphone input levels
3. Ensure sample rate matches (default: 44100 Hz)
4. Try a clearer audio source

### Issue: Connection error to Google Cloud

**Solutions:**
1. Check internet connection
2. Verify API keys are enabled
3. Ensure service account has proper permissions
4. Check API quotas: https://console.cloud.google.com/quotas

## Performance Notes

- **Audio Quality**: 44100 Hz (44.1 kHz) is standard for speech recognition
- **Processing Latency**: ~2-3 seconds per recognition request
- **Network Dependency**: All processing requires internet connection
- **File Size**: Typical 30-second audio = ~2.6 MB

## Platform-Specific Notes

### Windows
- Built-in audio APIs fully supported
- PortAudio integrated via pyaudio
- No special setup required

### macOS
- CoreAudio fully supported
- May require microphone permission prompt
- Preferred for low-latency audio

### Linux
- ALSA or PulseAudio required
- Install: `sudo apt install libportaudio2 portaudio19-dev`
- May need to adjust audio input device

## Environment Detection

All modules automatically detect your platform:
```
Running on: Darwin (darwin)      # macOS
Running on: Windows (win32)      # Windows
Running on: Linux (linux)        # Linux
```

## API Costs

Google Cloud services are not free beyond the free tier:
- Speech-to-Text: ~$0.024 per 15 seconds
- Text-to-Speech: ~$0.016 per 1 million characters

Monitor your usage at: https://console.cloud.google.com/billing

## References

- [Google Cloud Speech-to-Text](https://cloud.google.com/speech-to-text/docs)
- [Google Cloud Text-to-Speech](https://cloud.google.com/text-to-speech/docs)
- [SoundDevicePy Documentation](https://python-sounddevice.readthedocs.io/)
- [SciPy Audio Guide](https://docs.scipy.org/doc/scipy/reference/io.wavfile.html)
