# test_studybridge.py
"""
Tests for StudyBridge module.
"""

import unittest
from studybridge import StudyBridge

class TestStudyBridge(unittest.TestCase):
    """Test cases for StudyBridge class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = StudyBridge()
        self.assertIsInstance(instance, StudyBridge)
        
    def test_run_method(self):
        """Test the run method."""
        instance = StudyBridge()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
