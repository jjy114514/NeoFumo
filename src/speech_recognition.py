import src.speech_recognition as sr
from scipy.spatial.distance import cosine
import numpy as np

class SpeechRecognition:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
        self.known_speakers = {}  # Dictionary to store known speakers and their audio features

    def listen_and_recognize(self):
        with self.microphone as source:
            audio = self.recognizer.listen(source)
            try:
                text = self.recognizer.recognize_google(audio)
                speaker = self.identify_speaker(audio)
                return text, speaker
            except sr.UnknownValueError:
                return None, None

    def identify_speaker(self, audio):
        features = self.extract_features(audio)
        min_distance = float('inf')
        identified_speaker = None

        for speaker, known_features in self.known_speakers.items():
            distance = cosine(features, known_features)
            if distance < min_distance:
                min_distance = distance
                identified_speaker = speaker

        if min_distance < 0.3:  # Threshold for identifying a known speaker
            return identified_speaker
        else:
            return "Unknown"

    def extract_features(self, audio):
        # Implement feature extraction logic, e.g., MFCC
        return np.random.rand(13)  # Placeholder for actual feature extraction

    def stream_audio(self):
        with self.microphone as source:
            while True:
                audio = self.recognizer.listen(source)
                yield audio