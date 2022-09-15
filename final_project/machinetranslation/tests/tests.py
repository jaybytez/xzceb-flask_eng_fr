"""
Test the translator functions
"""
import unittest

from translator import english_to_french, french_to_english

class TestEnglishToFrench(unittest.TestCase):
    """
    Tests for english text translation
    """
    def test_translate_empty(self):
        """
        Test empty string returns None
        """
        self.assertIsNone(english_to_french(""))

    def test_translate_none(self):
        """
        Test None param returns None
        """
        self.assertIsNone(english_to_french(None))

    def test_translate_str(self):
        """
        Test valid string is translated correctly
        """
        self.assertEqual(english_to_french('Hello'), 'Bonjour')

class TestFrenchToEnglish(unittest.TestCase):
    """
  Tests for french text translation
  """
    def test_translate_empty(self):
        """
        Test empty string returns None
        """
        self.assertIsNone(french_to_english(""))

    def test_translate_none(self):
        """
        Test None param returns None
        """
        self.assertIsNone(french_to_english(None))

    def test_translate_str(self):
        """
        Test valid string is translated correctly
        """
        self.assertEqual(french_to_english('Bonjour'), 'Hello')

unittest.main()
