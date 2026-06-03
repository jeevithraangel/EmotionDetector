from EmotionDetection.emotion_detection import emotion_detector
import unittest
class TestEmotionDetector(unittest.TestCase):

    def test_joy(self):
        result = emotion_detector("I am very happy")
        self.assertEqual(result["dominant_emotion"], "joy")

    def test_sadness(self):
        result = emotion_detector("I am very sad")
        self.assertEqual(result["dominant_emotion"], "sadness")

    def test_fear(self):
        result = emotion_detector("I am scared of danger")
        self.assertEqual(result["dominant_emotion"], "fear")


if __name__ == "__main__":
    unittest.main()