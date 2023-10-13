'''
This file contains the Translator class responsible for translating text files.
'''
from libretranslatepy import LibreTranslateAPI
class Translator:
    def __init__(self):
        self.api = LibreTranslateAPI()
    def translate(self, file_path):
        with open(file_path, "r") as file:
            text = file.read()
        translated_text = self.api.translate(text, "en", "fr")
        return translated_text