from src.speech_recognition import SpeechRecognition
from src.hardware_interface import HardwareInterface
from src.database import Database
from src.ai_chat import AIChat
from src.knowledge_query import KnowledgeQuery

def main():
    sr = SpeechRecognition()
    hw = HardwareInterface()
    db = Database()
    ai = AIChat(api_key='your_openai_api_key')
    kq = KnowledgeQuery()

    for audio in sr.stream_audio():
        text, speaker = sr.listen_and_recognize()
        if text and speaker:
            db.insert_conversation(speaker, text)
            if ai.should_respond(text):
                response = ai.ask_ai(text)
                hw.play_audio(response)
                hw.display_text(response)

if __name__ == "__main__":
    main()
