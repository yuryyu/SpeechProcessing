# Cross-platform Audio Player and Recorder
# Install: pip install sounddevice scipy soundfile

import sys
import platform
from pathlib import Path
import sounddevice as sd
from scipy.io.wavfile import write
import soundfile as sf
import time

# Platform detection
PLATFORM = sys.platform
OS_NAME = platform.system()
print(f"Audio module running on: {OS_NAME} ({PLATFORM})")

class Player:
    """Cross-platform audio player and recorder"""

    def __init__(self, sample_rate=44100, duration=3, amplitude=1.0):
        """
        Initialize Player.
        
        Args:
            sample_rate (int): Audio sample rate in Hz (default: 44100)
            duration (int): Recording duration in seconds (default: 3)
            amplitude (float): Volume amplification factor (default: 1.0)
        """
        self.fs = sample_rate
        self.seconds = duration
        self.AMP = amplitude
        self.platform = OS_NAME        

    def record(self, recordfilepath):
        """
        Record audio from microphone and save to file.
        
        Args:
            recordfilepath (str): Output file path
        """
        try:
            # Create output directory if it doesn't exist
            record_path = Path(recordfilepath)
            record_path.parent.mkdir(parents=True, exist_ok=True)
            
            print(f'Recording to: {record_path}')
            print('Start recording')
            myrecording = sd.rec(
                int(self.seconds * self.fs),
                samplerate=self.fs,
                dtype='int16',
                channels=1
            )
            sd.wait()  # Wait until recording is finished
            print('Stop recording')
            write(str(record_path), self.fs, myrecording)  # Save as WAV file
            print(f'Recording saved to: {record_path}')
        except Exception as e:
            print(f'Failed in Record operation: {e}')        

    def play(self, playfilepath):
        """
        Play audio file.
        
        Args:
            playfilepath (str): Path to audio file
        """
        try:
            play_path = Path(playfilepath)
            if not play_path.exists():
                raise FileNotFoundError(f"Audio file not found: {play_path}")
            
            # Extract data and sampling rate from file
            data, fs = sf.read(str(play_path), dtype='float32')
            print(f'Starting playback: {play_path}')
            sd.play(data * self.AMP, fs)
            sd.wait()  # Wait until file is done playing
            print('Stop playing')
        except FileNotFoundError as e:
            print(f'Audio file error: {e}')
        except Exception as e:
            print(f'Failed in playback operation: {e}')

if __name__ == '__main__':
    # Cross-platform example
    print(f"Running on: {OS_NAME} ({PLATFORM})")
    
    pl = Player()
    
    # Record audio
    print("\n=== Recording Test ===")
    pl.record('test_recording.wav')
    
    # Play audio
    print("\n=== Playback Test ===")
    try:
        pl.play('test_recording.wav')
    except FileNotFoundError:
        print("Test file not found. Create a recording first.")
    