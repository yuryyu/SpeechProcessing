"""
Test suite for A1 folder modules
This test file verifies the functionality of the three main Python scripts in the A1 folder:
- wav_play_sounddev.py: WAV file playback using sounddevice
- sin_sampleaudio.py: Sine wave generation and playback
- fftexample.py: FFT computation and visualization

Note: Some tests may be skipped if required modules are not installed.
Required modules:
- numpy
- matplotlib
- sounddevice (optional)
- soundfile (optional)
- simpleaudio (optional)
"""

import unittest
import os
import sys
import importlib
import importlib.util
from unittest.mock import patch, MagicMock

# Check for required modules
try:
    import numpy as np
except ImportError:
    print("WARNING: numpy not installed. Some tests will be skipped.")
    np = None

try:
    import matplotlib
except ImportError:
    print("WARNING: matplotlib not installed. Some tests will be skipped.")
    matplotlib = None

# Optional modules
sounddevice_available = importlib.util.find_spec("sounddevice") is not None
soundfile_available = importlib.util.find_spec("soundfile") is not None
simpleaudio_available = importlib.util.find_spec("simpleaudio") is not None

class TestA1Modules(unittest.TestCase):
    
    def setUp(self):
        """Set up test environment"""
        self.current_dir = os.path.dirname(os.path.abspath(__file__))
        self.wav_file_path = os.path.join(self.current_dir, 'Al_page_13_78.wav')
        
        # Check if the WAV file exists
        self.assertTrue(os.path.exists(self.wav_file_path), 
                        f"Test WAV file not found at {self.wav_file_path}")
    
    def test_wav_file_exists(self):
        """Test if the WAV file exists in the A1 folder"""
        self.assertTrue(os.path.exists(self.wav_file_path))
    
    @unittest.skipIf(np is None or not sounddevice_available or not soundfile_available,
                 "Required modules (numpy, sounddevice, soundfile) not available")
    @patch('matplotlib.pyplot.show')
    @patch('sounddevice.play')
    @patch('sounddevice.wait')
    @patch('soundfile.read')
    def test_wav_play_sounddev(self, mock_sf_read, mock_sd_wait, mock_sd_play, mock_plt_show):
        """Test wav_play_sounddev.py functionality"""
        # Mock the soundfile.read function to return test data
        mock_data = np.array([0.1, 0.2, 0.3, 0.4, 0.5])
        mock_fs = 44100
        mock_sf_read.return_value = (mock_data, mock_fs)
        
        # Import the module
        with patch.dict(sys.modules, {'matplotlib.pyplot': MagicMock()}):
            spec = importlib.util.spec_from_file_location(
                "wav_play_sounddev", 
                os.path.join(self.current_dir, "wav_play_sounddev.py")
            )
            wav_play_module = importlib.util.module_from_spec(spec)
            
            # Execute the module with mocked functions
            with patch('builtins.print') as mock_print:
                spec.loader.exec_module(wav_play_module)
                
                # Verify that soundfile.read was called with the correct filename
                mock_sf_read.assert_called_once()
                self.assertEqual(mock_sf_read.call_args[0][0], 'Al_page_13_78.wav')
                
                # Verify that sounddevice.play was called with the correct data
                mock_sd_play.assert_called_once()
                np.testing.assert_array_almost_equal(
                    mock_sd_play.call_args[0][0], 
                    mock_data * 1.2  # AMP = 1.2 in the script
                )
                
                # Verify that sounddevice.wait was called
                mock_sd_wait.assert_called_once()
                
                # Verify that the expected print statements were made
                mock_print.assert_any_call('Starting playing')
                mock_print.assert_any_call('Stop playing')
    
    @unittest.skipIf(np is None or not simpleaudio_available,
                 "Required modules (numpy, simpleaudio) not available")
    @patch('matplotlib.pyplot.show')
    @patch('simpleaudio.play_buffer')
    def test_sin_sampleaudio(self, mock_sa_play, mock_plt_show):
        """Test sin_sampleaudio.py functionality"""
        # Mock the simpleaudio.play_buffer function
        mock_play_obj = MagicMock()
        mock_sa_play.return_value = mock_play_obj
        
        # Import the module
        with patch.dict(sys.modules, {'matplotlib.pyplot': MagicMock()}):
            with patch('builtins.print') as mock_print:
                spec = importlib.util.spec_from_file_location(
                    "sin_sampleaudio", 
                    os.path.join(self.current_dir, "sin_sampleaudio.py")
                )
                sin_audio_module = importlib.util.module_from_spec(spec)
                
                # Execute the module with mocked functions
                spec.loader.exec_module(sin_audio_module)
                
                # Verify that simpleaudio.play_buffer was called
                mock_sa_play.assert_called_once()
                
                # Verify that the wait_done method was called on the play object
                mock_play_obj.wait_done.assert_called_once()
                
                # Verify that the expected print statements were made
                mock_print.assert_any_call('Start playback')
                mock_print.assert_any_call('Stop playback')
    
    @unittest.skipIf(np is None or matplotlib is None,
                 "Required modules (numpy, matplotlib) not available")
    @patch('matplotlib.pyplot.show')
    def test_fftexample(self, mock_plt_show):
        """Test fftexample.py functionality"""
        # Import the module
        with patch.dict(sys.modules, {'matplotlib.pyplot': MagicMock()}):
            with patch('builtins.print') as mock_print:
                spec = importlib.util.spec_from_file_location(
                    "fftexample", 
                    os.path.join(self.current_dir, "fftexample.py")
                )
                fft_module = importlib.util.module_from_spec(spec)
                
                # Execute the module with mocked functions
                spec.loader.exec_module(fft_module)
                
                # Verify that matplotlib.pyplot.show was called
                mock_plt_show.assert_called_once()
                
                # Verify that the expected print statement was made
                mock_print.assert_any_call('End of FFT script!')
    
    @unittest.skipIf(np is None, "numpy not available")
    def test_sin_wave_generation(self):
        """Test the sine wave generation functionality"""
        frequency = 440
        fs = 44100
        seconds = 0.1  # Short duration for testing
        
        # Generate array with seconds*sample_rate steps, ranging between 0 and seconds
        t = np.linspace(0, seconds, int(seconds * fs), False)
        
        # Generate a sine wave
        note = np.sin(frequency * t * 2 * np.pi)
        
        # Test that the sine wave has the expected length
        self.assertEqual(len(note), int(seconds * fs))
        
        # Test that the sine wave values are within the expected range [-1, 1]
        self.assertTrue(np.all(note >= -1.0))
        self.assertTrue(np.all(note <= 1.0))
        
        # Test that the frequency is approximately correct by checking zero crossings
        zero_crossings = np.where(np.diff(np.signbit(note)))[0]
        if len(zero_crossings) >= 2:
            # Calculate the average number of samples between zero crossings
            avg_samples_between_crossings = np.mean(np.diff(zero_crossings))
            # Each cycle has 2 zero crossings, so divide by 2
            measured_frequency = fs / (avg_samples_between_crossings * 2)
            # Allow for some numerical error
            self.assertAlmostEqual(measured_frequency, frequency, delta=frequency*0.1)
    
    @unittest.skipIf(np is None, "numpy not available")
    def test_fft_computation(self):
        """Test the FFT computation functionality"""
        # Generate a simple signal with known frequency components
        fs = 1000  # sampling rate
        t = np.arange(0, 1, 1/fs)  # time vector (1 second)
        
        # Create a signal with frequencies at 50 Hz and 120 Hz
        f1, f2 = 50, 120
        signal = np.sin(2*np.pi*f1*t) + 0.5*np.sin(2*np.pi*f2*t)
        
        # Compute FFT
        n = len(signal)
        fft_result = np.fft.fft(signal)/n
        freqs = np.fft.fftfreq(n, 1/fs)
        
        # Get the positive frequencies only
        positive_freq_idx = np.where(freqs >= 0)[0]
        freqs = freqs[positive_freq_idx]
        fft_result = fft_result[positive_freq_idx]
        
        # Find the peaks in the FFT magnitude
        magnitude = np.abs(fft_result)
        peaks = []
        for i in range(1, len(magnitude)-1):
            if magnitude[i] > magnitude[i-1] and magnitude[i] > magnitude[i+1]:
                if magnitude[i] > 0.1:  # Threshold to filter out noise
                    peaks.append((freqs[i], magnitude[i]))
        
        # Sort peaks by magnitude
        peaks.sort(key=lambda x: x[1], reverse=True)
        
        # Check that we found at least 2 peaks
        self.assertGreaterEqual(len(peaks), 2)
        
        # Check that the frequencies are approximately correct
        detected_freqs = [peak[0] for peak in peaks[:2]]
        self.assertTrue(any(abs(freq - f1) < 5 for freq in detected_freqs))
        self.assertTrue(any(abs(freq - f2) < 5 for freq in detected_freqs))

if __name__ == '__main__':
    unittest.main()