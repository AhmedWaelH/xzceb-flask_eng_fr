import unittest
from translator import french_to_english, english_to_french

class Testfrench_to_english(unittest.TestCase):
    def test_french_to_english1(self):
        self.assertEqual(french_to_english("Bonjour"), "Hello")
        self.assertEqual(french_to_english("Merci"), "Thank you")
        self.assertEqual(french_to_english(""), "")
    
class Testenglish_to_french(unittest.TestCase):
    def test_english_to_french(self):
        self.assertEqual(english_to_french("Hello"), "Bonjour")
        self.assertEqual(english_to_french("Thank you"), "Je vous remercie")
        self.assertEqual(english_to_french(""), "")
if __name__=='__main__':
    unittest.main()
