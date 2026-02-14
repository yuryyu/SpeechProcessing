# Cross-platform Text-to-Speech using Google Cloud API
# Install: pip install --upgrade google-cloud-texttospeech

import os
import sys
import platform
from pathlib import Path
from google.cloud import texttospeech

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

class TTS:
    """Text-to-Speech class using Google Cloud API"""
    
    def __init__(self):
        """Initialize TTS client"""
        self.client = texttospeech.TextToSpeechClient()
        self.platform = OS_NAME

    def tts_request(self, textstring, language_code='en-US'):
        """
        Request text-to-speech synthesis from Google Cloud API.
        
        Args:
            textstring (str): Text to synthesize
            language_code (str): Language code (default: 'en-US')
            
        Returns:
            google.cloud.texttospeech_v1.TextToSpeechResponse: Audio response
        """
        # Set the text input to be synthesized
        synthesis_input = texttospeech.SynthesisInput(text=textstring)

        # Build the voice request
        voice = texttospeech.VoiceSelectionParams(
            language_code=language_code,
            ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL
        )

        # Select audio encoding
        audio_config = texttospeech.AudioConfig(
            audio_encoding=texttospeech.AudioEncoding.LINEAR16
        )

        # Perform the text-to-speech request
        response = self.client.synthesize_speech(
            input=synthesis_input, voice=voice, audio_config=audio_config
        )
        return response


    def save2file(self, respond, outputfilename='current_tts.wav'):
        """
        Save TTS response to WAV file.
        
        Args:
            respond: TTS response object from Google Cloud API
            outputfilename (str): Output file path
        """
        # Create output directory if it doesn't exist
        output_path = Path(outputfilename)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Write the response to the output file
        with open(output_path, 'wb') as out:
            out.write(respond.audio_content)
            print(f'Audio content written to file: {output_path}')
        return str(output_path)
      


if __name__ == '__main__':
    # Cross-platform example
    output_filename = 'output_tts.wav'
    print(f"Running on: {OS_NAME} ({PLATFORM})")
    
    try:
        tt = TTS()
        respond = tt.tts_request('Humble test request number two')
        tt.save2file(respond, output_filename)
        print(f"Successfully saved TTS output to: {output_filename}")
    except Exception as e:
        print(f"Error: {e}")
        print("Make sure GOOGLE_APPLICATION_CREDENTIALS is set correctly")