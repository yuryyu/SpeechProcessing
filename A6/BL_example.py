import sys
import platform
import time
from pathlib import Path
from player import Player
from stt_class import STT
from tts_class import TTS

# Platform detection
PLATFORM = sys.platform
OS_NAME = platform.system()

# Cross-platform file paths (relative to script location)
SCRIPT_DIR = Path(__file__).parent
OUTPUT_DIR = SCRIPT_DIR / 'audio_files'
OUTPUT_DIR.mkdir(exist_ok=True)

# Audio file paths
user_response_file = OUTPUT_DIR / 'user_input.wav'
tts_file = OUTPUT_DIR / 'tts_output.wav'

sys_delay = 3  # delay in seconds

def bl(pl, st, ts):
    """
    Business logic for interactive voice assistant.
    
    Args:
        pl (Player): Audio player instance
        st (STT): Speech-to-text instance
        ts (TTS): Text-to-speech instance
    """
    try:
        # First greeting
        print("\n=== Starting Voice Assistant ===")
        greeting_response = ts.tts_request('Hello my dear. Please say something')
        ts.save2file(greeting_response, str(tts_file))
        pl.play(str(tts_file))
        time.sleep(sys_delay)
        
        running = True
        while running:
            # Record user input
            pl.record(str(user_response_file))
            time.sleep(sys_delay)
            
            # Recognize speech
            try:
                audio = st.opensoundfile(str(user_response_file))
                recognition = st.recognize(audio)
                user_response = (
                    recognition.results[0].alternatives[0].transcript
                    if recognition and recognition.results
                    else ''
                )
            except Exception as e:
                print(f"Recognition error: {e}")
                user_response = ''
            
            print(f"User said: {user_response}")
            time.sleep(1)
            
            # Process user response
            if len(user_response) == 0:
                response_text = 'Sorry, could you repeat, please?'
            elif 'stop it' in user_response.lower():
                response_text = 'OK, goodbye my good friend'
                running = False
            elif 'hi there' in user_response.lower():
                response_text = 'What can I do for you, dear?'
            elif "what's up" in user_response.lower():
                response_text = 'Nothing new, comrade'
            else:
                response_text = 'I heard you say: ' + user_response
            
            # Text-to-speech response
            response = ts.tts_request(response_text)
            ts.save2file(response, str(tts_file))
            time.sleep(sys_delay)
            pl.play(str(tts_file))
            time.sleep(sys_delay)
        
        print("\n=== Voice Assistant Ended ===")
        
    except KeyboardInterrupt:
        print("\nVoice assistant interrupted by user")
    except Exception as e:
        print(f"Error in business logic: {e}")

if __name__ == '__main__':
    print(f"Running on: {OS_NAME} ({PLATFORM})")
    print(f"Output directory: {OUTPUT_DIR}")
    print()
    
    try:
        pl = Player()
        st = STT()
        ts = TTS()
        print('Starting voice assistant example')
        bl(pl, st, ts)
        print('End of voice assistant example')
    except Exception as e:
        print(f"Fatal error: {e}")
        print("Make sure Google Cloud credentials are configured")
        sys.exit(1)
