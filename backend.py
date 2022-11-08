import os
from PyPDF2 import PdfReader
import pyttsx3
from googletrans import Translator

male_names = ["Stefan", "George", "Pablo", "Paul", "Hemant"]
female_names = ["Hazel", "Helena", "Hortense", "Kalpana", "Hedda"]

language_codes = {"english": "en", "french": "fr", "german": "de", "spanish": "es", "hindi": "hi"}

cwd = os.getcwd()
cwd = cwd+"\GCSE_2022"

def load_voices(path=cwd+"\Voices"):
    """
    Downloads the voice register files from the user's system from the path specified.
    :param path: Path to the voice register files
    :return: None
    """
    voices = [voice for voice in pyttsx3.init().getProperty("voices")]
    for filename in os.listdir(path):
        if all(os.path.splitext(filename)[0] not in voice.name for voice in voices):
            os.system(f"{path}\\{filename}")

def pdf_to_text(filename):
    """
    Given the name of pdf file, returns the text from the pdf file.
    :param filename: The filename of the pdf
    :return: The text from the pdf as a string
    """
    pdf = PdfReader(filename)
    return '\n'.join(page.extractText() for page in pdf.pages)

def text_to_speech(txt, lang="English", male=True, speed="medium", volume=100):
    """
    Converts a string of text to mp3 and stores it in the given filename.
    :param txt: A string of text to convert
    :param male: True for male voice, false for female voice
    :param lang: A string representing the language option e.g. "English", "French"
    :param speed: Strings "slow", "medium" and "fast" for slow, medium and fast speeds
    :param volume: Int from 0 to 100, with 0 being silent and 100 being max volume
    :return: None
    """
    engine = pyttsx3.init()

    all_voices = [voice for voice in engine.getProperty("voices")]

    voice_names = male_names if male else female_names
    voices = [voice for voice in all_voices if any(name in voice.name for name in voice_names)]

    voice = [voice for voice in voices if lang.capitalize() in voice.name][0]

    engine.setProperty("rate", {"slow": 100, "medium": 200, "fast": 300}[speed])
    engine.setProperty("voice", voice.id)
    engine.setProperty("volume", volume / 100)

    translated_txt = Translator().translate(txt, dest=language_codes[lang]).text

    engine.say(translated_txt)
    engine.runAndWait()
