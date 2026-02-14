
# Cross-platform Speech-to-Text using Google Cloud API
# Install: pip install google-cloud-speech

import io
import os
import sys
import platform
from pathlib import Path
from google.cloud import speech

# Platform detection
PLATFORM = sys.platform
OS_NAME = platform.system()

# Google Cloud Credentials handling
def setup_google_credentials():
    """
    Setup Google Application Credentials from environment variable.
    Priority:
    1. Check GOOGLE_APPLICATION_CREDENTIALS environment variable
    2. Look for credentials.json in project root or current directory
    3. Raise error if not found
    """
    # Check if credential path is already set in environment
    if 'GOOGLE_APPLICATION_CREDENTIALS' in os.environ:
        cred_path = os.environ['GOOGLE_APPLICATION_CREDENTIALS']
        if os.path.exists(cred_path):
            print(f"Using Google credentials from environment: {cred_path}")
            return
    
    # Look for credentials.json in common locations
    possible_paths = [
        Path.cwd() / 'credentials.json',
        Path.home() / '.google' / 'credentials.json',
        Path.home() / 'Downloads' / 'credentials.json'
    ]
    
    for cred_file in possible_paths:
        if cred_file.exists():
            os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = str(cred_file)
            print(f"Found Google credentials at: {cred_file}")
            return
    
    print("WARNING: GOOGLE_APPLICATION_CREDENTIALS not set")
    print(f"Running on: {OS_NAME} ({PLATFORM})")
    print("Please set GOOGLE_APPLICATION_CREDENTIALS environment variable")
    print("  or place credentials.json in current directory")

# Setup credentials on module load
setup_google_credentials()

class STT:
    """Speech-to-Text class using Google Cloud API"""
    
    def __init__(self, language_code='en-US', sample_rate=44100):
        """
        Initialize STT client.
        
        Args:
            language_code (str): Language code (default: 'en-US')
            sample_rate (int): Sample rate in Hz (default: 44100)
        """
        self.config = speech.RecognitionConfig(
            encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
            sample_rate_hertz=sample_rate,
            language_code=language_code,
        )
        self.client = speech.SpeechClient()
        self.platform = OS_NAME
        

    def opensoundfile(self, file_name):
        """
        Load audio file into memory for recognition.
        
        Args:
            file_name (str): Path to audio file
            
        Returns:
            google.cloud.speech_v1.RecognitionAudio: Audio object
        """
        file_path = Path(file_name)
        if not file_path.exists():
            raise FileNotFoundError(f"Audio file not found: {file_path}")
        
        # Loads the audio into memory
        with io.open(str(file_path), "rb") as audio_file:
            content = audio_file.read()
            audio = speech.RecognitionAudio(content=content)
        return audio

    def recognize(self, audio):
        """
        Recognize speech from audio.
        
        Args:
            audio: RecognitionAudio object
            
        Returns:
            google.cloud.speech_v1.RecognizeResponse: Recognition results
        """
        try:
            response = self.client.recognize(config=self.config, audio=audio)
            return response
        except Exception as e:
            print(f'Error during speech recognition: {e}')
            return None    

if __name__ == '__main__':
    # Cross-platform example
    file_name = 'test_audio.wav'
    print(f"Running on: {OS_NAME} ({PLATFORM})")
    
    try:
        st = STT()
        audio = st.opensoundfile(file_name)
        rz = st.recognize(audio)
        
        if rz and rz.results:
            for result in rz.results:
                print(f"Transcript: {result.alternatives[0].transcript}")
        else:
            print("No speech recognized")
    except FileNotFoundError as e:
        print(f"Error: {e}")
        print(f"Usage: Place '{file_name}' in current directory")
    except Exception as e:
        print(f"Error: {e}")
        print("Make sure GOOGLE_APPLICATION_CREDENTIALS is set correctly")
