import unittest

from emotion_detection import emotion_detector

class TestEmotionDetect(unittest.TestCase):
    def testJoy(self):
        result = emotion_detector("I am glad this happened")["dominant_emotion"]
        self.assertEqual(result, "joy")

    def testAnger(self):
        result = emotion_detector("I am really mad about this")["dominant_emotion"]
        self.assertEqual(result, "anger")

    def testDisgust(self):
        result = emotion_detector("I feel disgusted just hearing about this")["dominant_emotion"]
        self.assertEqual(result, "disgust")

    def testSadness(self):
        result = emotion_detector("I am so sad about this")["dominant_emotion"]
        self.assertEqual(result, "sadness")

    def testFear(self):
        result = emotion_detector("I am really afraid that this will happen")["dominant_emotion"]
        self.assertEqual(result, "fear")

unittest.main()