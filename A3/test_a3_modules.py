"""
Test suite for A3 folder modules
This test file verifies the functionality of the Praat scripts in the A3 folder.
"""

import unittest
import os
import sys
import subprocess
import tempfile
import shutil
import re
from pathlib import Path
import platform

class TestA3PraatScripts(unittest.TestCase):
    
    def setUp(self):
        """Set up test environment"""
        self.current_dir = Path(__file__).parent
        
        # Create temporary directory for output files
        self.temp_dir = Path(tempfile.mkdtemp())
    
    def test_file_existence(self):
        """Test if all required files exist"""
        required_files = [
            "pitch_from_wav.praat",
            "formant_vec_from_wav_part.praat",
            "formant_vec_from_wav_part_mul.praat",
            "manipulate_pitch_duration_from_wav.praat",
            "testCommandLineCalls.praat",
            "SETUP.md",
            "CODE_ANALYSIS.md"
        ]
        
        for file in required_files:
            file_path = self.current_dir / file
            self.assertTrue(file_path.exists(), f"Required file not found: {file}")
    
    def test_cmd_folder_structure(self):
        """Test if the cmd folder has the expected structure"""
        cmd_dir = self.current_dir / "cmd"
        self.assertTrue(cmd_dir.exists(), "cmd directory not found")
        
        expected_files = [
            "create_sin_play",
            "pitch_textGrid_man",
            "read_and_play_file"
        ]
        
        for file in expected_files:
            file_path = cmd_dir / file
            self.assertTrue(file_path.exists(), f"Required file not found in cmd directory: {file}")
    
    def test_cmd_refactored_folder_structure(self):
        """Test if the cmd_refactored folder has the expected structure"""
        cmd_refactored_dir = self.current_dir / "cmd_refactored"
        self.assertTrue(cmd_refactored_dir.exists(), "cmd_refactored directory not found")
        
        expected_files = [
            "create_sin_play.praat",
            "pitch_textGrid_man.praat",
            "read_and_play_file.praat",
            "README.md"
        ]
        
        for file in expected_files:
            file_path = cmd_refactored_dir / file
            self.assertTrue(file_path.exists(), f"Required file not found in cmd_refactored directory: {file}")
    
    def test_cross_platform_compatibility(self):
        """Test if the refactored scripts are cross-platform compatible"""
        # Check if the refactored scripts use relative paths instead of absolute paths
        refactored_scripts = [
            self.current_dir / "cmd_refactored" / "create_sin_play.praat",
            self.current_dir / "cmd_refactored" / "pitch_textGrid_man.praat",
            self.current_dir / "cmd_refactored" / "read_and_play_file.praat"
        ]
        
        for script_path in refactored_scripts:
            if not script_path.exists():
                continue
            
            try:
                with open(script_path, "r", encoding="utf-8") as f:
                    content = f.read()
            except UnicodeDecodeError:
                with open(script_path, "r", encoding="latin-1") as f:
                    content = f.read()
            
            # Check for Windows-specific absolute paths
            self.assertNotRegex(content, r'C:\\Users', 
                               f"Script {script_path.name} contains Windows-specific absolute paths")
            
            # Check for platform-specific path separators
            self.assertNotRegex(content, r'\\\\', 
                               f"Script {script_path.name} contains Windows-specific path separators")
    
    def test_documentation_quality(self):
        """Test the quality of documentation files"""
        doc_files = [
            self.current_dir / "SETUP.md",
            self.current_dir / "CODE_ANALYSIS.md",
            self.current_dir / "cmd_refactored" / "README.md"
        ]
        
        for doc_path in doc_files:
            if not doc_path.exists():
                continue
            
            try:
                with open(doc_path, "r", encoding="utf-8") as f:
                    content = f.read()
            except UnicodeDecodeError:
                with open(doc_path, "r", encoding="latin-1") as f:
                    content = f.read()
            
            # Check if the documentation has a minimum length
            self.assertGreater(len(content), 500, 
                              f"Documentation file {doc_path.name} is too short")
            
            # Check if the documentation mentions all platforms
            self.assertIn("Windows", content, 
                         f"Documentation file {doc_path.name} should mention Windows")
            self.assertIn("macOS", content, 
                         f"Documentation file {doc_path.name} should mention macOS")
            self.assertIn("Linux", content, 
                         f"Documentation file {doc_path.name} should mention Linux")
    
    def test_hardcoded_paths(self):
        """Test if the original scripts contain hardcoded paths"""
        original_scripts = [
            self.current_dir / "pitch_from_wav.praat",
            self.current_dir / "formant_vec_from_wav_part.praat",
            self.current_dir / "formant_vec_from_wav_part_mul.praat",
            self.current_dir / "manipulate_pitch_duration_from_wav.praat"
        ]
        
        for script_path in original_scripts:
            if not script_path.exists():
                continue
            
            try:
                with open(script_path, "r", encoding="utf-8") as f:
                    content = f.read()
            except UnicodeDecodeError:
                with open(script_path, "r", encoding="latin-1") as f:
                    content = f.read()
            
            # Check for Windows-specific absolute paths
            if re.search(r'C:\\Users', content):
                print(f"Script {script_path.name} contains Windows-specific absolute paths")
    
    def test_original_vs_refactored(self):
        """Test if the refactored scripts are improvements over the originals"""
        # Check if the original cmd scripts have hardcoded paths
        original_cmd_scripts = [
            self.current_dir / "cmd" / "read_and_play_file"
        ]
        
        for script_path in original_cmd_scripts:
            if not script_path.exists():
                continue
            
            try:
                with open(script_path, "r", encoding="utf-8") as f:
                    content = f.read()
            except UnicodeDecodeError:
                with open(script_path, "r", encoding="latin-1") as f:
                    content = f.read()
            
            # Check for Windows-specific absolute paths
            if re.search(r'C:\\Users', content):
                print(f"Original script {script_path.name} contains Windows-specific absolute paths")
        
        # Check if the refactored scripts have improved error handling
        refactored_scripts = [
            self.current_dir / "cmd_refactored" / "read_and_play_file.praat"
        ]
        
        for script_path in refactored_scripts:
            if not script_path.exists():
                continue
            
            try:
                with open(script_path, "r", encoding="utf-8") as f:
                    content = f.read()
            except UnicodeDecodeError:
                with open(script_path, "r", encoding="latin-1") as f:
                    content = f.read()
            
            # Check for error handling
            self.assertIn("if not fileReadable", content, 
                         f"Refactored script {script_path.name} should have file validation")
            
            # Check for user feedback
            self.assertIn("appendInfoLine", content, 
                         f"Refactored script {script_path.name} should have user feedback")
    
    def tearDown(self):
        """Clean up after tests"""
        # Remove the temporary directory
        if os.path.exists(self.temp_dir):
            try:
                shutil.rmtree(self.temp_dir)
            except:
                pass

if __name__ == '__main__':
    unittest.main()