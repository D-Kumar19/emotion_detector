"""
Unit tests for emotion_detection module.
"""

import unittest
from emotion_detection import emotion_detector as ed

class TestEmotionDetection(unittest.TestCase):
    """
    Test cases for emotion_detection module.

    Args:
        unittest (unittest.TestCase): Inherits from unittest.TestCase class.
    """

    def test_emotion_detection(self):
        """
        Test cases for emotion_detection module.
        """

        test_1 = 'I am glad this happened'
        expected_output_1 = 'joy'
        self.assertEqual(ed(test_1)['dominant_emotion'] , expected_output_1)

        test_2 = 'I am really mad about this'
        expected_output_2 = 'anger'
        self.assertEqual(ed(test_2)['dominant_emotion'] ,expected_output_2)

        test_3 = 'I feel disgusted just hearing about this'
        expected_output_3 = 'disgust'
        self.assertEqual(ed(test_3)['dominant_emotion'] , expected_output_3)

        test_4 = 'I am so sad about this'
        expected_output_4 = 'sadness'
        self.assertEqual(ed(test_4)['dominant_emotion'] , expected_output_4)

        test_5 = 'I am really afraid that this will happen'
        expected_output_5 = 'fear'
        self.assertEqual(ed(test_5)['dominant_emotion'] , expected_output_5)

if __name__ == "__main__":
    unittest.main()
